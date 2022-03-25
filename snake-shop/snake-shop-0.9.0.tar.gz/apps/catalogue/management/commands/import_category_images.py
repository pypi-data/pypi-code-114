import os
from django.core.management.base import BaseCommand
from apps.catalogue.models import Category
from ._file import File


class Command(BaseCommand):
    help = 'Import category images'

    def add_arguments(self, parser):
        parser.add_argument(
            '-i', '--input-dir',
            required=True, action='store', dest='input_dir', type=str,
        )
        parser.add_argument(
            '--fieldname',
            help='Fieldname to use as filename identifier',
            default='slug', required=False, action='store', dest='fieldname',
            type=str,
        )

    def handle(self, *args, **options):
        input_dir = options['input_dir']
        input_dir = input_dir if input_dir.endswith('/') else input_dir + '/'
        files = [File(input_dir + filename) for filename in
                 sorted(os.listdir(options['input_dir']))]
        for category in Category.objects.filter(image__isnull=True):
            for file in files:
                identifier = getattr(category, options['fieldname'])
                if file.identifier == identifier:
                    category.image = file.get_django_file()
                    category.save()
