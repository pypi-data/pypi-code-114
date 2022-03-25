import os
from shutil import copy2
from django.core.management.base import BaseCommand
from apps.catalogue.models import Category


class Command(BaseCommand):
    help = 'Export category images'
    missing_product_images = []
    missing_category_images = []

    def add_arguments(self, parser):
        parser.add_argument(
            '-o', '--output-dir',
            required=True, action='store', dest='output_dir', type=str,
        )

    def handle(self, *args, **options):
        os.makedirs(options['output_dir'], exist_ok=True)

        for category in Category.objects.all():
            if category.image and os.path.isfile(category.image.path):
                dest_path = '{}/{}.{}'.format(
                    options['output_dir'],
                    category.slug,
                    category.image.path.split('.')[-1],
                )
                copy2(category.image.path, dest_path)
