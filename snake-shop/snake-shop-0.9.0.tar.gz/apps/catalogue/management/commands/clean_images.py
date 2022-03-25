from pathlib import Path
from PIL import Image
from django.core.management.base import BaseCommand
from oscar.core.loading import get_model

ProductImage = get_model('catalogue', 'ProductImage')


class Command(BaseCommand):
    help = 'Save images as new images without exiv data (icc ...)'

    def handle(self, *args, **options):
        for image in ProductImage.objects.all():
            path = Path(image.original.path)
            if path.is_file():
                image = Image.open(str(path))
                # next 3 lines strip exif
                data = list(image.getdata())
                image_without_exif = Image.new(image.mode, image.size)
                image_without_exif.putdata(data)
                image_without_exif.save(str(path))
