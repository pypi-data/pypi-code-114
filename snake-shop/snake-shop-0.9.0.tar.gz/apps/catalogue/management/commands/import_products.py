import csv
from decimal import Decimal as D
from pathlib import Path
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction
from django.contrib.sites.models import Site
from oscar.core.loading import get_model
from custom.lib import clean
from apps.communication.utils import CustomDispatcher
from apps.catalogue.models import Manufacturer

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


PRODUCT_ATTRIBUTES = {
    'vessel': ProductAttribute.objects.get(code='vessel'),
}

TAXES = {
    19: Tax.objects.get(rate=19),
    7: Tax.objects.get(rate=7),
    None: Tax.objects.get(rate=19),
}


class Command(BaseCommand):
    help = 'Import products from csv'
    default_fieldnames = ('title,upc,deposit,volume,weight,container_count,'
                          'price,tax,has_box,category,product_class,'
                          'brand,reusable,vessel,is_public')

    directory_mode = False

    def add_arguments(self, parser):
        parser.add_argument(
            '-i', '--input-file', '--input-path',
            required=True, action='store', dest='input_path', type=str,
        )
        parser.add_argument(
            '-f', '--force',
            help='Overwrite existing products',
            action='store_true', dest='force',
        )
        parser.add_argument(
            '-z', '--zero-prices',
            help='Creates StockRecord if there is no Price, too.',
            action='store_true', dest='zero_prices',
        )
        parser.add_argument(
            '-m', '--move-imported',
            help='Moved files to imported directory in directory mode.',
            action='store_true', dest='move_imported',
        )
        parser.add_argument(
            '-t', '--tag',
            help='Set a tag with this name for all created objects',
            default='', action='store', dest='tag',
        )
        parser.add_argument(
            '-b', '--base-url',
            help='Base url to send status email after successfully imported.',
            required=False, action='store', dest='base_url',
        )
        parser.add_argument(
            '--reset',
            help='Deletes products before recreating',
            action='store_true', dest='reset',
        )
        parser.add_argument(
            '-p', '--partner',
            help='Overwrite existing products',
            default='default', action='store', dest='partner',
        )
        parser.add_argument(
            '--fieldnames',
            help='Comma separated fieldnames to use as filename identifier',
            required=False, action='store', dest='fieldnames',
            type=str,
        )

    def get_fieldnames(self, fieldnames, **options):
        field_str = fieldnames or self.default_fieldnames
        return field_str.split(',')

    def get_input_file(self, input_path, **options):
        if '/' not in input_path:
            input_path = f'{settings.BASE_DIR}/{input_path}'
        input_path = Path(input_path)
        files = [input_path]
        if input_path.is_dir():
            self.directory_mode = True
            input_path.joinpath('imported').mkdir(exist_ok=True)
            files = []
            for child in input_path.iterdir():
                if str(child).endswith('.csv') and child.is_file():
                    files.append(child)
        return files

    def get_tag(self, file, tag, **options):
        tag = tag or file.name
        tag_obj = Tag.objects.filter(name=tag).first()
        if not tag_obj:
            tag_obj = Tag.objects.create(name=tag)
        return tag_obj

    def iterate_file(self, file, fieldnames):
        with open(file, encoding='cp1252') as csv_file:
            csv_reader = csv.DictReader(
                csv_file, delimiter=';', fieldnames=fieldnames
            )
            line_count = 0
            for row in csv_reader:
                yield row
                line_count +=1

    def execute_reset(self, upcs):
        Product.objects.filter(upc__in=upcs).delete()

    @transaction.atomic
    def handle(self, reset, *args, **options):
        files = self.get_input_file(**options)
        fieldnames = self.get_fieldnames(**options)
        objects = []

        for file in files:
            rows_iterator = self.iterate_file(file, fieldnames)

            if reset:
                upcs = []
                for row in rows_iterator:
                    upcs.append(row['upc'])
                self.execute_reset(upcs)

            rows = []
            for row in rows_iterator:
                row['partner'] = options['partner']
                row['tag'] = self.get_tag(file, **options)
                row['zero_prices'] = options['zero_prices']
                rows.append(Row(objects, **dict(row)))

        if self.directory_mode and options['move_imported']:
            for file in files:
                new_path = file.parent.joinpath('imported').joinpath(file.name)
                file.rename(new_path)

        if options.get('base_url') and objects:
            context = {
                'base_url': options['base_url'],
                'objects': objects,
                'files': files,
            }
            site = Site.objects.get_current()
            CustomDispatcher(
                'OBJECTS_IMPORTED', site, extra_context=context).send()


class Row:
    def __init__(self, objects, zero_prices,  force=False, **row):
        self.zero_prices = zero_prices
        self.force = force
        self.product, self.product_created = self.get_product(**row)
        self.partners = self.get_partner(**row)

        if self.product_created:
            self.stockrecord = self.get_stockrecord(**row)
            self.category = self.get_category(**row)
            self.product_category = self.get_product_category(**row)
            self.vessel = self.get_attr('vessel', **row)
            objects.append(self.product)

    def get_attr(self, field, **row):
        if not row[field]:
            return
        options = PRODUCT_ATTRIBUTES[field].option_group.options
        field_value = {
            'Glas': 'Glasflasche',
        }.get(row[field], row[field])
        attribute_option = options.get(option=field_value)
        if self.force:
            return ProductAttributeValue.objects.update_or_create(
                attribute=PRODUCT_ATTRIBUTES[field],
                product=self.product,
                defaults={'value_option': attribute_option},
            )
        return ProductAttributeValue.objects.get_or_create(
            attribute=PRODUCT_ATTRIBUTES[field],
            product=self.product,
            defaults={'value_option': attribute_option},
        )

    def get_product_class(self, product_class):
        replace = {
            'Getraenke': 'Getränke',
        }
        for key, value in replace.items():
            product_class = product_class.replace(key, value)
        return ProductClass.objects.get(name=product_class)

    def get_manufacturer(self, brand):
        if not brand:
            return None
        return Manufacturer.objects.get_or_create(name=brand)[0]

    def get_reusability(self, reusable):
        return {
            'EINWEG': 0,
            'MEHRWEG': 1,
        }.get(reusable, None)

    def get_product(self, title, upc, deposit, volume, weight, container_count,
                    has_box, tax, product_class, is_public, tag, brand,
                    reusable, **row):
        has_box_choices = {
            'Falsch': False,
            'Wahr': True,
        }
        kwargs = {
            'title': title.strip(),
            'upc': upc,
            'deposit': clean(deposit, D) if deposit else None,
            'volume': clean(volume, D) if volume else None,
            'weight': clean(weight, D) if weight else None,
            'container_count': container_count,
            'has_box': has_box_choices.get(has_box, None),
            'tax': TAXES[int(tax)] if tax else TAXES[None],
            'product_class': self.get_product_class(product_class),
            'is_public': clean(is_public, bool),
            'manufacturer': self.get_manufacturer(brand),
            'reusability': self.get_reusability(reusable),
        }
        if self.force:
            product, created = Product.objects.update_or_create(
                upc=upc,
                defaults=kwargs,
            )
        else:
            product, created = Product.objects.get_or_create(
                upc=upc,
                defaults=kwargs,
            )
        if created and tag:
            product.tags.add(tag)
        return product, created

    def get_category(self, category, **row):
        category_obj = Category.objects.filter(name=category).first()
        if not category_obj:
            category = {
                'Getraenke': 'getranke',
            }.get(category, category)
            category_obj = Category.objects.get(slug=category)
        return category_obj

    def get_product_category(self, **row):
        if self.force:
            return ProductCategory.objects.update_or_create(
                product=self.product,
                category=self.category
            )[0]
        else:
            return ProductCategory.objects.get_or_create(
                product=self.product,
                category=self.category
            )[0]

    def get_partner(self, partner, **row):
        partners = partner.split(',')
        return Partner.objects.filter(code__in=partners)

    def get_stockrecord(self, upc, price, **row):
        stockrecords = []
        if not int(price) and not self.zero_prices:
            return None
        for partner in self.partners:
            kwargs = {
                'product': self.product,
                'partner': partner,
                'partner_sku': upc,
                'price': D(price.replace(',', '.')),
            }
            if self.force:
                stockrecords.append(StockRecord.objects.update_or_create(
                    partner=partner, partner_sku=upc, defaults=kwargs,
                )[0])
            else:
                stockrecords.append(StockRecord.objects.get_or_create(
                    partner=partner, partner_sku=upc, defaults=kwargs,
                )[0])
        return stockrecords
