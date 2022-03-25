import csv
from decimal import Decimal as D
from django.core.management.base import BaseCommand
from oscar.core.loading import get_model
from typing import List
from _collections import OrderedDict

Partner = get_model('partner', 'Partner')
StockRecord = get_model('partner', 'StockRecord')

Product = get_model('catalogue', 'Product')
Category = get_model('catalogue', 'Category')
Tax = get_model('catalogue', 'Tax')
Tag = get_model('custom', 'Tag')
ProductClass = get_model('catalogue', 'ProductClass')
ProductCategory = get_model('catalogue', 'ProductCategory')

ProductAttribute = get_model('catalogue', 'ProductAttribute')
AttributeOption = get_model('catalogue', 'AttributeOption')
ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')


class Table:
    def __init__(self, fieldnames: List, products):
        self.objects = self.get_objects(fieldnames)
        self.fieldnames = self.objects.keys()
        self.head = self.fieldnames
        self.products = products
        self.columns = list(self.get_columns(self.objects))
        self.rows = self.get_rows(self.columns, self.products)

    def get_objects(self, fieldnames):
        """
        This makes the decision which fieldname is valid and shown in the table
        """
        objects = OrderedDict()
        product = Product.objects.first()
        attributes = {x.code: x for x in ProductAttribute.objects.all()}
        for fieldname in fieldnames:
            if hasattr(product, fieldname):
                objects[fieldname] = None
            elif fieldname in attributes:
                objects[fieldname] = attributes[fieldname]
        return objects

    def get_rows(self, columns, products):
        for product in products:
            yield Row(columns, product)

    def get_columns(self, objects):
        for fieldname in objects.keys():
            yield Column(fieldname, objects[fieldname])


class Column:
    def __init__(self, fieldname, obj):
        self.fieldname = fieldname
        self.obj = obj

    def __str__(self):
        return self.fieldname


class Row:
    def __init__(self, columns, product):
        self.columns = columns
        self.product = product
        self.cells = self.get_cells()
        self.values = self.get_values()

    def get_cells(self):
        for column in self.columns:
            yield Cell(self, column)

    def get_values(self):
        for cell in self.cells:
            yield cell.value

    def __str__(self):
        return str(self.product)


class Cell:
    def __init__(self, row, column):
        self.column = column
        self.row = row
        self.value = self.get_value()

    def get_value(self):
        obj = self.column.obj
        product = self.row.product
        fieldname = self.column.fieldname
        if isinstance(obj, ProductAttribute):
            for attribute_value in product.attribute_values.all():
                if attribute_value.attribute == obj:
                    if obj and obj.type == 'multi_option':
                        values = [x.option for x in
                                  attribute_value.value_multi_option.all()]
                        return ','.join(values)
                    return str(attribute_value.value)
            return ''
        return str(getattr(product, fieldname))

    def __str__(self):
        return str(self.value)


class Command(BaseCommand):
    help = 'Export products to csv'
    default_fieldnames = ('title,upc,deposit,volume,weight,container_count,'
                          'has_box,category,product_class,brand,reusable,'
                          'vessel,bio,tax,is_public,price,special_price')

    def add_arguments(self, parser):
        parser.add_argument(
            '-o', '--output-file',
            required=True, action='store', dest='output_file', type=str,)
        parser.add_argument(
            '--fieldnames',
            help='Comma separated fieldnames to use as filename identifier',
            required=False, action='store', dest='fieldnames', type=str,)

    def get_fieldnames(self, fieldnames=None, **options):
        if fieldnames:
            field_str = fieldnames
        else:
            field_str = self.default_fieldnames
        return field_str.split(',')

    def get_product_qs(self):
        qs = Product.objects.all()
        qs = qs.select_related('tax')
        qs = qs.prefetch_related(
            'categories', 'attribute_values', 'tax', 'manufacturer')
        qs = qs.order_by('title')
        return qs

    def handle(self, **options):
        table = Table(self.get_fieldnames(**options), self.get_product_qs())
        with open(options['output_file'], 'w') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(table.head)
            for row in table.rows:
                values = list(row.values)
                writer.writerow(values)
        return 
