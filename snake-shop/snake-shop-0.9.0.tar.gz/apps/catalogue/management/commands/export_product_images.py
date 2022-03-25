import os
from shutil import copy2
from django.core.management.base import BaseCommand
from apps.catalogue.models import Product


class Command(BaseCommand):
    help = 'Export product images'
    missing_product_images = []
    missing_category_images = []

    def add_arguments(self, parser):
        parser.add_argument(
            '-o', '--output-dir',
            required=True, action='store', dest='output_dir', type=str,
        )

    def handle(self, *args, **options):
        os.makedirs(options['output_dir'], exist_ok=True)

        for product in Product.objects.all().prefetch_related('images'):
            images = list(product.images.all())
            for i, image in enumerate(images):
                image = image.original
                dest_path = '{}/{}_{}.{}'.format(
                    options['output_dir'],
                    product.upc,
                    i + 1,
                    image.path.split('.')[-1],
                )
                if os.path.isfile(image.path):
                    copy2(image.path, dest_path)
                else:
                    self.missing_product_images.append(image)
