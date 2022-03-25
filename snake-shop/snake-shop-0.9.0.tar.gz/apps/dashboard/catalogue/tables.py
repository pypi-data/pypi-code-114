from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext_lazy
from django_tables2 import A, Column, LinkColumn, TemplateColumn

from oscar.core.loading import get_class, get_model

DashboardTable = get_class('dashboard.tables', 'DashboardTable')
Product = get_model('catalogue', 'Product')
Category = get_model('catalogue', 'Category')
AttributeOptionGroup = get_model('catalogue', 'AttributeOptionGroup')
Option = get_model('catalogue', 'Option')


class ProductTable(DashboardTable):
    title = TemplateColumn(
        verbose_name=_('Title'),
        template_name='oscar/dashboard/catalogue/product_row_title.html',
        order_by='title', accessor=A('title'))
    image = TemplateColumn(
        verbose_name=_('Image'),
        template_name='oscar/dashboard/catalogue/product_row_image.html',
        orderable=False)
    product_class = Column(
        verbose_name=_('Product type'),
        accessor=A('product_class'),
        order_by='product_class__name')
    variants = TemplateColumn(
        verbose_name=_("Variants"),
        template_name='oscar/dashboard/catalogue/product_row_variants.html',
        orderable=False
    )
    packaging = TemplateColumn(
        verbose_name=_('Packaging'),
        template_name='oscar/dashboard/catalogue/product_row_packaging.html',
        orderable=False
    )
    tax = TemplateColumn(
        verbose_name=_('Tax'),
        template_name='oscar/dashboard/catalogue/product_row_tax.html',
    )
    actions = TemplateColumn(
        verbose_name=_('Actions'),
        template_name='oscar/dashboard/catalogue/product_row_actions.html',
        orderable=False)

    icon = 'fas fa-sitemap'

    class Meta(DashboardTable.Meta):
        model = Product
        fields = ('upc', 'is_public', 'date_updated',)
        sequence = ('title', 'upc', 'image', 'product_class', 'variants',
                    '...', 'is_public', 'date_updated', 'actions')
        order_by = '-date_updated'
