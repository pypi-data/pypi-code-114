from reportlab.lib import colors

from pyametista.engine.bands.elements import process_graphic_element, process_report_element
from pyametista.engine.commonutilities import add_attr2attributes
from pyametista.engine.components.line import line_style_dict


def draw_rectangle(report, attributes, line_style, line_width, fore_color, background_color, fill):
    """
    Draw a rectangle on report_info.
    :param attributes:
    :param line_style:
    :param line_width:
    :param fore_color:
    :param background_color:
    :param fill:
    """
    # global report_info

    report["canvas"].saveState()

    report["canvas"].setDash(line_style_dict.get(line_style, (1)))
    report["canvas"].setLineWidth(line_width)
    if fore_color is not None:
        report["canvas"].setStrokeColor(colors.HexColor(fore_color))
    if background_color is not None:
        report["canvas"].setFillColor(colors.HexColor(background_color))
    if attributes.get("radius") is None:
        report["canvas"].rect(
            attributes["x"],
            report["cur_y"] - attributes["y"] - attributes["height"],
            attributes["width"],
            attributes["height"],
            fill=fill,
        )
    else:
        report["canvas"].roundRect(
            attributes["x"],
            report["cur_y"] - attributes["y"] - attributes["height"],
            attributes["width"],
            attributes["height"],
            radius=attributes.get("radius"),
            fill=fill,
        )

    report["canvas"].restoreState()


def process_rectangle(report, element):
    """
    Process jrxml "rectangle" element.
    :param report:
    :param element:
    :return:
    """
    # global report_info

    rectangle_element = element.get("child")
    if rectangle_element is not None:
        attributes = process_report_element(
            report, rectangle_element[0].get("reportElement")
        )  # get reportElement
        # get radius attribute on rectangle element
        add_attr2attributes(element, attributes)

        # set attributes from following graphicElement
        attributes = process_graphic_element(report, rectangle_element, attributes)

        # set line attributes
        line_style = attributes.get("lineStyle")
        line_width = float(attributes.get("lineWidth", "1.0"))
        fore_color = attributes.get("forecolor")
        background_color = attributes.get("backcolor")

        fill = 0
        if background_color is not None:
            fill = 1

        # draw rectangle
        if (
            line_style == "Double"
        ):  # double line consists of wide solid line with thin white line in between
            draw_rectangle(
                report,
                attributes,
                line_style_dict["Solid"],
                line_width * 1.5,
                fore_color,
                background_color,
                fill,
            )
            draw_rectangle(
                report,
                attributes,
                line_style_dict["Solid"],
                line_width * 0.3,
                "#FFFFFF",
                background_color,
                fill,
            )
        else:
            draw_rectangle(
                report, attributes, line_style, line_width, fore_color, background_color, fill
            )


def draw_ellipse(report, attributes, line_style, line_width, fore_color, background_color, fill):
    """
    Draw an ellipse on report_info.
    :param report:
    :param attributes:
    :param line_style:
    :param line_width:
    :param fore_color:
    :param background_color:
    :param fill:
    :return:
    """
    # global report_info

    report["canvas"].saveState()

    report["canvas"].setDash(line_style_dict.get(line_style, (1)))
    report["canvas"].setLineWidth(line_width)
    if fore_color is not None:
        report["canvas"].setStrokeColor(colors.HexColor(fore_color))
    if background_color is not None:
        report["canvas"].setFillColor(colors.HexColor(background_color))
    # ellipse(cx, cy, rx, ry, stroke=1, fill=0)
    report["canvas"].ellipse(
        attributes["x"],
        report["cur_y"] - attributes["y"],
        attributes["x"] + attributes["width"],
        report["cur_y"] - attributes["y"] - attributes["height"],
        fill=fill,
    )
    report["canvas"].restoreState()


def process_ellipse(report, element):
    """
    Process jrxml 'ellipse' element
    :param report:.
    :param element:
    """
    # global report_info

    ellipse_element = element.get("child")
    if ellipse_element is not None:
        report_element = process_report_element(
            report, ellipse_element[0].get("reportElement")
        )  # get reportElement

        # set attributes from following graphicElement
        report_element = process_graphic_element(report, ellipse_element, report_element)

        # set line attributes
        line_style = report_element.get("lineStyle")
        line_width = float(report_element.get("lineWidth", "1.0"))
        fore_color = report_element.get("forecolor")
        background_color = report_element.get("backcolor")

        fill = 0
        if background_color is not None:
            fill = 1

        # draw ellipse
        if (
            line_style == "Double"
        ):  # double line consists of wide solid line with thin white line in between
            draw_ellipse(
                report,
                report_element,
                line_style_dict["Solid"],
                line_width * 1.0,
                fore_color,
                background_color,
                fill,
            )
            draw_ellipse(
                report,
                report_element,
                line_style_dict["Solid"],
                line_width * 0.5,
                "#FFFFFF",
                background_color,
                fill,
            )
        else:
            draw_ellipse(
                report, report_element, line_style, line_width, fore_color, background_color, fill
            )


def draw_circle(report, attributes, line_style, line_width, fore_color, background_color, fill):
    """
    Draw an circle.
    :param report:
    :param attributes:
    :param line_style:
    :param line_width:
    :param fore_color:
    :param background_color:
    :param fill:
    :return:
    """
    # global report_info

    report["canvas"].saveState()

    report["canvas"].setDash(line_style_dict.get(line_style, (1)))
    report["canvas"].setLineWidth(line_width)
    if fore_color is not None:
        report["canvas"].setStrokeColor(colors.HexColor(fore_color))
    if background_color is not None:
        report["canvas"].setFillColor(colors.HexColor(background_color))
    # circle(cx, cy, r, stroke=1, fill=0)
    radius = min(attributes["width"], attributes["height"]) / 2
    report["canvas"].circle(
        attributes["x"] + radius, report["cur_y"] - attributes["y"] - radius, radius, fill=fill
    )
    report["canvas"].restoreState()


def process_circle(report, element):
    """
    Process jrxml 'ellipse' element.
    :param element:
    """
    # global report_info

    ellipse_element = element.get("child")
    if ellipse_element is not None:
        report_element = process_report_element(
            report, ellipse_element[0].get("reportElement")
        )  # get reportElement

        # set attributes from following graphicElement
        report_element = process_graphic_element(report, ellipse_element, report_element)

        # set line attributes
        line_style = report_element.get("lineStyle")
        line_width = float(report_element.get("lineWidth", "1.0"))
        fore_color = report_element.get("forecolor")
        background_color = report_element.get("backcolor")

        fill = 0
        if background_color is not None:
            fill = 1

        # draw ellipse
        if (
            line_style == "Double"
        ):  # double line consists of wide solid line with thin white line in between
            draw_circle(
                report,
                report_element,
                line_style_dict["Solid"],
                line_width * 1.0,
                fore_color,
                background_color,
                fill,
            )
            draw_circle(
                report,
                report_element,
                line_style_dict["Solid"],
                line_width * 0.5,
                "#FFFFFF",
                background_color,
                fill,
            )
        else:
            draw_circle(
                report, report_element, line_style, line_width, fore_color, background_color, fill
            )
