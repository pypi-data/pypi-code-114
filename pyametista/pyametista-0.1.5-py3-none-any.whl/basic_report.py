import os

from pyametista.engine import reportGenerator


class BasicReport:
    """ "
    Base wrapper class to generate reports.
    """

    def __init__(
        self, jrxml_filename, output_filename, data_config=None, fonts=None, report_type="pdf"
    ):
        self.jrxml_filename = jrxml_filename
        self.output_filename = output_filename
        self.data_config = data_config

        if fonts is not None:
            self.fonts = fonts
        else:
            self.fonts = [
                {"font_path": [os.path.join(os.path.abspath(os.path.dirname(__file__)), "fonts")]},
                {
                    "font_filename": "OpenSans-Regular.ttf",
                    "fonts": [{"index": 0, "name": "OpenSans"}],
                },
                {
                    "font_filename": "OpenSans-Bold.ttf",
                    "fonts": [{"index": 1, "name": "OpenSans-Bold"}],
                },
                {
                    "font_filename": "OpenSans-Italic.ttf",
                    "fonts": [{"index": 2, "name": "OpenSans-Italic"}],
                },
                {
                    "font_filename": "OpenSans-BoldItalic.ttf",
                    "fonts": [{"index": 3, "name": "OpenSans-BoldItalic"}],
                },
                {
                    "font-family": {
                        "name": "OpenSans",
                        "normal": "OpenSans",
                        "bold": "OpenSans-Bold",
                        "italic": "OpenSans-Italic",
                        "boldItalic": "OpenSans-BoldItalic",
                    }
                },
                {"font_filename": "Roboto-Regular.ttf", "fonts": [{"index": 0, "name": "Roboto"}]},
                {
                    "font_filename": "Roboto-Bold.ttf",
                    "fonts": [{"index": 1, "name": "Roboto-Bold"}],
                },
                {
                    "font_filename": "Roboto-Italic.ttf",
                    "fonts": [{"index": 2, "name": "Roboto-Italic"}],
                },
                {
                    "font_filename": "Roboto-BoldItalic.ttf",
                    "fonts": [{"index": 3, "name": "Roboto-BoldItalic"}],
                },
                {
                    "font-family": {
                        "name": "Roboto",
                        "normal": "Roboto",
                        "bold": "Roboto-Bold",
                        "italic": "Roboto-Italic",
                        "boldItalic": "Roboto-BoldItalic",
                    }
                },
                {
                    "font_filename": "RobotoSlab-Regular.ttf",
                    "fonts": [{"index": 0, "name": "RobotoSlab"}],
                },
                {
                    "font_filename": "RobotoSlab-Bold.ttf",
                    "fonts": [{"index": 1, "name": "RobotoSlab-Bold"}],
                },
                {
                    "font-family": {
                        "name": "RobotoSlab",
                        "normal": "RobotoSlab",
                        "bold": "RobotoSlab-Bold",
                    }
                },
            ]

        self.report_type = report_type

    def generate_report(self):
        reportGenerator.generate_report(
            jrxml_filename=self.jrxml_filename,
            output_filename=self.output_filename,
            data_config=self.data_config,
            fonts=self.fonts,
            report_type=self.report_type,
        )

    def set_report_type(self, report_type):
        self.report_type = report_type
