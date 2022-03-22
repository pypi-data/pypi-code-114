import os
from collections import OrderedDict
from os.path import expanduser
from typing import Dict, List, Union, Sequence, Optional, Tuple, Type, Any

import numpy as np
import pandas as pd

from d3m import container, utils
from d3m.base import utils as base_utils
from d3m.metadata import base as metadata_base, hyperparams, params
from d3m.primitive_interfaces.base import CallResult
from d3m.primitive_interfaces.supervised_learning import SupervisedLearnerPrimitiveBase
from d3m.exceptions import PrimitiveNotFittedError

from fastai.data.transforms import Normalize
from fastai.optimizer import Adam, RMSProp
from fastai.losses import CrossEntropyLossFlat, BCEWithLogitsLossFlat, LabelSmoothingCrossEntropy, LabelSmoothingCrossEntropyFlat
from fastai.metrics import F1Score, accuracy
from fastai.vision.all import ImageDataLoaders, cnn_learner, imagenet_stats
from fastai.vision.augment import Resize, Dihedral, Rotate, Flip
from fastai.vision.models import resnet18, resnet50, densenet201
from fastai.learner import Learner

from efficientnet_pytorch import EfficientNet

import torch

__all__ = ('FastAIWrapperPrimitive',)

Inputs = container.DataFrame
Outputs = container.DataFrame


_LOSS_FUNCTIONS = {
    'CrossEntropyLossFlat': CrossEntropyLossFlat,
    'BCEWithLogitsLossFlat': BCEWithLogitsLossFlat,
    'LabelSmoothingCrossEntropy': LabelSmoothingCrossEntropy,
    'LabelSmoothingCrossEntropyFlat': LabelSmoothingCrossEntropyFlat,
}

_METRICS = {
    'accuracy': accuracy,
    'F1Score': F1Score,
}

_OPT_FUNCTIONS = {
    'Adam': Adam,
    'RMSProp': RMSProp,
}


class Params(params.Params):
    learner_: Optional[Learner]
    input_column_names: Optional[pd.core.indexes.base.Index]
    target_names_: Optional[Sequence[Any]]
    training_indices_: Optional[Sequence[int]]
    target_column_indices_: Optional[Sequence[int]]
    target_columns_metadata_: Optional[List[OrderedDict]]


class Hyperparams(hyperparams.Hyperparams):
    # hyperparams for imagedataloader
    valid_pct = hyperparams.Uniform(
        lower=0,
        upper=1,
        default=0.2,
        description='The Validation Split Percentage',
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/TuningParameter'
            ],
    )
    num_workers = hyperparams.Bounded[int](
        lower=0,
        upper=None,
        default=2,
        description='Number of subprocesses to use for data loading',
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/ResourcesUseParameter',
            'https://metadata.datadrivendiscovery.org/types/ControlParameter'
        ],
    )
    bs = hyperparams.Bounded[int](
        lower=1,
        upper=None,
        default=5,
        description='Batch Size',
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/TuningParameter',
        ],
    )
    model = hyperparams.Enumeration[str](
        values=['resnet18', 'resnet50', 'densenet201', 'efficientnetb0'],
        default='efficientnetb0',
        description="Pre-trained model to be used",
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/ControlParameter'
        ],
    )
    metrics = hyperparams.Enumeration[str](
        values=list(_METRICS),
        default='accuracy',
        description="Metrics to be used for evaluation",
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/ControlParameter'
        ],
    )
    epochs = hyperparams.Bounded[int](
        lower=1,
        upper=None,
        default=5,
        description="Number of epochs",
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/TuningParameter',
        ],
    )
    pretrained = hyperparams.UniformBool(
        default=True,
        description='Pretrain the model',
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/ControlParameter'
        ],
    )
    norm = hyperparams.UniformBool(
        default=True,
        description="Normalization",
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/ControlParameter'
        ],
    )
    loss_fn = hyperparams.Enumeration[str](
        values=list(_LOSS_FUNCTIONS),
        default='CrossEntropyLossFlat',
        description="Loss Function",
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/ControlParameter'
        ],
    )
    opt_fn = hyperparams.Enumeration[str](
        values=list(_OPT_FUNCTIONS),
        default='Adam',
        description="Optimization Function",
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/ControlParameter'
        ],
    )
    use_inputs_columns = hyperparams.Set(
        elements=hyperparams.Hyperparameter[int](-1),
        default=(),
        description="A set of inputs column indices to force primitive to operate on. If any specified column cannot be used, it is skipped.",
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/ControlParameter'
        ]
    )
    exclude_inputs_columns = hyperparams.Set(
        elements=hyperparams.Hyperparameter[int](-1),
        default=(),
        description="A set of inputs column indices to not operate on. Applicable only if \"use_columns\" is not provided.",
        semantic_types=[
            'https://metadata.datadrivendiscovery.org/types/ControlParameter'
        ],
    )
    use_outputs_columns = hyperparams.Set(
        elements=hyperparams.Hyperparameter[int](-1),
        default=(),
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="A set of outputs column indices to force primitive to operate on.",
    )
    exclude_outputs_columns = hyperparams.Set(
        elements=hyperparams.Hyperparameter[int](-1),
        default=(),
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="A set of outputs column indices to not operate on. Applicable only if \"use_columns\" is not provided.",
    )
    return_result = hyperparams.Enumeration(
        values=['append', 'replace', 'new'],
        # Default value depends on the nature of the primitive.
        default='append',
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="Defines if result columns should append or replace original columns",
    )
    use_semantic_types = hyperparams.UniformBool(
        default=False,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="Controls whether semantic_types metadata will be used for filtering columns in input dataframe.",
    )
    add_index_columns = hyperparams.UniformBool(
        default=False,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="Also include primary index columns if input data has them. Applicable only if \"return_result\" is set to \"new\".",
    )
    error_on_no_input = hyperparams.UniformBool(
        default=True,
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter'],
        description="Throw an exception if no input column is selected/provided.",
    )
    return_semantic_type = hyperparams.Enumeration[str](
        values=[
            'https://metadata.datadrivendiscovery.org/types/Attribute',
            'https://metadata.datadrivendiscovery.org/types/ConstructedAttribute',
            'https://metadata.datadrivendiscovery.org/types/PredictedTarget'
        ],
        default='https://metadata.datadrivendiscovery.org/types/PredictedTarget',
        description='Decides what semantic type to attach to generated output',
        semantic_types=['https://metadata.datadrivendiscovery.org/types/ControlParameter']
    )


class FastAIWrapperPrimitive(SupervisedLearnerPrimitiveBase[Inputs, Outputs, Params, Hyperparams]):
    """
    A Wrapper for FastAI Transfer Learning.

    It uses semantic types to determine which columns to operate on.
    """
    __author__ = 'JPL DARPA D3M Team'
    _weights_configs = [{
        'type': 'TGZ',
        'key': 'resnet50_fastai.pth',
        'file_uri': 'https://github.com/bhavints/d3m_jpl/releases/download/v1.0/models.tar.gz',
        'file_digest': '132628b7408554d017fe0e698931646920bbd18ea058a801e81bf19ff8770a9e',
    }]
    metadata = metadata_base.PrimitiveMetadata(
        {
            'id': '26582450-8b6a-4a5e-abd8-cbf557873cdb',
            'version': '0.1.0',
            'name': "FastAI Vision Wrapper",
            'python_path': 'd3m.primitives.classification.Convolutional_neural_network.Fastai',
            'keywords': ['Transfer Learning', 'Computer Vision'],
            'source': {
                'name': 'JPL',
                'contact': 'mailto:bhavin.t.shah@jpl.nasa.gov',
                'uris': [
                    'https://gitlab.com/datadrivendiscovery/fastai_prims/-/issues'
                ],
            },
            'installation': [{
                'type': metadata_base.PrimitiveInstallationType.PIP,
                'package_uri': 'git+https://gitlab.com/datadrivendiscovery/fastai_prims.git@{git_commit}#egg=fastai_prims'.format(
                    git_commit=utils.current_git_commit(os.path.dirname(__file__)),
                ),
            }] + _weights_configs,
            'algorithm_types': [
                metadata_base.PrimitiveAlgorithmType.CONVOLUTIONAL_NEURAL_NETWORK,
            ],
            'primitive_family': metadata_base.PrimitiveFamily.CLASSIFICATION,
            'hyperparams_to_tune': [
                'valid_pct',
                'bs',
                'epochs',
            ]
        }
    )

    def __init__(self, *, hyperparams: Hyperparams, random_seed: int = 0, _verbose: int = 0, volumes: Union[Dict[str, str], None] = None) -> None:
        super().__init__(hyperparams=hyperparams, random_seed=random_seed, volumes=volumes)
        self.volumes = volumes
        # We need random seed multiple times (every time an underlying "RandomForestClassifier" is instantiated),
        # and when we sample. So instead we create our own random state we use everywhere.
        self._random_state = np.random.RandomState(self.random_seed)
        self._verbose = _verbose
        self._inputs: container.DataFrame
        self._outputs: container.DataFrame
        self._training_indices: List[int] = []
        self._training_inputs: container.DataFrame
        self._training_outputs: container.DataFrame
        self._image_loader: Any = None
        self._is_fit = False
        self._target_columns_metadata: List[OrderedDict[Any, Any]] = []
        self._target_column_indices: List[Any]
        self._input_column_names = None
        self._target_names: List[Any]
        self._model_path = self._find_weights_dir(key_filename=self._weights_configs[0]['key'], weights_configs=self._weights_configs[0])

    def set_training_data(self, *, inputs: container.DataFrame, outputs: container.DataFrame) -> None:
        self._inputs = inputs
        self._outputs = outputs
        self._is_fit = False
        self._new_training_data = True

    def _get_images_path(self, input_dataframe: container.DataFrame = Inputs) -> str:
        image_path: list = []
        for i in range(input_dataframe.metadata.query((metadata_base.ALL_ELEMENTS,))['dimension']['length']):
            column_metada = input_dataframe.metadata.query((metadata_base.ALL_ELEMENTS, i,))
            if 'semantic_types' in column_metada and 'https://metadata.datadrivendiscovery.org/types/FileName' in \
                    column_metada['semantic_types']:
                if 'location_base_uris' not in column_metada:
                    raise ValueError(
                        'File Column {} does not contains "location_base_uris"'.format(column_metada['name']))
                else:
                    image_path = column_metada['location_base_uris']
                    break
        return image_path[0][7:]

    def _find_weights_dir(self, key_filename, weights_configs):
        _weight_file_path = None
        # Check common places
        if key_filename in self.volumes:
            _weight_file_path = self.volumes[key_filename]
            if not os.path.isfile(_weight_file_path):
                _weight_file_path = os.path.join(self.volumes[key_filename], key_filename)
                if not os.path.isfile(_weight_file_path):
                    _weight_file_path = os.path.join(self.volumes[key_filename], weights_configs['file_digest'], key_filename)

        else:
            if os.path.isdir('/static'):
                _weight_file_path = os.path.join('/static', weights_configs['file_digest'], key_filename)
                if not os.path.exists(_weight_file_path):
                    _weight_file_path = os.path.join('/static', weights_configs['file_digest'])
            # Check other directories
            if not os.path.exists(_weight_file_path):
                home = expanduser("/")
                root = expanduser("~")
                _weight_file_path = os.path.join(home, weights_configs['file_digest'])
                if not os.path.exists(_weight_file_path):
                    _weight_file_path = os.path.join(home, weights_configs['file_digest'], key_filename)
                if not os.path.exists(_weight_file_path):
                    _weight_file_path = os.path.join('.', weights_configs['file_digest'], key_filename)
                if not os.path.exists(_weight_file_path):
                    _weight_file_path = os.path.join(root, weights_configs['file_digest'], key_filename)
                if not os.path.exists(_weight_file_path):
                    _weight_file_path = os.path.join(weights_configs['file_digest'], key_filename)

        if os.path.isfile(_weight_file_path):
            return _weight_file_path
        else:
            raise ValueError("Can't get weights file from the volume by key: {} or in the static folder: {}".format(key_filename, _weight_file_path))

    def _create_data_loader(self, image_paths: container.DataFrame, image_labels: container.DataFrame) -> Type[ImageDataLoaders]:
        path = self._get_images_path(image_paths)
        temp_fname = image_paths.values.flatten()
        path_str = str(path) + "/"
        fnames = [path_str + s for s in temp_fname]
        labels = image_labels.values.flatten()
        batch_transforms = [Rotate(), Flip(), Dihedral(), Normalize.from_stats(*imagenet_stats)]
        return ImageDataLoaders.from_lists(
            path,
            fnames, labels,
            train='.', bs=self.hyperparams['bs'],
            num_workers=self.hyperparams['num_workers'], valid_pct=self.hyperparams['valid_pct'],
            item_tfms=Resize(224),
            batch_tfms=batch_transforms)

    def _create_learner(self) -> None:
        pt_model = None
        load_torch_dict = True
        weights_path = os.path.split(self._model_path)[0] + "/" + self.hyperparams['model'] + "_fastai.pth"

        if self.hyperparams['model'] == 'resnet18':
            pt_model = resnet18
        elif self.hyperparams['model'] == 'resnet50':
            pt_model = resnet50
        elif self.hyperparams['model'] == 'densenet201':
            pt_model = densenet201
        elif self.hyperparams['model'] == 'efficientnetb0':
            pt_model = EfficientNet.from_pretrained('efficientnet-b0', weights_path)
            load_torch_dict = False

        if load_torch_dict:
            self._learner = cnn_learner(
                dls=self._image_loader,
                arch=pt_model,
                pretrained=False,
                metrics=_METRICS[self.hyperparams['metrics']],
                model_dir=os.getcwd(),
                normalize=self.hyperparams['norm'],
                opt_func=_OPT_FUNCTIONS[self.hyperparams['opt_fn']],
                #loss_func=_LOSS_FUNCTIONS[self.hyperparams['loss_fn']],
            )

            if (self.hyperparams['pretrained']):
                new_state_dict = torch.load(weights_path)
                learn_state_dict = self._learner.model.state_dict()
                for name, param in learn_state_dict.items():
                    if name in new_state_dict['model']:
                        input_param = new_state_dict['model'][name]
                        if input_param.shape == param.shape:
                            param.copy_(input_param)
                        else:
                            print('Shape mismatch at:', name, 'skipping')
                    else:
                        print(f'{name} weight of the model not in pretrained weights')
                self._learner.model.load_state_dict(learn_state_dict)

        else:
            self._learner = Learner(
                dls=self._image_loader,
                model=pt_model,
                metrics=[_METRICS[self.hyperparams['metrics']]],
                opt_func=_OPT_FUNCTIONS[self.hyperparams['opt_fn']],
                model_dir=os.getcwd(),
            )

    def _find_appropriate_lr(self, model: Learner, lr_diff: int = 15, loss_threshold: float = .05, adjust_value: float = 1, plot: bool = False) -> float:
        # Run the Learning Rate Finder
        model.lr_find()

        # Get loss values and their corresponding gradients, and get lr values
        losses = np.array(model.recorder.losses)
        assert(lr_diff < len(losses))
        loss_grad = np.gradient(losses)
        lrs = model.recorder.lrs

        # Search for index in gradients where loss is lowest before the loss spike
        # Initialize right and left idx using the lr_diff as a spacing unit
        # Set the local min lr as -1 to signify if threshold is too low
        r_idx = -1
        l_idx = r_idx - lr_diff
        local_min_lr = None
        while (l_idx >= -len(losses)) and (abs(loss_grad[r_idx] - loss_grad[l_idx]) > loss_threshold):
            local_min_lr = lrs[l_idx]
            r_idx -= 1
            l_idx -= 1
        lr_to_use = local_min_lr * adjust_value
        return lr_to_use

    def fit(self, *, timeout: float = None, iterations: int = None) -> CallResult[None]:
        if self._inputs is None or self._outputs is None:
            raise ValueError("Missing training data.")
        if not self._new_training_data:
            return CallResult(None)
        self._new_training_data = False
        self._training_inputs, self._training_indices = self._get_columns_to_fit(self._inputs, self.hyperparams)
        self._training_outputs, self._target_names, self._target_column_indices = self._get_targets(self._outputs, self.hyperparams)
        self._input_column_names = self._training_inputs.columns.astype(str)
        if len(self._training_indices) > 0 and len(self._target_column_indices) > 0:
            self._target_columns_metadata = self._get_target_columns_metadata(self._training_outputs.metadata, self.hyperparams)
            tl_training_output = self._training_outputs.values

            shape = tl_training_output.shape
            if len(shape) == 2 and shape[1] == 1:
                tl_training_output = np.ravel(tl_training_output)

            assert self._training_inputs is not None
            self._image_loader = self._create_data_loader(self._training_inputs, self._training_outputs)
            self._create_learner()
            assert self._learner is not None
            lr = self._find_appropriate_lr(self._learner)
            self._learner.fine_tune(self.hyperparams['epochs'], lr)
            self._is_fit = True
        else:
            if self.hyperparams['error_on_no_input']:
                raise RuntimeError("No input columns were selected")
            self.logger.warn("No input columns were selected")

        return CallResult(None)

    def produce(self, *, inputs: container.DataFrame, timeout: float = None, iterations: int = None) -> CallResult[Outputs]:

        output = container.DataFrame()

        tl_inputs, columns_to_use = self._get_columns_to_fit(inputs, self.hyperparams)

        if len(tl_inputs.columns):
            tl_output: List[Any] = []

            path = str(self._get_images_path(tl_inputs))
            temp_fname = tl_inputs.values.flatten()
            path_str = str(path) + "/"
            fnames = [path_str + s for s in temp_fname]
            test_dl = self._learner.dls.test_dl(fnames)

            try:
                probabilities, targets, decoded_results = self._learner.get_preds(dl=test_dl, with_decoded=True)
            except AttributeError as error:
                raise PrimitiveNotFittedError("Primitive not fitted.") from error

            tl_output = [self._learner.dls.vocab[i] for i in decoded_results.tolist()]

            assert self._learner is not None
            if not self._is_fit:
                raise ValueError("Primitive has not been fitted")
            output = self._wrap_predictions(inputs, tl_output)
            output.columns = self._target_names
        else:
            if self.hyperparams['error_on_no_input']:
                raise RuntimeError("No input columns were selected")
            self.logger.warn("No input columns were selected")

        outputs = base_utils.combine_columns(
            return_result=self.hyperparams['return_result'],
            add_index_columns=self.hyperparams['add_index_columns'],
            inputs=inputs, column_indices=self._target_column_indices,
            columns_list=[output]
        )

        return CallResult(outputs)

    def get_params(self) -> Params:
        if not self._is_fit:
            return Params(
                learner_=None,
                input_column_names=self._input_column_names,
                training_indices_=self._training_indices,
                target_names_=self._target_names,
                target_column_indices_=self._target_column_indices,
                target_columns_metadata_=self._target_columns_metadata
                )

        return Params(
            learner_=self._learner,
            input_column_names=self._input_column_names,
            training_indices_=self._training_indices,
            target_names_=self._target_names,
            target_column_indices_=self._target_column_indices,
            target_columns_metadata_=self._target_columns_metadata
            )

    def set_params(self, *, params: Params) -> None:
        self._learner = params['learner_']
        self._input_column_names = params['input_column_names']
        self._training_indices = params['training_indices_']
        self._target_names = params['target_names_']
        self._target_column_indices = params['target_column_indices_']
        self._target_columns_metadata = params['target_columns_metadata_']

        if params['learner_'] is not None:
            self._is_fit = True

        return

    @classmethod
    def _get_columns_to_fit(cls, inputs: container.DataFrame, hyperparams: Hyperparams) -> Tuple[container.DataFrame, List[int]]:
        if not hyperparams['use_semantic_types']:
            return inputs, list(range(len(inputs.columns)))

        inputs_metadata = inputs.metadata

        def can_produce_column(column_index: int) -> bool:
            return cls._can_produce_column(inputs_metadata, column_index, hyperparams)

        columns_to_produce: List[Any] = []

        columns_to_produce, columns_not_to_produce = base_utils.get_columns_to_use(
            inputs_metadata,
            use_columns=hyperparams['use_inputs_columns'],
            exclude_columns=hyperparams['exclude_inputs_columns'],
            can_use_column=can_produce_column
        )
        return inputs.iloc[:, columns_to_produce], columns_to_produce
        # return columns_to_produce

    @classmethod
    def _can_produce_column(cls, inputs_metadata: metadata_base.DataMetadata, column_index: int, hyperparams: Hyperparams) -> bool:
        column_metadata = inputs_metadata.query((metadata_base.ALL_ELEMENTS, column_index))

        accepted_structural_types = (int, str, np.integer)
        accepted_semantic_types = set()
        accepted_semantic_types.add("https://metadata.datadrivendiscovery.org/types/Attribute")
        if not issubclass(column_metadata['structural_type'], accepted_structural_types):
            return False

        semantic_types = set(column_metadata.get('semantic_types', []))

        if len(semantic_types) == 0:
            cls.logger.warning("No semantic types found in column metadata")
            return False
        # Making sure all accepted_semantic_types are available in semantic_types
        if len(accepted_semantic_types - semantic_types) == 0:
            return True

        return False

    @classmethod
    def _get_targets(cls, data: container.DataFrame, hyperparams: Hyperparams) -> Tuple[container.DataFrame, list, Any]:
        if not hyperparams['use_semantic_types']:
            return data, list(data.columns), list(range(len(data.columns)))
        metadata = data.metadata

        def can_produce_column(column_index: int) -> bool:
            accepted_semantic_types = set()
            accepted_semantic_types.add("https://metadata.datadrivendiscovery.org/types/TrueTarget")
            column_metadata = metadata.query((metadata_base.ALL_ELEMENTS, column_index))
            semantic_types = set(column_metadata.get('semantic_types', []))
            if len(semantic_types) == 0:
                cls.logger.warning("No semantic types found in column metadata")
                return False
            # Making sure all accepted_semantic_types are available in semantic_types
            if len(accepted_semantic_types - semantic_types) == 0:
                return True
            return False

        target_column_indices, target_columns_not_to_produce = base_utils.get_columns_to_use(
            metadata,
            use_columns=hyperparams['use_outputs_columns'],
            exclude_columns=hyperparams['exclude_outputs_columns'],
            can_use_column=can_produce_column
        )
        targets: container.DataFrame = container.DataFrame()
        if target_column_indices:
            targets = data.select_columns(target_column_indices)
        target_column_names = []
        for idx in target_column_indices:
            target_column_names.append(data.columns[idx])
        return targets, target_column_names, target_column_indices

    @classmethod
    def _get_target_columns_metadata(cls, outputs_metadata: metadata_base.DataMetadata, hyperparams: Hyperparams) -> List[OrderedDict]:
        outputs_length = outputs_metadata.query((metadata_base.ALL_ELEMENTS,))['dimension']['length']

        target_columns_metadata: List[OrderedDict] = []
        for column_index in range(outputs_length):
            column_metadata = OrderedDict(outputs_metadata.query_column(column_index))

            # Update semantic types and prepare it for predicted targets.
            semantic_types = set(column_metadata.get('semantic_types', []))
            semantic_types_to_remove = set(["https://metadata.datadrivendiscovery.org/types/TrueTarget", "https://metadata.datadrivendiscovery.org/types/SuggestedTarget"])
            add_semantic_types = set(["https://metadata.datadrivendiscovery.org/types/PredictedTarget"])
            add_semantic_types.add(hyperparams["return_semantic_type"])
            semantic_types = semantic_types - semantic_types_to_remove
            semantic_types = semantic_types.union(add_semantic_types)
            column_metadata['semantic_types'] = list(semantic_types)

            target_columns_metadata.append(column_metadata)

        return target_columns_metadata

    @classmethod
    def _update_predictions_metadata(cls, inputs_metadata: metadata_base.DataMetadata, outputs: container.DataFrame,
                                     target_columns_metadata: List[OrderedDict]) -> metadata_base.DataMetadata:
        outputs_metadata = metadata_base.DataMetadata().generate(value=outputs)

        for column_index, column_metadata in enumerate(target_columns_metadata):
            column_metadata.pop("structural_type", None)
            outputs_metadata = outputs_metadata.update_column(column_index, column_metadata)

        return outputs_metadata

    def _wrap_predictions(self, inputs: container.DataFrame, predictions: np.ndarray) -> container.DataFrame:
        outputs = container.DataFrame(predictions, generate_metadata=False)
        outputs.metadata = self._update_predictions_metadata(inputs.metadata, outputs, self._target_columns_metadata)
        return outputs
