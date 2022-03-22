"""Classes that check the values in the dictionary included in the code"""

import copy
import json

from .constants import CATEGORICAL_SCHEMES, ORDERED_SCHEMES


class DictKWS:
    def __init__(self):
        self.kws = {}

    def __repr__(self):
        aux = copy.deepcopy(self.kws)
        for attr, value in self.__dict__.items():
            if attr != "kws":
                aux.update(value.kws)

        return json.dumps(aux)


class LegendHoverKws(DictKWS):
    def __init__(self, legend_kws):
        super().__init__()
        self.kws = {
            "show": True,
            "scale_size": 1,
            "color_source_hovered": "#2c7bb6",
            "color_target_hovered": "#d7191c",
        }
        self.kws.update(legend_kws)


class NodeCircleKws(DictKWS):
    def __init__(self, node_kws, dataset):
        super().__init__()
        self.kws = {"tooltip": None, "hover": True}
        self.color = ColorAttribute(dataset, node_kws)
        self.size = SizeAttribute(dataset, node_kws)
        for key in node_kws:
            if key in self.kws:
                self.kws[key] = node_kws[key]


class LinkRectKws(DictKWS):
    def __init__(self, node_kws, dataset):
        super().__init__()
        self.kws = {
            "tooltip": None,
            "hover": True,
            "hover_rect_color": "#dbdbdb",
            "hover_text_color": "red",
        }
        self.color = ColorAttribute(dataset, node_kws)
        for key in node_kws:
            if key in self.kws:
                self.kws[key] = node_kws[key]


class LinkLineKws(DictKWS):
    def __init__(self, node_kws, dataset):
        super().__init__()
        self.kws = {"tooltip": None, "stroke_width": None, "hover": True}
        self.color = ColorAttribute(dataset, node_kws)
        for key in node_kws:
            if key in self.kws:
                self.kws[key] = node_kws[key]


class SizeAttribute:
    def __init__(self, dataset, node_kws) -> None:
        self.kws = {
            "size_attribute": None,
            "size_scale_type": "lineal",
            "size_default": None,
            "scale_domain_function": None,
            "scale_range_function": [2, 5],
        }
        for key in node_kws:
            if key in self.kws:
                self.kws[key] = node_kws[key]

        self.check_size(dataset)

    def check_size(self, dataset):
        node_kws = self.kws
        attr = node_kws["size_attribute"]
        size_d_extreme = node_kws["scale_domain_function"]
        if attr is None or node_kws["size_default"] is not None:
            return

        assert node_kws["size_scale_type"] in [
            "lineal",
            "pow",
            "sqrt",
            "log",
        ], "size_scale_type should be 'lineal', 'pow', 'sqrt' or 'log'"

        assert isinstance(
            node_kws["scale_range_function"], list
        ), "scale_range_function should be an array with integers or floats"

        for d in node_kws["scale_range_function"]:
            assert isinstance(
                d, (int, float)
            ), "Every element in scale_range_function should be int or float"

        for node in dataset["nodes"]:
            assert (
                attr in node
            ), "All nodes should contain the attribute defined in size_attribute"
            assert isinstance(
                node[attr], (int, float)
            ), "The attribute should be and integer or float"

        if size_d_extreme is not None:
            assert len(size_d_extreme) == len(
                node_kws["scale_range_function"]
            ), "scale_domain_function and scale_range_function should have the same lenght"
            for d in size_d_extreme:
                assert isinstance(
                    d, (int, float)
                ), "if scale_domain_function is not None, every element in scale_domain_function should be int or float"
        else:
            assert (
                len(node_kws["scale_range_function"]) == 2
            ), "if scale_domain_function is None, scale_range_function should be an array with 2 elements"


class ColorAttribute:
    def __init__(self, dataset, node_kws) -> None:
        self.kws = {
            "color_attribute": None,
            "color_attribute_type": "categorical",
            "color_scale_type": "lineal",  # Only for numerical
            "color_scheme": None,
            "color_domain_function": None,  # num: [min, max] - ord/cat: None or list of uniques values
            "color_default": None,
            "color_unknown": None,
        }
        for key in node_kws:
            if key in self.kws:
                self.kws[key] = node_kws[key]

        if self.kws["color_scheme"] is None:
            self.kws["color_scheme"] = (
                "Tableau10"
                if self.kws["color_attribute_type"] == "categorical"
                else "Blues"
            )

        self.check_color(dataset)

    def check_color(self, dataset):
        node_kws = self.kws
        if node_kws["color_attribute"] is None:
            return

        color_d_function = node_kws["color_domain_function"]
        if color_d_function is None:
            assert (
                node_kws["color_unknown"] is None
            ), "Only define color_unknown if you define color_domain_function"

        assert node_kws["color_attribute_type"] in [
            "numerical",
            "categorical",
            "ordinal",
        ], "size_scale_type should be 'numerical', 'categorical' or 'ordinal'"
        if node_kws["color_attribute_type"] == "numerical":
            assert node_kws["color_scale_type"] in [
                "lineal",
                "pow",
                "sqrt",
                "log",
            ], "color_scale_type should be 'lineal', 'pow', 'sqrt' or 'log'"
            assert node_kws["color_scheme"] in ORDERED_SCHEMES

            assert (
                color_d_function is None or len(color_d_function) == 2
            ), "If color_attribute_type is numerical, color_domain_function should be None or array with 2 element"

        elif node_kws["color_attribute_type"] == "categorical":
            assert node_kws["color_scheme"] in CATEGORICAL_SCHEMES

        else:  # node_kws["color_attribute_type"] == "ordinal":
            assert node_kws["color_scale_type"] in [
                "lineal",
                "pow",
                "sqrt",
                "log",
            ], "color_scale_type should be 'lineal', 'pow', 'sqrt' or 'log'"
            assert node_kws["color_scheme"] in ORDERED_SCHEMES

        for node in dataset["nodes"]:
            assert (
                node_kws["color_attribute"] in node
            ), "All nodes should contain the attribute defined in color_attribute"
