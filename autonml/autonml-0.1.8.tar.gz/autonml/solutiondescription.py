
# File: solutiondescription.py 
# Author(s): Saswati Ray
# Created: Wed Feb 17 06:44:20 EST 2021 
# Description:
# Acknowledgements:
# Copyright (c) 2021 Carnegie Mellon University
# This code is subject to the license terms contained in the code repo.

import pandas as pd
import uuid, copy, math
import time, random
import numpy as np
import json
from d3m.metadata.pipeline import Pipeline, PrimitiveStep, SubpipelineStep
from d3m.metadata.base import PrimitiveFamily, Context, ArgumentType
from d3m.metadata import base as metadata_base
from d3m.primitive_interfaces.base import PrimitiveBaseMeta
from d3m.runtime import Runtime
from d3m import container
import d3m.index

import networkx as nx

import logging, typing, os 
from timeit import default_timer as timer

# AutonML imports
from autonml.helper_functions import StepType as StepType
from autonml.helper_functions import ActionType as ActionType
from autonml.helper_functions import get_argument as get_argument
from autonml.helper_functions import get_pipeline_values as get_pipeline_values
from autonml.helper_functions import get_values as get_values
from autonml.helper_functions import get_split_indices, get_num_splits
import autonml.solution_templates as solution_templates 
import autonml.default_hyperparams as default_hyperparams
import autonml.helper_functions as helper_functions
import autonml.problem_pb2 as problem_pb2
import autonml.pipeline_pb2 as pipeline_pb2 
import autonml.primitive_pb2 as primitive_pb2
import autonml.value_pb2 as value_pb2

class SolutionDescription(object):
    """
    Represents a solution or pipeline in the D3M environment.
    The idea is that this can be evaluated, fit, produce a model and performance metrics.
    """
    def __init__(self, problem):
        self.id = str(uuid.uuid4())
        self.source = None
        self.created = helper_functions.compute_timestamp()
        self.context = 'PRETRAINING'
        self.name = None
        self.description = None
        self.users = None
        self.inputs = []
        self.rank = 1
        
        self.problem = problem
        self.outputs = None
        self.execution_order = None
        self.primitives_arguments = None
        self.primitives = None
        self.subpipelines = None
        self.pipeline = None
        self.produce_order = None
        self.hyperparams = None
        self.steptypes = None
        self.taskname = None
        self.exclude_columns = None
        self.primitives_outputs = None
        self.cross_outputs = None
        self.pipeline_description = None
        self.total_cols = 0
        self.categorical_atts = None
        self.ordinal_atts = None
        self.ok_to_denormalize = True
        self.add_floats = None
        self.privileged = None
        self.index_denormalize = 0
        self.pipeline_description = None
        self.splitter = False
        self.volumes_dir = os.environ['D3MSTATICDIR']

    def set_categorical_atts(self, atts):
        self.categorical_atts = atts

    def set_ordinal_atts(self, atts):
        self.ordinal_atts = atts

    def set_denormalize(self, ok_to_denormalize):
        self.ok_to_denormalize = ok_to_denormalize

    def set_privileged(self, privileged):
        self.privileged = privileged

    def set_add_floats(self, add_floats):
        self.add_floats = add_floats

    def add_splitter(self):
        self.splitter = True

    def contains_placeholder(self):
        if self.steptypes is None:
            return False

        for step in self.steptypes:
            if step == StepType.PLACEHOLDER:
                return True
        return False

    def num_steps(self):
        """
        Returns number of steps in the pipeline.
        """
        if self.primitives_arguments is not None:
            return len(self.primitives_arguments)
        else:
            return 0

    def find_primitive_index(self, path):
        """
        Returns index of particular primitive in the pipeline
        """
        index = 0
        for id,p in self.primitives.items():
            python_path = p.metadata.query()['python_path'] 
            if path == python_path:
                return index
            index = index + 1

    def create_pipeline_json(self, prim_dict, solution_dict):
        """
        Generate pipeline.json
        """
        name = "Pipeline for evaluation"
        pipeline_id = self.id 
        pipeline_description = Pipeline(pipeline_id=pipeline_id, name=name)
        for ip in self.inputs:
            pipeline_description.add_input(name=ip['name'])

        num = self.num_steps()
 
        # Iterate through different steps in the pipeline
        for i in range(num):
            if self.steptypes[i] == StepType.PRIMITIVE: # PRIMITIVE
                p = prim_dict[self.primitives[i]]
                pdesc = {}
                pdesc['id'] = p.id
                pdesc['version'] = p.primitive_class.version
                pdesc['python_path'] = p.primitive_class.python_path
                pdesc['name'] = p.primitive_class.name
                pdesc['digest'] = p.primitive_class.digest
                step = PrimitiveStep(primitive_description=pdesc)

                # Primitives with multiple produce methods being used in the pipeline
                if 'DistilSingleGraphLoader' in p.primitive_class.python_path or \
                   'DistilGraphLoader' in p.primitive_class.python_path or \
                   'DistilEdgeListLoader' in p.primitive_class.python_path or \
                   'DistilAudioDatasetLoader' in p.primitive_class.python_path:
                    for op in p.primitive_class.produce_methods:
                        step.add_output(output_id=op)
                elif 'extra_trees' in p.primitive_class.python_path or \
                     'random_forest' in p.primitive_class.python_path or \
                     'gradient_boosting' in p.primitive_class.python_path or \
                     'ada_boost' in p.primitive_class.python_path:
                     #'xgboost_gbtree' in p.primitive_class.python_path:
                    for op in p.primitive_class.produce_methods:
                        step.add_output(output_id=op)
                else: # Single produce methods
                    if len(self.primitives_arguments[i]) > 0:
                        step.add_output(output_id=p.primitive_class.produce_methods[0])
                for name, value in self.primitives_arguments[i].items():
                    origin = value['origin']
                    argument_type = ArgumentType.CONTAINER
                    step.add_argument(name=name, argument_type=argument_type, data_reference=value['data'])
                if self.hyperparams[i] is not None:
                    for name, value in self.hyperparams[i].items():
                        if name == "primitive" or name == "primitive_learner":
                            step.add_hyperparameter(name=name, argument_type=ArgumentType.PRIMITIVE, data=value) 
                        else:
                            step.add_hyperparameter(name=name, argument_type=ArgumentType.VALUE, data=value)
            else: # SUBPIPELINE
                solution = solution_dict[self.subpipelines[i]]
                pdesc = solution.pipeline_description
                if pdesc is None:
                    solution.create_pipeline_json(prim_dict, solution_dict)
                    pdesc = solution.pipeline_description 
                step = SubpipelineStep(pipeline=pdesc)
                ipname = 'steps.' + str(i-1) + '.produce'
                step.add_input(ipname)
                for output in solution.outputs:
                    step.add_output(output_id=output[2])

            pipeline_description.add_step(step)

        for op in self.outputs:
            pipeline_description.add_output(data_reference=op[2], name=op[3])

        self.pipeline_description = pipeline_description
   
    def write_pipeline_json(self, prim_dict, solution_dict, dirName, subpipeline_dirName, rank=None, train_score=None):
        """
        Output pipeline to JSON file
        """
        filename = dirName + "/" + self.id + ".json"
        if self.pipeline_description is None:
            self.create_pipeline_json(prim_dict, solution_dict)
            for step in self.pipeline_description.steps:
                if isinstance(step, SubpipelineStep):
                    subfilename = subpipeline_dirName + "/" + step.pipeline.id + ".json"
                    with open(subfilename, "w") as out:
                        parsed = json.loads(step.pipeline.to_json())
                        json.dump(parsed, out, indent=4)

        with open(filename, "w") as out:
            parsed = json.loads(self.pipeline_description.to_json())
            if rank is not None:
                parsed['pipeline_rank'] = str(rank)
            if rank is not None:
                parsed['pipeline_score'] = train_score
            json.dump(parsed, out, indent=4)    

    def write_pipeline_run(self, problem_description, dataset, filename_yaml): 
        runtime = Runtime(pipeline=self.pipeline_description, problem_description=problem_description, context=Context.TESTING, is_standard_pipeline=True)
        output = runtime.fit(inputs=dataset)
        pipeline_run = output.pipeline_run
        with open(filename_yaml, "w") as out:
            pipeline_run.to_yaml(file=filename_yaml)

    def create_from_pipelinedescription(self, solution_dict, pipeline_description: pipeline_pb2.PipelineDescription) -> None:
        """
        Initialize a solution object from a pipeline_pb2.PipelineDescription object passed by TA3.
        """
        n_steps = len(pipeline_description.steps)

        logging.critical("Steps = %d", n_steps)
        logging.critical("Running %s", pipeline_description)
       
        self.inputs = []
        for ip in pipeline_description.inputs:
             self.inputs.append({"name": ip.name})

        self.id = pipeline_description.id
        self.source = {}
        self.source['name'] = pipeline_description.source.name
        self.source['contact'] = pipeline_description.source.contact
        self.source['pipelines'] = []
        for id in pipeline_description.source.pipelines:
            self.source['pipelines'].append(id)

        self.name = pipeline_description.name
        self.description = pipeline_description.description
        self.users = []
        for user in pipeline_description.users:
            self.users.append({"id": user.id, "reason": user.reason, "rationale": user.rationale})

        self.subpipelines = {}
        self.primitives_arguments = {}
        self.primitives = {}
        self.hyperparams = {}
        self.steptypes = []
        for i in range(0, n_steps):
            self.primitives_arguments[i] = {}
            self.hyperparams[i] = None

        self.execution_order = None

        self.pipeline = [None] * n_steps
        self.outputs = []

        # Constructing DAG to determine the execution order
        execution_graph = nx.DiGraph()
        for i in range(0, n_steps):
            # PrimitivePipelineDescriptionStep
            if pipeline_description.steps[i].HasField("primitive") == True:
                s = pipeline_description.steps[i].primitive
                python_path = s.primitive.python_path
                prim = d3m.index.get_primitive(python_path)
                self.primitives[i] = prim
                self.subpipelines[i] = None
                arguments = s.arguments
                self.steptypes.append(StepType.PRIMITIVE)

                for name,argument in arguments.items():
                    if argument.HasField("container") == True:
                        data = argument.container.data
                    else:
                        data = argument.data.data
                    origin = data.split('.')[0]
                    source = data.split('.')[1]
                    self.primitives_arguments[i][name] = {'origin': origin, 'source': int(source), 'data': data}
                    
                    if origin == 'steps':
                        execution_graph.add_edge(str(source), str(i))
                    else:
                        execution_graph.add_edge(origin, str(i))

                hyperparams = s.hyperparams
                if hyperparams is not None:
                    self.hyperparams[i] = {}
                    for name,argument in hyperparams.items():
                        value = None
                        if argument.HasField("value") == True:
                            arg = argument.value.data.raw
                            value = get_values(arg)
                            self.hyperparams[i][name] = value
                        elif argument.HasField("primitive") == True:
                            arg = int(argument.primitive.data)
                            self.hyperparams[i][name] = arg 

            # SubpipelinePipelineDescriptionStep
            elif pipeline_description.steps[i].HasField("pipeline") == True:
                s = pipeline_description.steps[i].pipeline
                self.primitives[i] = None
                self.subpipelines[i] = s.pipeline.id
                self.steptypes.append(StepType.SUBPIPELINE)
                for j in range(len(s.inputs)):
                    argument_edge = s.inputs[j].data
                    origin = argument_edge.split('.')[0]
                    source = argument_edge.split('.')[1]
                    self.primitives_arguments[i]['inputs'] = {'origin': origin, 'source': int(source), 'data': argument_edge}

                    if origin == 'steps':
                        execution_graph.add_edge(str(source), str(i))
                    else:
                        execution_graph.add_edge(origin, str(i))

            else: # PlaceholderPipelineDescriptionStep
                s = pipeline_description.steps[i].placeholder
                self.steptypes.append(StepType.PLACEHOLDER)
                self.primitives[i] = None
                self.subpipelines[i] = None
                for j in range(len(s.inputs)):
                    argument_edge = s.inputs[j].data
                    origin = argument_edge.split('.')[0]
                    source = argument_edge.split('.')[1]
                    self.primitives_arguments[i]['inputs'] = {'origin': origin, 'source': int(source), 'data': argument_edge}

                    if origin == 'steps':
                        execution_graph.add_edge(str(source), str(i))
                    else:
                        execution_graph.add_edge(origin, str(i))
            
        execution_order = list(nx.topological_sort(execution_graph))

        # Removing non-step inputs from the order
        execution_order = list(filter(lambda x: x.isdigit(), execution_order))
        self.execution_order = [int(x) for x in execution_order]

        # Creating set of steps to be call in produce
        self.produce_order = set()
        for i in range(len(pipeline_description.outputs)):
            output = pipeline_description.outputs[i]
            origin = output.data.split('.')[0]
            source = output.data.split('.')[1]
            self.outputs.append((origin, int(source), output.data, output.name))

            if origin != 'steps':
                continue
            else:
                current_step = int(source)
                self.produce_order.add(current_step)
                for i in range(0, len(execution_order)):
                    step_origin = self.primitives_arguments[current_step]['inputs']['origin']
                    step_source = self.primitives_arguments[current_step]['inputs']['source']
                    if step_origin != 'steps':
                        break
                    else:
                        self.produce_order.add(step_source)
                        current_step = step_source
        logging.info("Outputs = %s", self.outputs)

    def isDataFrameStep(self, n_step):
        if self.steptypes[n_step] is StepType.PRIMITIVE and \
        ('profiler' in self.primitives[n_step].metadata.query()['python_path']):
            return True
        return False

    def remove_one_hot_encoder(self):
        #For very high-dim datasets, replace one hot encoder primitive with "nothing".
        num = len(self.primitives)
        # Iterate through steps of the pipeline 
        for i in range(num):     
            p = self.primitives[i]
            python_path = p.metadata.query()['python_path'] 
            if 'one_hot_' in python_path:
                prim = d3m.index.get_primitive('d3m.primitives.data_transformation.do_nothing.DSBOX')
                self.primitives[i] = prim
                self.hyperparams[i] = None
                break

    def exclude(self, df):
        """
        Exclude columns which cannot/need not be processed.
        """
        self.exclude_columns = set()
        metadata = df.metadata
        rows = len(df)
        attributes = metadata.get_columns_with_semantic_type("https://metadata.datadrivendiscovery.org/types/Attribute")

        # Ignore all column that have only one value
        for att in attributes:
            attmeta = metadata.query((metadata_base.ALL_ELEMENTS, att))['semantic_types']
            length = len(attmeta)-1
            if 'https://metadata.datadrivendiscovery.org/types/UniqueKey' in attmeta:
                length = length - 1
                if length == 0:
                    self.exclude_columns.add(int(att))
                    continue
            col = int(att)

            # Remove constant attributes
            if len(df.iloc[:, col].unique()) <= 1:
                self.exclude_columns.add(col)

        cols = metadata.get_columns_with_semantic_type("https://metadata.datadrivendiscovery.org/types/FloatVector") # Found to be very expensive in ColumnParser!
        for col in cols:
            self.exclude_columns.add(col)

        if rows > 100000 and (len(attributes) - len(self.exclude_columns) > 50):
            random.seed(1979)
            remove = random.sample(attributes, len(attributes) - len(self.exclude_columns) - 50)
            self.exclude_columns.update(remove)
            self.remove_one_hot_encoder()
        if rows > 1000000 and (len(attributes) - len(self.exclude_columns) > 5):
            random.seed(1979)
            remove = random.sample(attributes, len(attributes) - len(self.exclude_columns) - 5)
            self.exclude_columns.update(remove)
            self.remove_one_hot_encoder() 
        if len(attributes) - len(self.exclude_columns) >= 10000:
            remove = random.sample(attributes, len(attributes) - len(self.exclude_columns) - 10000)
            self.exclude_columns.update(remove)
            self.remove_one_hot_encoder()

        targets = metadata.get_columns_with_semantic_type("https://metadata.datadrivendiscovery.org/types/TrueTarget")
        for t in targets:
            if t in self.exclude_columns:
                self.exclude_columns.remove(t)

    def produce_feature_importances(self, prefix):
        """
        Produce feature_importances
        """
        try:
            n_step = self.num_steps()-2
            model = self.pipeline[n_step]   
            step_name = "step."+str(n_step)+".produce_feature_importances"
            if prefix is not None:
                step_name = prefix + step_name
            values = model.produce_feature_importances().value
            return (step_name, values)   
        except:
            return (None, None)        

    def fit(self, **arguments):
        """
        Train all steps in the solution.

        Paramters
        ---------
        arguments
            Arguments required to train the solution
        """
        primitives_outputs = [None] * len(self.primitives) 
   
        if self.primitives_outputs is None: 
            for i in range(0, len(self.execution_order)):
                n_step = self.execution_order[i]
                primitives_outputs[n_step] = self.process_step(n_step, primitives_outputs, ActionType.FIT, arguments)
                if self.isDataFrameStep(n_step) == True:
                    self.exclude(primitives_outputs[n_step])
        else:
            last_step = self.get_last_step()
            primitives_outputs[last_step] = self.process_step(last_step, self.primitives_outputs, ActionType.FIT, arguments)
            i = 0
            for op in self.primitives_outputs:
                primitives_outputs[i] = op
                i = i + 1
            if last_step < len(self.execution_order) - 1:
                for i in range(last_step+1, len(self.execution_order)):
                     n_step = self.execution_order[i]
                     primitives_outputs[n_step] = self.process_step(n_step, primitives_outputs, ActionType.FIT, arguments)
            
        v = primitives_outputs[self.execution_order[len(self.execution_order)-1]]
        return v

    def _pipeline_step_fit(self, n_step: int, pipeline_id: str, primitive_arguments, arguments, action):
        """
        Execute a subpipeline step
        
        Paramters
        ---------
        n_step: int
            An integer of the actual step.
        pipeline_id: str
            
        primitive_arguments
            Arguments for the solution
        """
        solution = arguments['solution_dict'][pipeline_id]

        inputs = []
        inputs.append(primitive_arguments['inputs'])

        if action is ActionType.FIT: 
            return solution.fit(inputs=inputs, solution_dict=arguments['solution_dict'])
        elif action is ActionType.SCORE:
            return solution.score_solution(inputs=inputs, solution_dict=arguments['solution_dict'], primitive_dict=arguments['primitive_dict'],
                   posLabel=arguments['posLabel'], metric=arguments['metric'])
        else:
            return 

    def cross_validate_step(self, n_step, primitive: PrimitiveBaseMeta, primitive_arguments):
        # Build hyperparameters for the primitive
        custom_hyperparams = dict()
        hyperparams = self.hyperparams[n_step]
        if hyperparams is not None:
            for hyperparam, value in hyperparams.items():
                custom_hyperparams[hyperparam] = value

        training_arguments_primitive = self._primitive_arguments(primitive, 'set_training_data')
        training_arguments = {}

        for param, value in primitive_arguments.items():
            if param in training_arguments_primitive:
                training_arguments[param] = value

        # Instantiate the primitive (model)
        primitive_hyperparams = primitive.metadata.query()['primitive_code']['class_type_arguments']['Hyperparams']
        prim_instance = primitive(hyperparams=primitive_hyperparams(primitive_hyperparams.defaults(), **custom_hyperparams))

        X, y = None, None
        y = training_arguments['outputs']
        X = training_arguments['inputs']

        task = "classification"
        if self.taskname != "classification":
            task = "regression"
        splits = get_num_splits(len(X), len(X.columns))
        split_indices = get_split_indices(X, y, splits, task)

        hyperparams = {}
        hyperparams['max_one_hot'] = 100
        prim = d3m.index.get_primitive('d3m.primitives.data_cleaning.robust_scaler.SKlearn')
        primitive_hyperparams = prim.metadata.query()['primitive_code']['class_type_arguments']['Hyperparams']
        scaler = prim(hyperparams=primitive_hyperparams.defaults())
        prim = d3m.index.get_primitive('d3m.primitives.data_transformation.to_numeric.DSBOX')
        primitive_hyperparams = prim.metadata.query()['primitive_code']['class_type_arguments']['Hyperparams']
        numeric = prim(hyperparams=primitive_hyperparams.defaults())

        train_predictions, test_predictions = [], []
        trainY, testY = [], []
        # Do the actual k-fold CV here
        for train_index, test_index in split_indices:
            X_train, X_test = X.iloc[train_index,:], X.iloc[test_index,:]
            y_train, y_test = y.iloc[train_index,:], y.iloc[test_index,:]

            X_test.reset_index(drop=True,inplace=True)
            X_train.reset_index(drop=True,inplace=True)
            prim_instance.set_training_data(inputs=X_train, outputs=y_train)
            prim_instance.fit()
            train = prim_instance.produce(inputs=X_train).value
            (cols, ordinals, add_floats) = helper_functions.get_cols_to_encode(train)
            hyperparams['use_columns'] = list(cols)
            prim = d3m.index.get_primitive('d3m.primitives.data_transformation.one_hot_encoder.DistilOneHotEncoder')
            primitive_hyperparams = prim.metadata.query()['primitive_code']['class_type_arguments']['Hyperparams']
            ohe_prim = prim(hyperparams=primitive_hyperparams(primitive_hyperparams.defaults(), **hyperparams))
            ohe_prim.set_training_data(inputs=train)
            ohe_prim.fit()
            train = ohe_prim.produce(inputs=train).value
            train = numeric.produce(inputs=train).value
            scaler.set_training_data(inputs=train)
            scaler.fit()
            train = scaler.produce(inputs=train).value

            test = prim_instance.produce(inputs=X_test).value
            test = ohe_prim.produce(inputs=test).value
            test = numeric.produce(inputs=test).value
            test = scaler.produce(inputs=test).value
            train_predictions.append(train)
            test_predictions.append(test)
            trainY.append(y_train)
            testY.append(y_test)

        return [train_predictions, test_predictions, trainY, testY]
 
    def fit_step(self, n_step: int, primitive: PrimitiveBaseMeta, primitive_arguments):
        """
        Execute a primitive step

        Paramters
        ---------
        n_step: int
            An integer of the actual step.
        primitive: PrimitiveBaseMeta
            A primitive class
        primitive_arguments
            Arguments for set_training_data, fit, produce of the primitive for this step.
        """
        model = self.pipeline[n_step]
        produce_params_primitive = self._primitive_arguments(primitive, 'produce')
        produce_params = {}

        for param, value in primitive_arguments.items():
            if param in produce_params_primitive:
                produce_params[param] = value

        # If model is cached, just use it!
        python_path = primitive.metadata.query()['python_path']
        if model is not None:  # Use pre-learnt model
            return model.produce(**produce_params).value

        # Build hyperparameters for the primitive
        custom_hyperparams = dict() 
        hyperparams = self.hyperparams[n_step]
        if hyperparams is not None:
            for hyperparam, value in hyperparams.items():
                if hyperparam == 'primitive':
                    val = self.primitives[value]
                    primitive_hyperparams = val.metadata.query()['primitive_code']['class_type_arguments']['Hyperparams']
                    primitive_model = val(hyperparams=primitive_hyperparams(primitive_hyperparams.defaults(), **self.hyperparams[value]))
                    custom_hyperparams[hyperparam] = primitive_model
                    continue
                custom_hyperparams[hyperparam] = value

        training_arguments_primitive = self._primitive_arguments(primitive, 'set_training_data')
        training_arguments = {}

        for param, value in primitive_arguments.items():
            if param in training_arguments_primitive:
                training_arguments[param] = value

        # Instantiate the primitive (model)
        primitive_hyperparams = primitive.metadata.query()['primitive_code']['class_type_arguments']['Hyperparams']
        method_arguments = primitive.metadata.query()['primitive_code'].get('instance_methods', {}).get('__init__', {}).get('arguments', [])
        if 'volumes' in method_arguments:
            primitive_name = str(primitive)
            volumes = helper_functions.get_primitive_volumes(self.volumes_dir, primitive, primitive_name)
            model = primitive(volumes=volumes, hyperparams=primitive_hyperparams(primitive_hyperparams.defaults(), **custom_hyperparams))
        else:
            model = primitive(hyperparams=primitive_hyperparams(primitive_hyperparams.defaults(), **custom_hyperparams))
    
        # Call set_training_data() on Primitive(model)
        model.set_training_data(**training_arguments)

        # Call fit() on Primitive(model)
        model.fit()

        # Reduce memory footprints!
        if 'splitter' in python_path or 'profiler' in python_path:
            model._training_inputs = None
        if 'corex' in python_path:
            model.training_data = None
        if 'tfidf' in python_path or 'robust_scaler' in python_path or 'imputer' in python_path or 'select_percentile' in python_path:
            model._inputs = None
            model._training_inputs = None
        if 'image_transfer' in python_path:
            self.pipeline[n_step] = None

        # Cache the model!
        self.pipeline[n_step] = model

        # Call produce() on Primitive(model)
        final_output = None

        # Some primitives have additional methods being called.
        if 'DistilRaggedDatasetLoader' in python_path or 'DistilAudioDatasetLoader' in python_path:
            final_output = {}
            final_output['produce'] = model.produce(**produce_params).value
            final_output['produce_collection'] = model.produce_collection(**produce_params).value
        elif 'DistilSingleGraphLoader' in python_path or \
             'DistilGraphLoader' in python_path or \
             'DistilEdgeListLoader' in python_path:
            final_output = {}
            final_output['produce'] = model.produce(**produce_params).value
            final_output['produce_target'] = model.produce_target(**produce_params).value
        else: # Most primitives have only "produce" method
            final_output = model.produce(**produce_params).value

        return final_output

    def _primitive_arguments(self, primitive, method: str) -> set:
        """
        Get the arguments of a primitive given a function.

        Parameters
        ---------
        primitive
            A primitive.
        method
            A method of the primitive.
        """
        return set(primitive.metadata.query()['primitive_code']['instance_methods'][method]['arguments'])

    def produce(self, **arguments):
        """
        Run produce on the solution.

        Paramters
        ---------
        arguments
            Arguments required to execute the solution
        """
        steps_outputs = [None] * len(self.primitives)

        # Loop through the pipeline
        for i in range(0, len(self.execution_order)):
            n_step = self.execution_order[i]
            produce_arguments = {}

            # Subpipeline
            if self.steptypes[n_step] is StepType.SUBPIPELINE:
                produce_arguments = {}
                for argument, value in self.primitives_arguments[n_step].items():
                    if value['origin'] == 'steps':
                        produce_arguments[argument] = steps_outputs[value['source']]
                    else:
                        produce_arguments[argument] = arguments['inputs'][value['source']]
                    if produce_arguments[argument] is None:
                        continue

            # Primitive
            if self.steptypes[n_step] is StepType.PRIMITIVE:
                primitive = self.primitives[n_step]
                python_path = primitive.metadata.query()['python_path']
                if self.pipeline[n_step] is None: #if 'resnet50' in python_path or self.pipeline[n_step] is None:
                    primitive_hyperparams = primitive.metadata.query()['primitive_code']['class_type_arguments']['Hyperparams']
                    custom_hyperparams = dict()

                    method_arguments = primitive.metadata.query()['primitive_code'].get('instance_methods', {}).get('__init__', {}).get('arguments', [])
                    if 'volumes' in method_arguments:
                        volumes = get_primitive_volumes(self.volumes_dir, primitive)
                        model = primitive(volumes=volumes, hyperparams=primitive_hyperparams(primitive_hyperparams.defaults(), **custom_hyperparams))
                    else:
                        model = primitive(hyperparams=primitive_hyperparams(primitive_hyperparams.defaults(), **custom_hyperparams))

                    self.pipeline[n_step] = model
                produce_arguments_primitive = self._primitive_arguments(primitive, 'produce')
                for argument, value in self.primitives_arguments[n_step].items():
                    if argument in produce_arguments_primitive:
                        if value['origin'] == 'steps':
                            produce_arguments[argument] = steps_outputs[value['source']]
                        else:
                            produce_arguments[argument] = arguments['inputs'][value['source']]
                        if produce_arguments[argument] is None:
                            continue
            if self.steptypes[n_step] is StepType.PRIMITIVE: # Primitive
                if n_step in self.produce_order:
                    primitive = self.primitives[n_step]
                    v = self.pipeline[n_step].produce(**produce_arguments).value
                    steps_outputs[n_step] = v
                else:
                    steps_outputs[n_step] = None
            else: # Subpipeline
                solution_dict = arguments['solution_dict']
                solution = solution_dict[self.subpipelines[n_step]]
                inputs = []
                inputs.append(produce_arguments['inputs'])
                op = solution.produce(inputs=inputs, solution_dict=solution_dict)
                steps_outputs[n_step] = op[0]

        # Create output
        pipeline_output = []
        for output in self.outputs:
            if output[0] == 'steps':
                pipeline_output.append(steps_outputs[output[1]])
            else:
                pipeline_output.append(arguments[output[0][output[1]]])
        return pipeline_output

    def initialize_RPI_solution(self, taskname):
        """
        Initialize a solution from scratch consisting of predefined steps
        Leave last step for filling in primitive (for classification/regression problems)
        """
        python_paths = copy.deepcopy(solution_templates.task_paths[taskname])

        if 'denormalize' in python_paths[0] and self.ok_to_denormalize == False:
            python_paths.remove('d3m.primitives.data_transformation.denormalize.Common')

        self.taskname = taskname
        self.primitives_arguments = {}
        self.subpipelines = {}
        self.primitives = {}
        self.hyperparams = {}
        self.steptypes = []
        self.pipeline = []
        self.execution_order = None
    
        self.inputs = []
        self.inputs.append({"name": "dataset inputs"})

        # Constructing DAG to determine the execution order
        execution_graph = nx.DiGraph()

        # Setting steps relative to column_parser step
        col_parser_step = 3
        after_step = self.index_denormalize + 3
        if self.add_floats is not None and len(self.add_floats) > 0:
            python_paths.insert(after_step, 'd3m.primitives.data_transformation.add_semantic_types.Common')
            col_parser_step = 4

        num = len(python_paths)
        # Iterate through steps of the pipeline 
        for i in range(num):
            self.add_primitive(python_paths[i], i)

            # Set hyperparameters for specific primitives
            if python_paths[i] == 'd3m.primitives.data_transformation.add_semantic_types.Common':
                self.hyperparams[i] = {}
                exclude_atts = set() 
                if self.ordinal_atts is not None and len(self.ordinal_atts) > 0:
                    exclude_atts.update(list(self.ordinal_atts))
                if self.add_floats is not None and len(self.add_floats) > 0:
                    exclude_atts.update(list(self.add_floats))
                self.hyperparams[i]['columns'] = list(exclude_atts)
                self.hyperparams[i]['semantic_types'] = ['http://schema.org/Float']

            if python_paths[i] == 'd3m.primitives.data_cleaning.imputer.SKlearn':
                self.hyperparams[i] = {}
                self.hyperparams[i]['strategy'] = 'most_frequent'

            # Construct pipelines for different task types
            if i == 0: # denormalize
                data = 'inputs.0'
            elif i == col_parser_step + 1: # extract_columns_by_semantic_types (targets)
                data = 'steps.{}.produce'.format(self.index_denormalize + 2)
                self.hyperparams[i] = {}
                self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
            elif i == col_parser_step + 2: # extract_columns_by_semantic_types
                data = 'steps.{}.produce'.format(col_parser_step)
                self.hyperparams[i] = {}
                self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/Attribute','https://metadata.datadrivendiscovery.org/types/PrimaryKey']
                if self.privileged is not None and len(self.privileged) > 0:
                    self.hyperparams[i]['exclude_columns'] = self.privileged
            elif 'RPI' in python_paths[i]:
                data = 'steps.{}.produce'.format(col_parser_step + 1)
                origin = data.split('.')[0]
                source = data.split('.')[1]
                self.primitives_arguments[i]['outputs'] = {'origin': origin, 'source': int(source), 'data': data}
                execution_graph.add_edge(str(source), str(i))
                data = 'steps.' + str(i - 1) + str('.produce')
            else: # other steps
                data = 'steps.' + str(i - 1) + '.produce'

            origin = data.split('.')[0]
            source = data.split('.')[1]
            self.primitives_arguments[i]['inputs'] = {'origin': origin, 'source': int(source), 'data': data}

            if i == 0:
                execution_graph.add_edge(origin, str(i))
            else:
                execution_graph.add_edge(str(source), str(i))

        execution_order = list(nx.topological_sort(execution_graph))

        # Removing non-step inputs from the order
        execution_order = list(filter(lambda x: x.isdigit(), execution_order))
        self.execution_order = [int(x) for x in execution_order]

    def add_ssl_variant(self, variant):
        """
        Add SSL blackbox model as hyperparameter.
        Should support 'n_estimators' and predict_proba() API.
        """
        if variant == 'd3m.primitives.classification.gradient_boosting.SKlearn':
            from d3m.primitives.classification.gradient_boosting import SKlearn as blackboxParam
        elif variant == 'd3m.primitives.classification.extra_trees.SKlearn':
            from  d3m.primitives.classification.extra_trees import SKlearn as blackboxParam
        elif variant == 'd3m.primitives.classification.random_forest.SKlearn':
            from d3m.primitives.classification.random_forest import SKlearn as blackboxParam
        elif variant == 'd3m.primitives.classification.bagging.SKlearn':
            from d3m.primitives.classification.bagging import SKlearn as blackboxParam
        elif variant == 'd3m.primitives.classification.svc.SKlearn':
            from d3m.primitives.classification.svc import SKlearn as blackboxParam
        elif variant == 'd3m.primitives.classification.linear_svc.SKlearn':
            from d3m.primitives.classification.linear_svc import SKlearn as blackboxParam
 
        numSteps = self.num_steps()
        self.hyperparams[numSteps-2] = {}
        self.hyperparams[numSteps-2]['blackbox'] = blackboxParam

    def get_python_paths(self, taskname, columns, metric):
        """
        In addition to the pipeline template of steps, add extra feature processing steps (OHE/Scaler etc)
        """
        python_paths = copy.deepcopy(solution_templates.task_paths[taskname])

        if self.splitter == True:
            python_paths.insert(0, 'd3m.primitives.data_transformation.splitter.DSBOX')
            self.index_denormalize = 1

        if 'denormalize' in python_paths[self.index_denormalize] and self.ok_to_denormalize == False:
            python_paths.remove('d3m.primitives.data_transformation.denormalize.Common')

        if taskname in ['CLASSIFICATION','REGRESSION','COREXTEXT','IMAGE','IMAGE2','TIMESERIES','DISTILTEXT','TFIDFTEXT','SEMISUPERVISED']:
            if self.splitter == False and self.categorical_atts is not None and len(self.categorical_atts) > 0:
                #python_paths.append('d3m.primitives.data_transformation.one_hot_encoder.SKlearn')
                python_paths.append('d3m.primitives.data_transformation.one_hot_encoder.DistilOneHotEncoder')

            python_paths.append('d3m.primitives.data_transformation.to_numeric.DSBOX')
            if taskname not in ['IMAGE','IMAGE2','VIDEO','TFIDFTEXT']:
                # Data frame has too many dimensions (in thousands)! This step is extremely slow! 
                python_paths.append('d3m.primitives.data_cleaning.robust_scaler.SKlearn')

            # ColumnParser.Common is expensive!
            if columns > 2000:  
                python_paths[self.index_denormalize+4] = 'd3m.primitives.data_transformation.column_parser.DistilColumnParser'
                python_paths.append('d3m.primitives.feature_selection.select_percentile.SKlearn')
       
            # Add float semantic type to Unknown attributes 
            after_target_step = self.index_denormalize + 4
            if (self.add_floats is not None and len(self.add_floats) > 0) or (self.ordinal_atts is not None and len(self.ordinal_atts) > 0):
                python_paths.insert(after_target_step, 'd3m.primitives.data_transformation.add_semantic_types.Common')

            if metric is not None and 'ROC_AUC' in metric:
                python_paths.append('d3m.primitives.data_transformation.add_semantic_types.Common')
                python_paths.append('d3m.primitives.data_transformation.horizontal_concat.DataFrameCommon')
                python_paths.append('d3m.primitives.operator.compute_unique_values.Common')
                python_paths.append('d3m.primitives.data_transformation.extract_columns_by_semantic_types.Common')
                python_paths.append('d3m.primitives.data_transformation.extract_columns_by_semantic_types.Common')
            
        return python_paths

    def initialize_solution(self, taskname, columns=10, metric=None):
        """
        Initialize a solution from scratch consisting of predefined steps
        Pipelines constructed from templates specified in solution_templates.py
        Leave last step for filling in primitive (for classification/regression problems)
        """
        self.taskname = taskname
        python_paths = self.get_python_paths(taskname, columns, metric)

        self.primitives_arguments = {}
        self.subpipelines = {}
        self.primitives = {}
        self.hyperparams = {}
        self.steptypes = []
        self.pipeline = []
        self.execution_order = None

        self.inputs = []
        self.inputs.append({"name": "dataset inputs"})

        # Constructing DAG to determine the execution order
        execution_graph = nx.DiGraph()

        num = len(python_paths)

        # Iterate through steps of the pipeline 
        for i in range(num):
            self.add_primitive(python_paths[i], i)

            # Set hyperparameters for specific primitives
            self.hyperparams[i] = default_hyperparams.set_default_hyperparameters(python_paths[i], taskname)
            if 'percentile' in python_paths[i]:
                self.hyperparams[i] = {}
                percent =  int(math.floor(100*100/columns))
                if percent < 1:
                    percent = 1
                self.hyperparams[i]['percentile'] = percent
                if 'REGRESSION' in taskname:
                    self.hyperparams[i]['score_func'] = 'f_regression'

            if python_paths[i] == 'd3m.primitives.data_transformation.add_semantic_types.Common':
                self.hyperparams[i] = {}
                exclude_atts = set()
                if self.ordinal_atts is not None and len(self.ordinal_atts) > 0:
                    exclude_atts.update(list(self.ordinal_atts))
                if self.add_floats is not None and len(self.add_floats) > 0:
                    exclude_atts.update(list(self.add_floats))
                self.hyperparams[i]['columns'] = list(exclude_atts)
                self.hyperparams[i]['semantic_types'] = ['http://schema.org/Float', 'https://metadata.datadrivendiscovery.org/types/Attribute']
                
            if self.privileged is not None and len(self.privileged) > 0 and \
                python_paths[i] == 'd3m.primitives.data_transformation.extract_columns_by_semantic_types.Common':
                self.hyperparams[i] = {}
                self.hyperparams[i]['exclude_columns'] = self.privileged
           
            if 'concat' in python_paths[i]:
                data = 'steps.{}.produce'.format(i-1)
                self.primitives_arguments[i]['left'] = get_argument(data) 
                data = 'steps.{}.produce'.format(self.index_denormalize + 3)
                self.primitives_arguments[i]['right'] = get_argument(data)    
                execution_graph.add_edge(str(i-1), str(i))
                execution_graph.add_edge(str(self.index_denormalize + 3), str(i))

            # Construct pipelines for different task types
            if taskname in ['CLASSIFICATION','REGRESSION','COREXTEXT','IMAGE','IMAGE2','VIDEO','TIMESERIES','DISTILTEXT','TFIDFTEXT','CONDITIONER','FORE_REGRESSION']:
                if i == 0: # denormalize
                    data = 'inputs.0'
                elif i == self.index_denormalize + 3 or (metric is not None and 'ROC_AUC' in metric and i == num-2): # extract_columns_by_semantic_types (targets)
                    data = 'steps.{}.produce'.format(i-1)
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == self.index_denormalize + 4 or (metric is not None and 'ROC_AUC' in metric and i == num-1): # column_parser/time series/add_semantic_types
                    data = 'steps.{}.produce'.format(i-2)
                elif 'DistilTextEncoder' in python_paths[i] or 'select_percentile' in python_paths[i]: # DistilTextEncoder / select_percentile: These need inputs AND outputs!
                    data = 'steps.{}.produce'.format(self.index_denormalize + 3)
                    self.primitives_arguments[i]['outputs'] = get_argument(data)
                    source = self.primitives_arguments[i]['outputs']['source']
                    execution_graph.add_edge(str(source), str(i))
                    data = 'steps.' + str(i - 1) + str('.produce')
                else: # other steps
                    data = 'steps.' + str(i - 1) + '.produce'
            elif taskname == 'TIMESERIES3':
                if i == 0: 
                    data = 'inputs.0'
                else: # other steps
                    data = 'steps.0.produce'
                    self.primitives_arguments[i]['outputs'] = get_argument(data)
                    data = 'steps.' + str(i - 1) + '.produce'

            # Graph problems!
            elif taskname in ['COMMUNITYDETECTION','LINKPREDICTION','VERTEXCLASSIFICATION','VERTEXCLASSIFICATION3','GRAPHMATCHING']:
                if i == 0: 
                    data = 'inputs.0'
                else:
                    data = 'steps.0.produce_target'
                    self.primitives_arguments[i]['outputs'] = get_argument(data)
                    data = 'steps.0.produce'

            # Another graph pipeline
            elif taskname == 'GRAPHMATCHING3':
                if i == 0 or i == 1 or i == 2: # dataset_to_dataframe
                    data = 'inputs.0'
                    if i > 0:
                        self.hyperparams[i] = {}
                        self.hyperparams[i]['dataframe_resource'] = str(i)
                else: #euclidean_nomination.JHU
                    data = 'steps.1.produce'
                    self.primitives_arguments[i]['inputs_1'] = get_argument(data)
                    data = 'steps.2.produce'
                    self.primitives_arguments[i]['inputs_2'] = get_argument(data)
                    data = 'steps.0.produce'
                    self.primitives_arguments[i]['reference'] = get_argument(data)
                    execution_graph.add_edge(str(0), str(i))
                    execution_graph.add_edge(str(1), str(i))
                    execution_graph.add_edge(str(2), str(i))

            # ISI_PIPELINE
            elif taskname == 'ISI_PIPELINE':
                if i == 0:
                    data = 'inputs.0'
                elif i == 2: # extract_columns_by_semantic_types (targets)
                    data = 'steps.{}.produce'.format(i-1)
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == 3: # gcn
                    data = 'steps.2.produce'
                    self.primitives_arguments[i]['outputs'] = get_argument(data)
                    source = self.primitives_arguments[i]['outputs']['source']
                    execution_graph.add_edge(str(source), str(i))
                    data = 'steps.0.produce'

            # Audio
            elif taskname == 'AUDIO':
                if i == 0: # AudioDatasetLoader
                    data = 'inputs.0'
                elif i == self.index_denormalize + 1: # column_parser
                    data = 'steps.{}.produce'.format(self.index_denormalize)
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['parse_semantic_types'] = ["http://schema.org/Boolean", \
                                                                   "http://schema.org/Integer", \
                                                                   "http://schema.org/Float"]
                elif i == self.index_denormalize + 2: # extract_columns_by_semantic_types (targets)
                    data = 'steps.{}.produce'.format(self.index_denormalize + 1)
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == self.index_denormalize + 3: # DistilAudioTransfer
                    data = 'steps.{}.produce_collection'.format(self.index_denormalize)
                else: # other steps
                    data = 'steps.' + str(i-1) + '.produce'

            # Remote-sensing
            elif taskname == 'REMOTESENSING':
                if i == 0: # denormalize
                    data = 'inputs.0'
                elif i == 3: # DistilColumnParser
                    data = 'steps.2.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['parse_semantic_types'] = ["http://schema.org/Integer", \
                                                                   "http://schema.org/Float", \
                                                                   "https://metadata.datadrivendiscovery.org/types/FloatVector"]
                elif i == 4: # extract_columns_by_semantic_types 
                    data = 'steps.3.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ["http://schema.org/ImageObject"]
                elif i == 5: # extract_columns_by_semantic_types (targets)
                    data = 'steps.3.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == 6: # remote_sensing
                    data = 'steps.4.produce'
                else: # other steps
                    data = 'steps.' + str(i-1) + '.produce'

            # Semi-supervised
            elif taskname == 'SEMISUPERVISED' or taskname == 'SEMISUPERVISED_HDB':
                if i == 0: # denormalize
                    data = 'inputs.0'
                elif i == 3: # extract_columns_by_semantic_types (targets)
                    data = 'steps.2.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == 4: # column_parser
                    data = 'steps.2.produce'
                elif 'extract_columns' in python_paths[i]:
                    data = 'steps.' + str(i-1) + '.produce'
                    if self.hyperparams[i] is None:
                        self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/Attribute', \
                                                             'https://metadata.datadrivendiscovery.org/types/PrimaryKey']
                else: # other steps
                    data = 'steps.' + str(i-1) + '.produce'

            # ARIMA
            elif taskname == 'ARIMA_FORECASTING':
                if i == 0: # denormalize
                    data = 'inputs.0'
                elif i == 3: # extract_columns_by_semantic_types (targets)
                    data = 'steps.2.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == 4: # column_parser
                    data = 'steps.2.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['parse_semantic_types'] = ["http://schema.org/Boolean", \
                                                                   "http://schema.org/Integer", \
                                                                   "http://schema.org/Float"]
                elif i == 5: # extract_columns
                    data = 'steps.4.produce'
                    if self.hyperparams[i] is None:
                        self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/Attribute', \
                                                             'https://metadata.datadrivendiscovery.org/types/PrimaryKey', \
                                                             'https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == 6: # arima
                    data = 'steps.3.produce'
                    self.primitives_arguments[i]['outputs'] = get_argument(data)
                    source = self.primitives_arguments[i]['outputs']['source']
                    data = 'steps.' + str(i-1) + '.produce'
                    execution_graph.add_edge(str(source), str(i))
                else: # other steps
                    data = 'steps.' + str(i-1) + '.produce'

            # Other forecasting pipelines!
            elif taskname in ['ESRNN_FORECASTING','NBEATS_FORECASTING','DISTIL_NBEATS']:
                if i == 0: # denormalize
                    data = 'inputs.0'
                elif i == 4: # extract_columns_by_semantic_types (targets)
                    data = 'steps.3.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == 5: # extract_columns
                    data = 'steps.3.produce'
                elif i == 3: # column_parser
                    data = 'steps.' + str(2) + '.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['parse_semantic_types'] = ["http://schema.org/Boolean", \
                                                                   "http://schema.org/Integer", \
                                                                   "http://schema.org/Float", \
                                                                   "https://metadata.datadrivendiscovery.org/types/FloatVector", \
                                                                   "http://schema.org/DateTime"]
                elif 'esrnn' in python_paths[i] or 'nbeats' in python_paths[i] or 'NBEATS' in python_paths[i]: # esrnn / nbeats
                    data = 'steps.4.produce'
                    self.primitives_arguments[i]['outputs'] = get_argument(data)
                    source = self.primitives_arguments[i]['outputs']['source']
                    data = 'steps.' + str(i-1) + '.produce'
                    execution_graph.add_edge(str(source), str(i))
                elif 'construct_predictions' in python_paths[i]: #i == 9:
                    data = 'steps.1.produce'
                    self.primitives_arguments[i]['reference'] = get_argument(data)
                    data = 'steps.' + str(i-1) + '.produce'
                else: # other steps
                    data = 'steps.' + str(i-1) + '.produce'

            # Other forecasting pipelines!
            elif taskname == 'VAR_FORECASTING' or taskname == 'LSTM_FORECASTING':
                if i == 0: # denormalize
                    data = 'inputs.0'
                elif i == 4: # extract_columns_by_semantic_types (targets)
                    data = 'steps.3.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == 3: # column_parser
                    data = 'steps.' + str(2) + '.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['parse_semantic_types'] = ["http://schema.org/Boolean", \
                                                                   "http://schema.org/Integer", \
                                                                   "http://schema.org/Float", \
                                                                   "https://metadata.datadrivendiscovery.org/types/FloatVector", \
                                                                   "http://schema.org/DateTime"]
                elif i == 5: # extract_columns
                    data = 'steps.3.produce'
                    if self.hyperparams[i] is None:
                        self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/Attribute', \
                                                             'https://metadata.datadrivendiscovery.org/types/PrimaryKey']
                elif 'AR' in python_paths[i]: # VAR
                    data = 'steps.' + str(4) + '.produce'
                    self.primitives_arguments[i]['outputs'] = get_argument(data)
                    source = self.primitives_arguments[i]['outputs']['source']
                    execution_graph.add_edge(str(source), str(i))
                    data = 'steps.' + str(i-1) + '.produce'
                else: # other steps
                    data = 'steps.' + str(i-1) + '.produce'

            # Object detection
            elif taskname == 'OBJECTDETECTION':
                if i == 0: # denormalize
                    data = 'inputs.0'
                elif i == 2: # extract_columns_by_semantic_types
                    data = 'steps.1.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/PrimaryMultiKey', \
                                                             'https://metadata.datadrivendiscovery.org/types/FileName']
                elif i == 3: # extract_columns_by_semantic_types (targets)
                    data = 'steps.1.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == 4: # yolo
                    data = 'steps.3.produce'
                    self.primitives_arguments[i]['outputs'] = get_argument(data)
                    data = 'steps.2.produce'
                else: # other steps
                    data = 'steps.' + str(i-1) + '.produce'

            # Another object detection pipeline
            elif taskname == 'OBJECTDETECTION2':
                if i == 0: # denormalize
                    data = 'inputs.0'
                elif i == 2: # retina_net
                    data = 'steps.1.produce'
                    self.primitives_arguments[i]['outputs'] = get_argument(data)
                else: # other steps
                    data = 'steps.' + str(i-1) + '.produce' 

            # Collaborative filtering
            elif taskname == 'COLLABORATIVEFILTERING':
                if i == 0: # dataset_to_dataframe
                    data = 'inputs.0'
                elif i == num-1: # construct_predictions
                    data = 'steps.1.produce'
                    self.primitives_arguments[i]['reference'] = get_argument(data)
                    data = 'steps.' + str(i-1) + '.produce'
                elif i == 4: # extract_columns_by_semantic_types (targets)
                    data = 'steps.3.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['semantic_types'] = ['https://metadata.datadrivendiscovery.org/types/TrueTarget']
                elif i == 5: # extract_columns_by_semantic_types
                    data = 'steps.3.produce'
                elif i == 3:
                    data = 'steps.' + str(i-1) + '.produce'
                    self.hyperparams[i] = {}
                    self.hyperparams[i]['parse_semantic_types'] = ["http://schema.org/Integer", \
                                                                   "http://schema.org/Float"]
                elif i == 6: # collaborative_filtering
                    data = 'steps.4.produce'
                    self.primitives_arguments[i]['outputs'] = get_argument(data)
                    source = self.primitives_arguments[i]['outputs']['source']
                    execution_graph.add_edge(str(source), str(i))
                    data = 'steps.' + str(i-1) + '.produce'
                else: # other steps
                    data = 'steps.' + str(i-1) + '.produce'

            # Clustering
            elif taskname == 'CLUSTERING':
                if i == 0: # dataset_to_dataframe
                    data = 'inputs.0'
                elif i == num-1: # construct_predictions
                    data = 'steps.0.produce'
                    self.primitives_arguments[i]['reference'] = get_argument(data)
                    data = 'steps.' + str(i-1) + '.produce'
                else: # other steps
                    data = 'steps.' + str(i-1) + '.produce'
            else:
                if i == 0:
                    data = 'inputs.0'
                else:
                    data = 'steps.' + str(i-1) + '.produce'

            self.primitives_arguments[i]['inputs'] = get_argument(data)
            source = self.primitives_arguments[i]['inputs']['source']
            origin = self.primitives_arguments[i]['inputs']['origin']

            if i == 0:
                execution_graph.add_edge(origin, str(i))
            else:
                execution_graph.add_edge(str(source), str(i))

            argument_metadata = self.primitives[i].metadata.query()['primitive_code'].get('arguments', {})
            if argument_metadata.get("inputs", None) is None:
                self.primitives_arguments[i].pop("inputs", None)
        execution_order = list(nx.topological_sort(execution_graph))
        # Removing non-step inputs from the order
        execution_order = list(filter(lambda x: x.isdigit(), execution_order))
        self.execution_order = [int(x) for x in execution_order]

    def add_primitive(self, python_path, i):
        """
        Helper function to add a primitive in the pipeline with basic initialization only.
        """
        self.primitives_arguments[i] = {}
        self.hyperparams[i] = None
        self.pipeline.append(None)
        prim = d3m.index.get_primitive(python_path)
        self.primitives[i] = prim
        self.steptypes.append(StepType.PRIMITIVE)
        self.subpipelines[i] = None

    def add_subpipeline(self, pipeline):
        """
        Helper function to add a subpipeline(replace placeholder step) in the pipeline with basic initialization only.
        """
        i = len(self.primitives_arguments)-1

        self.primitives_arguments[i] = {}
        self.hyperparams[i] = None
        self.pipeline.append(None)
        self.primitives[i] = None
        self.steptypes[i] = StepType.SUBPIPELINE
        self.subpipelines[i] = pipeline.id
      
        data = 'steps.' + str(i-1) + '.produce'
        origin = data.split('.')[0]
        source = data.split('.')[1] 
        self.primitives_arguments[i]['inputs'] = {'origin': origin, 'source': int(source), 'data': data}

        data = 'steps.' + str(i) + '.' + pipeline.outputs[0][2]
        origin = data.split('.')[0]
        source = data.split('.')[1]
        self.outputs = []
        self.outputs.append((origin, int(source), data, "output predictions"))

    def add_step(self, python_path, inputstep=-1, outputstep=2, dataframestep=1, construct_primitive='d3m.primitives.data_transformation.construct_predictions.Common'):
        """
        Add new primitive (classifier/regressor)
        This is currently for classification/regression pipelines
        python_path: Primitive
        inputstep: Step index of inputs for the primitive
        outputstep: Step index of outputs for the primitive
        dataframestep: Step index of data frame for the construct_predictions/construct confidence primitive's reference (to get d3mIndex)
        """
        i = len(self.primitives_arguments)
        self.add_primitive(python_path, i)

        if inputstep == -1:
            inputstep = i-1
        # Connect to inputs
        data = 'steps.' + str(inputstep) + str('.produce')
        origin = data.split('.')[0]
        source = data.split('.')[1]
        self.primitives_arguments[i]['inputs'] = {'origin': origin, 'source': int(source), 'data': data}
        
        # Connect to outputs
        data = 'steps.' + str(outputstep) + str('.produce') # extract_columns_by_semantic_types (targets)
        origin = data.split('.')[0]
        source = data.split('.')[1]
        self.primitives_arguments[i]['outputs'] = {'origin': origin, 'source': int(source), 'data': data}

        if 'learner.random_forest' in python_path:
            self.hyperparams[i] = {}
            self.hyperparams[i]['compute_confidences'] = True
            self.hyperparams[i]['n_estimators'] = 100

        if 'SKlearn' in python_path:
            self.hyperparams[i] = {}
            hyperparam_spec = self.primitives[i].metadata.query()['primitive_code']['hyperparams']
            if 'n_estimators' in hyperparam_spec:
                self.hyperparams[i]['n_estimators'] = 100
            if 'n_neighbors' in hyperparam_spec:
                self.hyperparams[i]['n_neighbors'] = 10

        self.execution_order.append(i)

        i = i + 1
        self.add_primitive(construct_primitive, i)

        data = 'steps.' + str(i-1) + str('.produce')
        if 'construct_confidence' in construct_primitive: # For ROC_AUC metric! 
            data = 'steps.' + str(i-4) + str('.produce')  # Should point to d3m.primitives.operator.compute_unique_values.Common

        origin = data.split('.')[0]
        source = data.split('.')[1]
        self.primitives_arguments[i]['inputs'] = {'origin': origin, 'source': int(source), 'data': data}
        
        data = 'steps.' + str(dataframestep) + str('.produce')
        origin = data.split('.')[0]
        source = data.split('.')[1]
        self.primitives_arguments[i]['reference'] = {'origin': origin, 'source': int(source), 'data': data}

        if 'construct_confidence' in construct_primitive:
            self.hyperparams[i] = {}
            self.hyperparams[i]['primitive_learner'] = i-1

        self.execution_order.append(i)
        self.add_outputs()

    def splitter_present(self):
        python_path = self.primitives[0].metadata.query()['python_path']
        if 'splitter' in python_path:
            return True
        return False

    def complete_solution(self, optimal_params):
        """
        This is currently for classification/regression pipelines with AutoRPI
        Sets optimal hyperparamters found for AutoRPI primitive and the model primitive.
        """
        i = self.get_last_step()
        self.hyperparams[i] = {}
        self.hyperparams[i]['method'] = optimal_params[1]
        self.hyperparams[i]['nbins'] = optimal_params[0]

        i = i + 2
        python_path = self.primitives[i].metadata.query()['python_path']
        if 'linear_disc' not in python_path:
            self.hyperparams[i] = {}
            self.hyperparams[i]['n_estimators'] = optimal_params[2]
        if 'gradient_boosting' in python_path:
            self.hyperparams[i]['learning_rate'] = 10/optimal_params[2]

    def add_RPI_step(self, RPI_step, python_path, output_step):
        """
        Complete pipeline with RPIprimitive and ML model
        This is currently for classification/regression pipelines with d3m.primitives.feature_selection.joint_mutual_information.AutoRPI
        and d3m.primitives.feature_selection.simultaneous_markov_blanket.AutoRPI 
        RPI_step: RPI primitive (Either d3m.primitives.feature_selection.joint_mutual_information.AutoRPI or d3m.primitives.feature_selection.simultaneous_markov_blanket.AutoRPI)
        python_path: ML model being added (Classifier/regressor)
        output_step: Step index of targets in the pipeline
        """
        n_steps = len(self.primitives_arguments) + 1
        i = n_steps-1

        # Add RPI step
        self.add_primitive(RPI_step, i)

        data = 'steps.' + str(i-1) + str('.produce')
        self.primitives_arguments[i]['inputs'] = get_argument(data)

        data = 'steps.' + str(output_step) + str('.produce') # extract_columns_by_semantic_types (targets)
        self.primitives_arguments[i]['outputs'] = get_argument(data)

        self.execution_order.append(i)

        # Add imputer
        i = i + 1
        self.add_primitive('d3m.primitives.data_cleaning.imputer.SKlearn', i)
        data = 'steps.' + str(i-1) + str('.produce')
        self.primitives_arguments[i]['inputs'] = get_argument(data)
        self.hyperparams[i] = {}
        self.hyperparams[i]['strategy'] = 'most_frequent'
        self.execution_order.append(i)

        # Add ML model
        i = i + 1
        self.add_primitive(python_path, i)
        data = 'steps.' + str(i-1) + str('.produce')
        self.primitives_arguments[i]['inputs'] = get_argument(data)
        data = 'steps.' + str(output_step) + str('.produce') # extract_columns_by_semantic_types (targets)
        self.primitives_arguments[i]['outputs'] = get_argument(data)
        self.execution_order.append(i)

        # Add construct_predictions
        i = i + 1
        self.add_primitive('d3m.primitives.data_transformation.construct_predictions.Common', i)
        data = 'steps.' + str(i-1) + str('.produce')
        self.primitives_arguments[i]['inputs'] = get_argument(data) 
        data = 'steps.' + str(1) + str('.produce')
        self.primitives_arguments[i]['reference'] = get_argument(data) 
        self.execution_order.append(i)

        self.add_outputs()

    def add_outputs(self): 
        """
        Add outputs as last step for pipeline
        Also compute produce order.
        """
        n_steps = len(self.execution_order)
        
        self.outputs = []

        data = 'steps.' + str(self.execution_order[n_steps-1]) + '.produce'

        origin = data.split('.')[0]
        source = data.split('.')[1]
        self.outputs.append((origin, int(source), data, "output predictions"))

        # Creating set of steps to be call in produce
        self.produce_order = set()

        current_step = int(source)
        self.produce_order.add(current_step)

        # Iterate through the pipeline execution order
        for i in range(0, len(self.execution_order)):
            name = list(self.primitives_arguments[current_step].keys())[0]
            step_origin = self.primitives_arguments[current_step][name]['origin']
            step_source = self.primitives_arguments[current_step][name]['source']
            if step_origin != 'steps':
                break
            else:
                self.produce_order.add(step_source)
                current_step = step_source

        data = 'steps.' + str(self.execution_order[n_steps-1]) + '.produce'
        source = data.split('.')[1]
        current_step = int(source)

        # Iterate once more. Steps to 'reference' argument should not get missed!
        for i in range(0, len(self.execution_order)):
            if 'reference' in self.primitives_arguments[current_step]:
                step_source = self.primitives_arguments[current_step]['reference']['source']
                if step_source in self.produce_order:
                    break
                else:
                    self.produce_order.add(step_source)
                    current_step = step_source

                    for j in range(0, len(self.execution_order)):
                        name = list(self.primitives_arguments[current_step].keys())[0]
                        step_origin = self.primitives_arguments[current_step][name]['origin']
                        step_source = self.primitives_arguments[current_step][name]['source']
                        if step_origin != 'steps':
                            break
                        else:
                            self.produce_order.add(step_source)
                            current_step = step_source

    def process_step(self, n_step, primitives_outputs, action, arguments):
        """
        Process each step of a pipeline
        This could be used while scoring or fitting a pipeline
        """
        # Subpipeline step
        if self.steptypes[n_step] is StepType.SUBPIPELINE:
            primitive_arguments = {}
            for argument, value in self.primitives_arguments[n_step].items():
                if value['origin'] == 'steps':
                    primitive_arguments[argument] = primitives_outputs[value['source']]
                else:
                    primitive_arguments[argument] = arguments['inputs'][value['source']]
            return self._pipeline_step_fit(n_step, self.subpipelines[n_step], primitive_arguments, arguments, action)

        # Primitive step
        if self.steptypes[n_step] is StepType.PRIMITIVE:
            primitive_arguments = {}
            python_path = self.primitives[n_step].metadata.query()['python_path']
            for argument, value in self.primitives_arguments[n_step].items():
                if value['origin'] == 'steps':
                    # Primitives with multiple produce methods used in pipeline
                    if 'DistilLinkPrediction' in python_path or \
                       'DistilSeededGraphMatcher' in python_path or \
                       'DistilCommunityDetection' in python_path or \
                       'DistilVertexNomination' in python_path or \
                       'DistilEdgeListLoader' in python_path or \
                       'DistilAudioTransfer' in python_path or \
                       'DistilSingleGraphLoader' in python_path or \
                       'DistilGraphLoader' in python_path or \
                       (self.taskname == 'AUDIO' and 'column_parser' in python_path):
                        method = value['data'].split('.')[2]
                        primitive_arguments[argument] = primitives_outputs[value['source']][method]
                    else: # Single output
                        primitive_arguments[argument] = primitives_outputs[value['source']]
                else:
                    primitive_arguments[argument] = arguments['inputs'][value['source']]

            # Score the pipeline at model stage (Run cross-validation)
            if action is ActionType.SCORE and self.is_last_step(n_step) == True: 
                primitive = self.primitives[n_step]
                primitive_desc = arguments['primitive_dict'][primitive]
                mode = None
                if 'mode' in arguments:
                    mode = arguments['mode']
                return self.score_step(primitive, primitive_arguments, arguments['metric'], arguments['posLabel'], primitive_desc, \
                                       self.hyperparams[n_step], n_step, mode)
            else: # Fit the pipeline step
                primitive = self.primitives[n_step]
                if 'DistilTextEncoder' in python_path and self.pipeline[n_step] is None:
                    self.cross_outputs = self.cross_validate_step(n_step, primitive, primitive_arguments)
                v = self.fit_step(n_step, primitive, primitive_arguments)
                return v

        # Placeholder step
        if self.steptypes[n_step] is StepType.PLACEHOLDER:
            return primitives_outputs[n_step-1]
 
    def is_last_step(self, n):
        last_step = self.get_last_step()
        if n == self.execution_order[last_step]:
            return True
        return False

    def get_last_step(self):
        """
        Return index of step which needs to be optimized/cross-validated.
        Typically this is the step for a classifier/regressor which can be optimized/cross-validated.
        This is the last-1 step of the pipeline, since it is followed by construct_predictions primitive to construct predictions output from d3mIndex and primitive output.
        """
        n_steps = len(self.execution_order)
        last_step = self.execution_order[n_steps-1]

        if self.steptypes[last_step] is StepType.SUBPIPELINE:
            return n_steps-1

        if self.primitives[last_step] is None:
            return n_steps-1

        if self.taskname == 'PIPELINE_RPI':
            index = 0
            for p in self.primitives:
                python_path = None
                if self.primitives[index] is not None:
                    python_path = self.primitives[index].metadata.query()['python_path'] 
                    if 'RPI' in python_path:
                        return index
                index = index + 1
 
        last_step = len(self.primitives)-1
        if 'construct_' in self.primitives[last_step].metadata.query()['python_path']:
            return last_step-1
        else:
            return last_step

    def score_solution(self, **arguments):
        """
        Score a solution 
        """
        score = 0.0
        primitives_outputs = [None] * len(self.primitives)

        last_step = self.get_last_step()

        if self.primitives_outputs is None: # Run entire pipeline
            for i in range(0, last_step+1):
                n_step = self.execution_order[i]
                primitives_outputs[n_step] = self.process_step(n_step, primitives_outputs, ActionType.SCORE, arguments)
                if self.isDataFrameStep(n_step) == True:
                    self.exclude(primitives_outputs[n_step])
        else: # Cached outputs. Score the ML model only
            primitives_outputs[last_step] = self.process_step(last_step, self.primitives_outputs, ActionType.SCORE, arguments)

        (score, optimal_params) = primitives_outputs[self.execution_order[last_step]]
        if self.steptypes[self.execution_order[last_step]] != StepType.SUBPIPELINE:
            self.hyperparams[last_step] = optimal_params
        
        return (score, optimal_params)

    def set_distil_text_hyperparam(self):
        """
        For text regression problems, set appropriate metric for DistilTextEncoder
        """
        for i in range(len(self.primitives)):
            p = self.primitives[i]
            path = p.metadata.query()['python_path'] 
            if 'DistilTextEncoder' in path:
                self.hyperparams[i] = {}
                self.hyperparams[i]['metric'] = 'meanSquaredError'
                break

    def set_classifier_hyperparam(self):
        for i in range(len(self.primitives)):
            p = self.primitives[i]
            path = p.metadata.query()['python_path']
            if 'random_forest' in path or 'extra_trees' in path or 'gradient_boosting' in path:
                self.hyperparams[i] = {}
                self.hyperparams[i]['n_estimators'] = 5
                break

    def set_hyperparams(self, solution_dict, hp):
        """
        Set hyperparameters for the primtiive at the "last" step.
        """
        n_step = self.get_last_step()

        if self.primitives[self.execution_order[n_step]] is not None: 
            if 'RPI' in self.primitives[self.execution_order[n_step]].metadata.query()['python_path']:
                self.complete_solution(hp)
            else:
                self.hyperparams[self.execution_order[n_step]] = hp
        else:
            solution_id = self.subpipelines[self.execution_order[n_step]]
            solution_dict[solution_id].set_hyperparams(solution_dict, hp)

        self.pipeline_description = None #Recreate it again

    def run_basic_solution(self, **arguments):
        """
        Runs common parts of a pipeline before adding last step of classifier/regressor
        This saves on data processing, featurizing steps being repeated across multiple pipelines.
        This is probably the most IMPORTANT step for multimedia datasets(audio/video/images), text datasets, or large datasets.
        Runs single-pass on expensive data loading, processing steps before forking multiple processes for validating ML models. 
        Forked processes get cached outputs and work on cross-validating the ML models only.
        """
        self.primitives_outputs = [None] * len(self.execution_order)

        output_step = arguments['output_step']
        if 'dataframe_step' in arguments:
            dataframe_step = arguments['dataframe_step']
        else:
            dataframe_step = self.index_denormalize + 1

        if 'input_step' in arguments:
            input_step = arguments['input_step']
        else:
            input_step = len(self.execution_order)-1

        # Execute the initial steps of a pipeline.
        # This executes all the common data processing steps of classifier/regressor pipelines, but only once for all pipelines.
        # Inputs and outputs for the next step (classifier/regressor) are stored.
        for i in range(0, len(self.execution_order)):
            n_step = self.execution_order[i]
            python_path = self.primitives[n_step].metadata.query()['python_path']
       
            if 'one_hot_encoder' in python_path:
                (cols, ordinals, add_floats) = helper_functions.get_cols_to_encode(self.primitives_outputs[n_step-1])
                self.hyperparams[n_step] = {}
                self.hyperparams[n_step]['use_columns'] = list(cols)
                self.hyperparams[n_step]['max_one_hot'] = 100
                print("Cats = ", cols)
                #print(self.primitives_outputs[n_step-1].iloc[:,cols])

            if python_path == 'd3m.primitives.data_transformation.column_parser.Common':
                if self.hyperparams[n_step] is None:
                    self.hyperparams[n_step] = {}
                exclude_atts = set() #
                if self.ordinal_atts is not None and len(self.ordinal_atts) > 0:
                    exclude_atts.update(list(self.ordinal_atts))
                if self.exclude_columns is not None and len(self.exclude_columns) > 0:
                    exclude_atts.update(list(self.exclude_columns))
                if len(exclude_atts) > 0:
                    self.hyperparams[n_step]['exclude_columns'] = list(exclude_atts)

            if self.exclude_columns is not None and len(self.exclude_columns) > 0:
                if python_path == 'd3m.primitives.data_transformation.extract_columns_by_semantic_types.Common':
                    if self.hyperparams[n_step] is None:
                        self.hyperparams[n_step] = {}
                    exclude_atts = set()
                    if 'exclude_columns' in self.hyperparams[n_step]:
                        exclude_atts.update(self.hyperparams[n_step]['exclude_columns'])
                    exclude_atts.update(list(self.exclude_columns))
                    self.hyperparams[n_step]['exclude_columns'] = list(exclude_atts)
                    self.exclude_columns = None

            if 'add_semantic_types' in python_path:
                from_step = int(self.primitives_arguments[n_step]['inputs']['source'])
                from_python_path = self.primitives[from_step].metadata.query()['python_path']
                if 'profiler' not in from_python_path:
                    self.hyperparams[n_step]['columns'] = list(range(len(self.primitives_outputs[from_step].columns)))
        
            # Running the primitive at n_step and cache the output
            logging.critical("Running %s", python_path)
            start = timer()
            self.primitives_outputs[n_step] = self.process_step(n_step, self.primitives_outputs, ActionType.FIT, arguments)
            end = timer()
            logging.critical("Time taken : %s sec", end - start)
            #if n_step > 1:
            #    logging.critical("%s", self.primitives_outputs[n_step].iloc[0:5,:])
            if self.isDataFrameStep(n_step) == True:
                self.exclude(self.primitives_outputs[n_step])

        # Remove other intermediate step outputs, they are not needed anymore.
        # Only inputs, outputs for training model are retained.
        # Also dataframe for constructing predictions.
        for i in range(0, len(self.execution_order)):
            if i == dataframe_step or i == output_step or i == input_step:
                continue
            self.primitives_outputs[i] = [None]

        # Randomly sample 100K points for scoring solutions
        if len(self.primitives_outputs[output_step]) > 1000000:
            np.random.seed(1979)
            indices = np.random.choice(len(self.primitives_outputs[output_step]),100000, replace=False)
            self.primitives_outputs[input_step] = self.primitives_outputs[input_step].iloc[indices,:]
            self.primitives_outputs[output_step] = self.primitives_outputs[output_step].iloc[indices,:]
        self.primitives_outputs[dataframe_step] = self.primitives_outputs[dataframe_step].iloc[0,:]
        self.total_cols = len(self.primitives_outputs[input_step].columns) 

    def get_total_cols(self):
        return self.total_cols

    def score_step(self, primitive: PrimitiveBaseMeta, primitive_arguments, metric, posLabel, primitive_desc, hyperparams, step_index, mode):
        """
        Last step of a solution evaluated for score_solution()
        Does hyperparameters tuning
        """
        custom_hyperparams = dict()
        if hyperparams is not None:
            for hyperparam, value in hyperparams.items():
                custom_hyperparams[hyperparam] = value

        if self.cross_outputs is not None:
            return primitive_desc.score_array(self.cross_outputs[0], self.cross_outputs[1], self.cross_outputs[2], self.cross_outputs[3], metric, posLabel, custom_hyperparams, self.taskname, self.id, mode)

        training_arguments_primitive = self._primitive_arguments(primitive, 'set_training_data')
        training_arguments = {}

        for param, value in primitive_arguments.items():
            if param in training_arguments_primitive:
                training_arguments[param] = value
        
        outputs = None
        if 'outputs' in training_arguments:
            outputs = training_arguments['outputs']

        python_path = primitive.metadata.query()['python_path']
        train_data = None
        if 'inputs' in training_arguments:
            train_data = training_arguments['inputs']

        if 'RPI' in python_path:    
            ml_python_path = self.primitives[step_index+2].metadata.query()['python_path'] 
            optimal_params = primitive_desc.optimize_RPI_bins(train_data, outputs, ml_python_path, metric, posLabel)
            score = optimal_params[3]
            return (score, optimal_params)
        else:  
            (score, optimal_params) = primitive_desc.score_primitive(train_data, outputs, metric, posLabel, custom_hyperparams, self.taskname, self.id, mode)
        
        return (score, optimal_params) 

    def describe_solution(self, prim_dict, solution_dict):
        """
        Required for TA2-TA3 API DescribeSolution().
        """
        inputs = []
        for i in range(len(self.inputs)):
            inputs.append(pipeline_pb2.PipelineDescriptionInput(name=self.inputs[i]["name"]))

        outputs=[]
        outputs.append(pipeline_pb2.PipelineDescriptionOutput(name="predictions", data=self.outputs[0][2]))

        steps=[]
        
        for j in range(len(self.primitives_arguments)):
            s = self.primitives[j]
            if s is None: # subpipeline
                s = self.subpipelines[j]
                step_inputs = []
                for argument, data in self.primitives_arguments[j].items():
                    argument_edge = data['data']
                    sa = pipeline_pb2.StepInput(data = argument_edge)
                    step_inputs.append(sa)
                step_outputs = []
                subpipe = solution_dict[s]
                for output in subpipe.outputs:
                    step_outputs.append(pipeline_pb2.StepOutput(id = output[2]))         
                p = pipeline_pb2.SubpipelinePipelineDescriptionStep(pipeline=pipeline_pb2.PipelineDescription(id=s), inputs=step_inputs, outputs=step_outputs)
                steps.append(pipeline_pb2.PipelineDescriptionStep(pipeline=p))
            else: # primitive
                prim = prim_dict[s]
                p = primitive_pb2.Primitive(id=prim.id, version=prim.primitive_class.version, python_path=prim.primitive_class.python_path, name=prim.primitive_class.name, digest=prim.primitive_class.digest)

                arguments={}
                for argument, data in self.primitives_arguments[j].items():
                    argument_edge = data['data']
                    sa = pipeline_pb2.PrimitiveStepArgument(container = pipeline_pb2.ContainerArgument(data=argument_edge))
                    arguments[argument] = sa

                step_outputs = []
                for a in prim.primitive_class.produce_methods:
                    step_outputs.append(pipeline_pb2.StepOutput(id=a))

                hyperparameters = self.get_hyperparams(j,prim_dict)
                step_hyperparameters = {}
                for name, value in hyperparameters.items():
                    if name == "primitive":
                        step_hyperparameters[name] = pipeline_pb2.PrimitiveStepHyperparameter(primitive=pipeline_pb2.PrimitiveArgument(data=value.raw.int64))
                    else:
                        step_hyperparameters[name] = pipeline_pb2.PrimitiveStepHyperparameter(value=pipeline_pb2.ValueArgument(data=value))
                steps.append(pipeline_pb2.PipelineDescriptionStep(primitive=pipeline_pb2.PrimitivePipelineDescriptionStep(primitive=p, arguments=arguments, outputs=step_outputs, hyperparams=step_hyperparameters)))
           
        return pipeline_pb2.PipelineDescription(id=self.id, source=self.source, created=self.created,
         name=self.name, description=self.description, inputs=inputs, outputs=outputs, steps=steps)

    def get_hyperparams(self, step, prim_dict):
        """
        Required for TA2-TA3 API DescribeSolution().
        """
        p = prim_dict[self.primitives[step]]
        custom_hyperparams = self.hyperparams[step]

        send_params={}
       
        if custom_hyperparams is None:
            return send_params
 
        for name, value in custom_hyperparams.items():
            if name == "primitive":
                send_params[name] = value_pb2.Value(raw=value_pb2.ValueRaw(int64=value))
                continue
            else:
                send_params[name] = get_pipeline_values(value)
           
        return send_params
