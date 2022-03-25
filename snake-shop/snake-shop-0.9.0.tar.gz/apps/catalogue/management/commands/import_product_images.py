import os
from django.core.management.base import BaseCommand
from apps.catalogue.models import Product, ProductImage
from ._file import File


class Command(BaseCommand):
    help = 'Import product images'

    def add_arguments(self, parser):
        parser.add_argument(
            '-i', '--input-dir',
            required=True, action='store', dest='input_dir', type=str,
        )
        parser.add_argument(
            '--fieldname',
            help='Fieldname to use as filename identifier',
            default='upc', required=False, action='store', dest='fieldname',
            type=str,
        )

    def handle(self, *args, **options):
        input_dir = options['input_dir']
        input_dir = input_dir if input_dir.endswith('/') else input_dir + '/'
        files = [File(input_dir + filename) for filename in 
                 sorted(os.listdir(options['input_dir']))]
        for file in files:
            query = {
                options['fieldname']: file.identifier,
            }
            qs = Product.objects.filter(**query).prefetch_related('images')
            for product in qs:
                if not product.images.all():
                    for i, product_image in enumerate(file.get_siblings(files)):
                        ProductImage.objects.create(
                            product=product,
                            original=product_image.get_django_file(),
                            display_order=i,
                        )
