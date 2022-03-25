from apps.partner.models import Partner
from textwrap import wrap


class Slide:
    def __init__(self, range_product):
        self.range_product = range_product
        self.product = range_product.product
        self.label = self.get_label()

    @property
    def is_valid(self):
        return self.range_product.has_slide

    @property
    def image(self):
        return self.range_product.image

    @property
    def link(self):
        if self.range_product.link:
            return self.range_product.link
        elif self.product:
            return self.product.get_absolute_url()

    def get_label(self):
        label = Label(self.range_product)
        if self.is_valid and label.is_valid:
            return label


class Label:
    """ Price Label class """
    LINE_CHARS = 22

    def __init__(self, range_product):
        self.range_product = range_product
        self.product = range_product.product

    @property
    def is_valid(self):
        return bool(self.range_product.top is not None
                    and self.range_product.left is not None)

    @property
    def css(self):
        return self.range_product.price_position.css

    @property
    def title(self):
        if self.range_product.title:
            return self.range_product.title
        elif self.product:
            return self.product.title or ''
        return ''

    @property
    def lines(self):
        if '<br>' in self.title:
            lines = self.title.split('<br>')
        else:
            lines = wrap(self.title, self.LINE_CHARS)
        if len(lines) == 0:
            lines = ['', '', '']
        elif len(lines) == 1:
            lines = ['', *lines, '']
        elif len(lines) == 2:
            lines = [*lines, '']
        return lines

    @property
    def lines_count(self):
        return len([x for x in self.lines if x])

    @property
    def line1(self):
        return self.lines[0]

    @property
    def line2(self):
        return self.lines[1]

    @property
    def line3(self):
        return self.lines[2]

    @property
    def base_price(self):
        if self.product:
            site = self.range_product.range.site
            stockrecord = self.product.stockrecords.filter(
                partner__code=Partner.default_code,
                partner__site=site,
            ).first()
            if stockrecord:
                return stockrecord.price
        return None

    @property
    def price(self):
        return self.range_product.special_price or self.base_price

    @property
    def tax_included(self):
        return True

    @property
    def deposit(self):
        if self.product:
            return self.product.deposit
