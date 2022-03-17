import math
from functools import partial
from typing import Dict, Optional

from PyQt6.QtCore import QPoint, QRect
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QColorDialog, QGridLayout, QLabel, QPushButton, QWidget

MARKER_CONTROL_MAP = {}


def register_marker(cls):
    MARKER_CONTROL_MAP[cls.name] = cls
    return cls


class BaseMarkerControl(QWidget):
    name = None

    def __init__(self, on_change: Optional[callable] = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.offset = (0, 0)
        self.center_offset = (0, 0)
        self.hex_color = "#abcdef"

        self.on_change = on_change

        layout = QGridLayout()

        color_button = QPushButton("✎")

        up_button = QPushButton("▲")
        down_button = QPushButton("▼")
        left_button = QPushButton("◀")
        right_button = QPushButton("►")

        offset_label = QLabel("")

        color_button.clicked.connect(self.choose_color)
        up_button.clicked.connect(partial(self.change_offset, y=-1))
        down_button.clicked.connect(partial(self.change_offset, y=+1))
        left_button.clicked.connect(partial(self.change_offset, x=-1))
        right_button.clicked.connect(partial(self.change_offset, x=+1))

        layout.addWidget(color_button, 1, 0)
        layout.addWidget(up_button, 0, 2)
        layout.addWidget(down_button, 2, 2)
        layout.addWidget(left_button, 1, 1)
        layout.addWidget(right_button, 1, 3)
        layout.addWidget(offset_label, 1, 2)

        self.setLayout(layout)

        self.layout = layout
        self.color_button = color_button
        self.offset_label = offset_label

        self.update_btn_color()
        self.update_offset_label()

    @classmethod
    def from_config(
        cls,
        config: Dict,
        on_change: Optional[callable] = None,
        on_remove: Optional[callable] = None,
    ):
        marker_type = config.pop("type")
        control: BaseMarkerControl = MARKER_CONTROL_MAP[marker_type](
            on_change, on_remove
        )

        for option, value in config.items():
            setattr(control, option, value)

        control.update_all()
        return control

    def to_config(self):
        return {
            "type": self.name,
            "offset": self.offset,
            "hex_color": self.hex_color,
        }

    def choose_color(self):
        new_color = QColorDialog.getColor(initial=QColor(self.hex_color))
        if new_color.isValid():
            self.hex_color = new_color.name()
            self.update_btn_color()
            if self.on_change:
                self.on_change(self)

    def change_offset(self, x=0, y=0):
        self.offset = (self.offset[0] + x, self.offset[1] + y)
        self.update_offset_label()
        if self.on_change:
            self.on_change(self)

    def update_btn_color(self):
        self.color_button.setStyleSheet(f"background-color : {self.hex_color}")

    def update_offset_label(self):
        d = math.sqrt(sum(offset**2 for offset in self.offset))
        self.offset_label.setText(f"∆x={self.offset[0]} ∆y={self.offset[1]}\nd={d:.2f}")

    def paint(self, painter: QPainter, rect: QRect):
        raise NotImplementedError()

    def update_all(self):
        self.update_offset_label()
        self.update_btn_color()


class CenterControl(BaseMarkerControl):
    name = "center"
    half_line_length = 20

    def paint(self, painter: QPainter, rect: QRect):
        x = rect.center().x() + rect.width() * self.offset[0] / 100
        y = rect.center().y() + rect.height() * self.offset[1] / 100
        half_length = rect.width() * self.half_line_length / 100
        painter.setPen(QColor(self.hex_color))
        painter.drawLine(x, y - half_length, x, y + half_length)
        painter.drawLine(x - half_length, y, x + half_length, y)

    def apply_config(self, config):
        self.offset = config["offset"]
        self.hex_color = config["hex_color"]
        self.update_all()


class RemovableMarkerControl(BaseMarkerControl):
    def __init__(
        self,
        on_change: Optional[callable] = None,
        on_remove: Optional[callable] = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(on_change, *args, **kwargs)
        self.on_remove = on_remove

        remove_button = QPushButton("x")
        remove_button.clicked.connect(self.remove_clicked)

        self.layout.addWidget(remove_button, 1, 5)

    def remove_clicked(self):
        if self.on_remove:
            self.on_remove(self)


@register_marker
class CircleControl(RemovableMarkerControl):
    name = "circle"

    def __init__(
        self,
        on_change: Optional[callable] = None,
        on_remove: Optional[callable] = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(on_change, on_remove, *args, **kwargs)
        self.radius = 50

        bigger_button = QPushButton("+")
        smaller_button = QPushButton("-")
        smaller_button.clicked.connect(partial(self.change_radius, r=-1))
        bigger_button.clicked.connect(partial(self.change_radius, r=+1))

        radius_label = QLabel("")

        self.layout.addWidget(bigger_button, 0, 4)
        self.layout.addWidget(smaller_button, 2, 4)
        self.layout.addWidget(radius_label, 1, 4)

        self.radius_label = radius_label

        self.update_radius_label()

    def change_radius(self, r):
        self.radius += r
        self.update_radius_label()
        if self.on_change:
            self.on_change(self)

    def update_radius_label(self):
        self.radius_label.setText(f"r={self.radius}")

    def paint(self, painter: QPainter, rect: QRect):
        x = (
            rect.center().x()
            + rect.width() * (self.offset[0] + self.center_offset[0]) / 100
        )
        y = (
            rect.center().y()
            + rect.height() * (self.offset[1] + self.center_offset[1]) / 100
        )
        radius = rect.width() * self.radius / 100
        center = QPoint(x, y)
        painter.setPen(QColor(self.hex_color))
        painter.drawEllipse(center, radius, radius)

    def to_config(self):
        config = super().to_config()
        config.update({"radius": self.radius})
        return config

    def update_all(self):
        super().update_all()
        self.update_radius_label()
