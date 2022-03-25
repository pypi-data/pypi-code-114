from django.core.management.base import BaseCommand
from oscar.core.loading import get_model, get_class
from django.http.request import HttpRequest
from ...utils import InkscapeConverter
from ...models import RangeProduct


class Command(BaseCommand):
    help = 'Refresh all rendered slider images of active slides'

    def handle(self, *args, **options):
        slides = RangeProduct.objects.filter(image__isnull=False)
        InkscapeConverter.refresh_slides(slides)
