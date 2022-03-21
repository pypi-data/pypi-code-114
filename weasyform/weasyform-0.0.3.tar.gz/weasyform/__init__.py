import math
from weasyprint import HTML as WPHTML
from weasyprint.document import DocumentMetadata, Matrix, rectangle_aabb, Document as WPDocument, Page as WPPage
from weasyprint.text.fonts import FontConfiguration
from weasyprint.css.counters import CounterStyle
from weasyprint.formatting_structure.build import build_formatting_structure
from weasyprint.layout import layout_document
from weasyprint.layout.percent import percentage
from weasyprint.html import get_html_metadata
from weasyprint.formatting_structure import boxes


class Page(WPPage):
    def __init__(self, page_box):
        self.form_elements = []
        super(Page, self).__init__(page_box)

    def _gather_links_and_bookmarks(self, box, parent_matrix=None):

        # Get box transformation matrix.
        # "Transforms apply to block-level and atomic inline-level elements,
        #  but do not apply to elements which may be split into
        #  multiple inline-level boxes."
        # http://www.w3.org/TR/css3-2d-transforms/#introduction
        if box.style['transform'] and not isinstance(box, boxes.InlineBox):
            border_width = box.border_width()
            border_height = box.border_height()
            origin_x, origin_y = box.style['transform_origin']
            offset_x = percentage(origin_x, border_width)
            offset_y = percentage(origin_y, border_height)
            origin_x = box.border_box_x() + offset_x
            origin_y = box.border_box_y() + offset_y

            matrix = Matrix(e=origin_x, f=origin_y)
            for name, args in box.style['transform']:
                a, b, c, d, e, f = 1, 0, 0, 1, 0, 0
                if name == 'scale':
                    a, d = args
                elif name == 'rotate':
                    a = d = math.cos(args)
                    b = math.sin(args)
                    c = -b
                elif name == 'translate':
                    e = percentage(args[0], border_width)
                    f = percentage(args[1], border_height)
                elif name == 'skew':
                    b, c = math.tan(args[1]), math.tan(args[0])
                else:
                    assert name == 'matrix'
                    a, b, c, d, e, f = args
                matrix = Matrix(a, b, c, d, e, f) @ matrix
            box.transformation_matrix = (
                    Matrix(e=-origin_x, f=-origin_y) @ matrix)
            if parent_matrix:
                matrix = box.transformation_matrix @ parent_matrix
            else:
                matrix = box.transformation_matrix
        else:
            matrix = parent_matrix

        bookmark_label = box.bookmark_label
        if box.style['bookmark_level'] == 'none':
            bookmark_level = None
        else:
            bookmark_level = box.style['bookmark_level']
        state = box.style['bookmark_state']
        link = box.style['link']
        anchor_name = box.style['anchor']
        has_bookmark = bookmark_label and bookmark_level
        # 'link' is inherited but redundant on text boxes
        has_link = link and not isinstance(box, (boxes.TextBox, boxes.LineBox))
        # In case of duplicate IDs, only the first is an anchor.
        has_anchor = anchor_name and anchor_name not in self.anchors

        has_form_element = box.element_tag in ['input']

        if has_bookmark or has_link or has_anchor or has_form_element:
            pos_x, pos_y, width, height = box.hit_area()
            if has_link:
                token_type, link = link
                assert token_type == 'url'
                link_type, target = link
                assert isinstance(target, str)
                if link_type == 'external' and box.is_attachment:
                    link_type = 'attachment'
                if matrix:
                    link = (
                        link_type, target,
                        rectangle_aabb(matrix, pos_x, pos_y, width, height),
                        box.download_name)
                else:
                    link = (
                        link_type, target,
                        (pos_x, pos_y, pos_x + width, pos_y + height),
                        box.download_name)
                self.links.append(link)
            if matrix and (has_bookmark or has_anchor):
                pos_x, pos_y = matrix.transform_point(pos_x, pos_y)
            if has_bookmark:
                self.bookmarks.append(
                    (bookmark_level, bookmark_label, (pos_x, pos_y), state))
            if has_anchor:
                self.anchors[anchor_name] = pos_x, pos_y

            if has_form_element:
                element_type = box.element.attrib.get('type')
                name = box.element.attrib.get('name')
                self.form_elements.append((
                    element_type,
                    name,
                    rectangle_aabb(matrix, pos_x, pos_y, width, height) if matrix else (pos_x, pos_y, pos_x + width, pos_y + height)
                ))

        for child in box.all_children():
            self._gather_links_and_bookmarks(child, matrix)


class Document(WPDocument):
    @classmethod
    def _render(cls, html, stylesheets, presentational_hints=False,
                optimize_size=('fonts',), font_config=None, counter_style=None,
                image_cache=None):
        if font_config is None:
            font_config = FontConfiguration()

        if counter_style is None:
            counter_style = CounterStyle()

        context = cls._build_layout_context(
            html, stylesheets, presentational_hints, optimize_size,
            font_config, counter_style, image_cache)

        root_box = build_formatting_structure(
            html.etree_element, context.style_for, context.get_image_from_uri,
            html.base_url, context.target_collector, counter_style,
            context.footnotes)

        page_boxes = layout_document(html, root_box, context)
        rendering = cls(
            [Page(page_box) for page_box in page_boxes],
            DocumentMetadata(**get_html_metadata(html)),
            html.url_fetcher, font_config, optimize_size)
        return rendering


class HTML(WPHTML):
    def render(self, stylesheets=None, presentational_hints=False,
               optimize_size=('fonts',), font_config=None, counter_style=None,
               image_cache=None):

        return Document._render(
            self, stylesheets, presentational_hints,
            optimize_size, font_config, counter_style, image_cache)
