from PyQt5 import QtWidgets
from propeller_design_tools.science_spinbox_class import ScientificDoubleSpinBox


class PDT_GroupBox(QtWidgets.QGroupBox):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10

        super(PDT_GroupBox, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)


class PDT_Label(QtWidgets.QLabel):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None

        super(PDT_Label, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)


class PDT_CheckBox(QtWidgets.QCheckBox):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        checked = kwargs.pop('checked') if 'checked' in kwargs else False

        super(PDT_CheckBox, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_checked(checked=checked)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_checked(self, checked: bool):
        self.setChecked(checked)


class PDT_PushButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None

        super(PDT_PushButton, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)


class PDT_LineEdit(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None

        super(PDT_LineEdit, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)


class PDT_ComboBox(QtWidgets.QComboBox):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None

        super(PDT_ComboBox, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)


class PDT_TextEdit(QtWidgets.QTextEdit):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None
        height = kwargs.pop('height') if 'height' in kwargs else None
        read_only = kwargs.pop('read_only') if 'read_only' in kwargs else True

        super(PDT_TextEdit, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)
        self.set_height(height=height)
        self.set_read_only(read_only=read_only)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)

    def set_height(self, height: int):
        if height is not None:
            self.setFixedHeight(height)

    def set_read_only(self, read_only: bool):
        self.setReadOnly(read_only)


class PDT_TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10

        super(PDT_TabWidget, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)


class PDT_SpinBox(QtWidgets.QSpinBox):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None
        height = kwargs.pop('height') if 'height' in kwargs else None
        special_str = kwargs.pop('special_str') if 'special_str' in kwargs else None
        box_range = kwargs.pop('box_range') if 'box_range' in kwargs else None
        box_single_step = kwargs.pop('box_single_step') if 'box_single_step' in kwargs else None

        super(PDT_SpinBox, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)
        self.set_height(height=height)
        self.set_box_range(box_range=box_range)
        self.set_box_single_step(box_single_step=box_single_step)
        self.set_special_str(special_str=special_str)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)

    def set_height(self, height: int):
        if height is not None:
            self.setFixedHeight(height)

    def set_special_str(self, special_str: str):
        if special_str is not None:
            self.setSpecialValueText(special_str)

    def set_box_range(self, box_range):
        if box_range is not None:
            self.setRange(*box_range)   # the * unpacks this from tuple or list into 2 values min, max

    def set_box_single_step(self, box_single_step):
        if box_single_step is not None:
            self.setSingleStep(box_single_step)


class PDT_DoubleSpinBox(QtWidgets.QDoubleSpinBox):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None
        height = kwargs.pop('height') if 'height' in kwargs else None
        special_str = kwargs.pop('special_str') if 'special_str' in kwargs else None
        box_range = kwargs.pop('box_range') if 'box_range' in kwargs else None
        box_single_step = kwargs.pop('box_single_step') if 'box_single_step' in kwargs else None

        super(PDT_DoubleSpinBox, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)
        self.set_height(height=height)
        self.set_box_range(box_range=box_range)
        self.set_box_single_step(box_single_step=box_single_step)
        self.set_special_str(special_str=special_str)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)

    def set_height(self, height: int):
        if height is not None:
            self.setFixedHeight(height)

    def set_special_str(self, special_str: str):
        if special_str is not None:
            self.setSpecialValueText(special_str)

    def set_box_range(self, box_range):
        if box_range is not None:
            self.setRange(*box_range)   # the * unpacks this from tuple or list into 2 values min, max

    def set_box_single_step(self, box_single_step):
        if box_single_step is not None:
            self.setSingleStep(box_single_step)


class PDT_ScienceSpinBox(ScientificDoubleSpinBox):
    def __init__(self, *args, **kwargs):
        italic = kwargs.pop('italic') if 'italic' in kwargs else False
        bold = kwargs.pop('bold') if 'bold' in kwargs else False
        font_size = kwargs.pop('font_size') if 'font_size' in kwargs else 10
        width = kwargs.pop('width') if 'width' in kwargs else None
        height = kwargs.pop('height') if 'height' in kwargs else None
        special_str = kwargs.pop('special_str') if 'special_str' in kwargs else None
        box_range = kwargs.pop('box_range') if 'box_range' in kwargs else None

        super(PDT_ScienceSpinBox, self).__init__(*args, **kwargs)

        self.set_italic(italic=italic)
        self.set_bold(bold=bold)
        self.set_font_size(font_size=font_size)
        self.set_width(width=width)
        self.set_height(height=height)
        self.set_special_str(special_str=special_str)
        self.set_box_range(box_range=box_range)

    def set_italic(self, italic: bool):
        font = self.font()
        font.setItalic(italic)
        self.setFont(font)

    def set_bold(self, bold: bool):
        font = self.font()
        font.setBold(bold)
        self.setFont(font)

    def set_font_size(self, font_size: int):
        font = self.font()
        font.setPointSize(font_size)
        self.setFont(font)

    def set_width(self, width: int):
        if width is not None:
            self.setFixedWidth(width)

    def set_height(self, height: int):
        if height is not None:
            self.setFixedHeight(height)

    def set_special_str(self, special_str: str):
            if special_str is not None:
                self.setSpecialValueText(special_str)

    def set_box_range(self, box_range):
        if box_range is not None:
            self.setRange(*box_range)   # the * unpacks this from tuple or list into 2 values min, max
