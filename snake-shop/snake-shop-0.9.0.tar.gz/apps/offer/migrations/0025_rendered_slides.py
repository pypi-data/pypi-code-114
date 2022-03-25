from django.db import migrations, models
from django.core.files.images import ImageFile
from apps.offer.utils import InkscapeConverter
from apps.offer.models import RangeProduct


def map_value(value, min_from, max_from, min_to, max_to):
    value = float(''.join([x for x in value if x.isdigit() or x=='.']))
    return min_to + (max_to - min_to) * (
        (value - min_from) / (max_from - min_from))


def position_to_coordinates(apps, schema):
    SlidePriceLabelPosition = apps.get_model('offer', 'SlidePriceLabelPosition')
    for position in SlidePriceLabelPosition.objects.all():
        for range_product in position.range_products.all():
            range_product.top = map_value(position.top, 0, 100 - 30.7, 0, 100)
            range_product.left = map_value(position.left, 0, 100 - 24.1, 0, 100)
            range_product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0024_auto_20210530_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='rangeproduct',
            name='left',
            field=models.FloatField(blank=True, null=True, verbose_name='Left'),
        ),
        migrations.AddField(
            model_name='rangeproduct',
            name='top',
            field=models.FloatField(blank=True, null=True, verbose_name='Top'),
        ),
        migrations.AddField(
            model_name='rangeproduct',
            name='cached_slide',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='cached_slides/', verbose_name='Angebotsslider Bild'),
        ),
        migrations.AlterModelOptions(
            name='rangeproduct',
            options={'ordering': ['-display_order']},
        ),
        migrations.RunPython(position_to_coordinates, migrations.RunPython.noop),
    ]
