import io
import subprocess
from base64 import b64encode
from django.core.files.images import ImageFile
from django.template.loader import get_template


class InkscapeTemplate:
    name = 'oscar/offer/slide.svg'
    top, right, bottom, left = 0, 150, 100, 0

    def __init__(self, left_max, top_max):
        assert left_max and top_max
        # X-Axis:
        self.left_max = left_max
        self.width = self.right - self.left
        self.relative_width = self.left_max - self.left
        self.label_width = self.width - self.relative_width
        self.label_width_ratio = self.label_width / self.width
        self.width_ratio = self.relative_width / self.width
        # Y-Axis:
        self.top_max = top_max
        self.height = self.bottom - self.top
        self.relative_height = self.top_max - self.top
        self.label_height = self.height - self.relative_height
        self.label_height_ratio = self.label_height / self.height
        self.height_ratio = self.relative_height / self.height

    def map_top(self, top_value):
        return self.map_value(top_value, 0, 100, self.top, self.top_max)

    def map_left(self, left_value):
        return self.map_value(left_value, 0, 100, self.left, self.left_max)

    @staticmethod
    def map_value(value, min_from, max_from, min_to, max_to):
        return min_to + (max_to - min_to) * (
            (value - min_from) / (max_from - min_from))


default_inkscape_template = InkscapeTemplate(115.29759, 70.83931)
subtitled_inkscape_template = InkscapeTemplate(115.29759, 67.216797)


class InkscapeTemplate:
    name = 'oscar/offer/slide.svg'
    top, right, bottom, left = 0, 150, 100, 0

    def __init__(self, left_max, top_max):
        assert left_max and top_max
        # X-Axis:
        self.left_max = left_max
        self.width = self.right - self.left
        self.relative_width = self.left_max - self.left
        self.label_width = self.width - self.relative_width
        self.label_width_ratio = self.label_width / self.width
        self.width_ratio = self.relative_width / self.width
        # Y-Axis:
        self.top_max = top_max
        self.height = self.bottom - self.top
        self.relative_height = self.top_max - self.top
        self.label_height = self.height - self.relative_height
        self.label_height_ratio = self.label_height / self.height
        self.height_ratio = self.relative_height / self.height

    def map_top(self, top_value):
        return self.map_value(top_value, 0, 100, self.top, self.top_max)

    def map_left(self, left_value):
        return self.map_value(left_value, 0, 100, self.left, self.left_max)

    @staticmethod
    def map_value(value, min_from, max_from, min_to, max_to):
        return min_to + (max_to - min_to) * (
            (value - min_from) / (max_from - min_from))


default_inkscape_template = InkscapeTemplate(115.29759, 70.83931)
subtitled_inkscape_template = InkscapeTemplate(115.29759, 67.216797)


class InkscapeConverter:
    """
    Width is in px from outside and units from inside the converter
    """
    binary_path = '/usr/bin/inkscape'

    def __init__(self, range_product, suffix, width=None):
        self.template = subtitled_inkscape_template if range_product.sub_title \
            else default_inkscape_template

        self.range_product = range_product
        self.site = range_product.range.site
        self.suffix = suffix
        self.filename = f'{ self.range_product.pk }.{ suffix }'
        self.width_px = width or self.range_product.image.width  # 800
        self.height_px = self._get_height(width)  # 533

    def _get_height(self, width):
        if width and self.range_product.image:
            return self.range_product.image.height / (
                self.range_product.image.width / width)
        return self.range_product.image.height

    def _get_params(self):
        return [
            self.binary_path,
            '--without-gui',
            '--pipe',
            '--export-plain-svg',
            '--export-type=png',
        ]

    def _get_context_data(self, range_product):
        context = {
            'range_product': range_product,
            'slide': range_product.slide,
            'label': getattr(range_product.slide, 'label', None),
            'width': self.width_px,
            'height': self.height_px,
            'width_px': self.width_px,
            'height_px': self.height_px,
            'background_image': self.background_image,
            'logo_square': self.logo_square,
        }
        if range_product.has_label:
            context.update({
                'top': str(self.template.map_top(range_product.top)),
                'left': str(self.template.map_left(range_product.left)),
            })
        return context

    @property
    def background_image(self):
        return b64encode(self.range_product.image.file.read()).decode()

    @property
    def logo_square(self):
        file = self.site.configuration.logo_square.file
        return b64encode(file.read()).decode()

    @property
    def svg(self):
        context = self._get_context_data(self.range_product)
        svg = get_template(self.template.name).render(context).strip()
        return io.BytesIO(svg.encode())

    @property
    def png(self):
        proc = subprocess.run(
            self._get_params(),
            check=True,
            input=self.svg.read(),
            capture_output=True,
        )
        return io.BytesIO(proc.stdout)

    @property
    def base64(self):
        return b64encode(self.png.read()).decode()

    @property
    def file(self):
        return getattr(self, self.suffix)

    @classmethod
    def refresh_slides(cls, range_product_iterable):
        for range_product in range_product_iterable:
            converter = cls(range_product, 'png')
            image = ImageFile(converter.file, converter.filename)
            range_product.cached_slide = image
            range_product.save()
