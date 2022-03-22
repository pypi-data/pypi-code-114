from pydantic import Field
from koil.composition.base import PedanticKoil

from typing import Optional, Type, TypeVar

from koil.qt import QtGeneratorTask, QtTask
from qtpy import QtWidgets, QtCore


class WrappedObject(QtCore.QObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_koil(self, koil: PedanticKoil):
        self.koil = koil

    def close(self):
        self.koil.__exit__(None, None, None)


class QtPedanticKoil(PedanticKoil):
    disconnect_on_close = True
    auto_connect = True
    task_class: Optional[Type[QtTask]] = Field(default=QtTask, exclude=True)
    gen_class: Optional[Type[QtGeneratorTask]] = Field(
        default=QtGeneratorTask, exclude=True
    )
    qobject: WrappedObject = Field(default_factory=WrappedObject)

    def __init__(self, **data):
        super().__init__(**data)
        if self.auto_connect:
            self.__enter__()

    def __enter__(self):
        self.qobject.set_koil(self)
        ap_instance = QtWidgets.QApplication.instance()
        if ap_instance is None:
            raise NotImplementedError("Qt Application not found")
        if self.disconnect_on_close:
            ap_instance.lastWindowClosed.connect(self.qobject.close)
        return super().__enter__()

    class Config:
        arbitrary_types_allowed = True
