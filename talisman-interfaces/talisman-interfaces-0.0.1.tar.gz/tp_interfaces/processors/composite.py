from typing import Iterable, Sequence, Tuple, Type, TypeVar

from tdm.abstract.datamodel import AbstractTreeDocumentContent
from tdm.datamodel import TalismanDocument

from tp_interfaces.abstract import AbstractCompositeModel, AbstractDocumentProcessor, ImmutableBaseModel

_DocumentContent = TypeVar('_DocumentContent', bound=AbstractTreeDocumentContent)
_Config = TypeVar('_Config', bound=ImmutableBaseModel)


class SequentialConfig(ImmutableBaseModel):
    def get_model_config(self, index: int) -> _Config:
        pass


class SequentialDocumentProcessor(
    AbstractCompositeModel[AbstractDocumentProcessor],
    AbstractDocumentProcessor[SequentialConfig, _DocumentContent]
):

    def __init__(self, processors: Iterable[AbstractDocumentProcessor]):
        AbstractCompositeModel[AbstractDocumentProcessor].__init__(self, processors)
        AbstractDocumentProcessor.__init__(self)

    def process_doc(self, document: TalismanDocument[_DocumentContent], config: _Config) -> TalismanDocument[_DocumentContent]:
        return self.process_docs([document], config)[0]

    def process_docs(self, documents: Sequence[TalismanDocument[_DocumentContent]], config: SequentialConfig) \
            -> Tuple[TalismanDocument[_DocumentContent], ...]:
        for _index, processor in enumerate(self._models):
            documents = processor.process_docs(documents, config)  # TODO implement correct configuration
        return documents

    @property
    def config_type(self) -> Type[SequentialConfig]:
        # TODO: generate runtime config
        return ImmutableBaseModel
