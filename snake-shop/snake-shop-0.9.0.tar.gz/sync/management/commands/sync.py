from django.core.management.base import BaseCommand
from ...models import Shop
from sync.utils import Syncer
from django.utils.timezone import now


class Command(BaseCommand):
    help = 'Sync full catalogue remote shops'
    sync_names = [
        # ProductClass related:
        'productclass',
        'attributeoptiongroup',
        'attributeoption',
        'productattribute',

        # Product related:
        'tax',
        'manufacturer',
        'product',
        'productattributevalue',
        'productattributevalue_value_multi_option',
        'productimage',

        # Category related:
        'category',
        'productcategory',
    ]

    def add_arguments(self, parser):
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument(
            '-a', '--all',
            help='Sync all connected remote shops.',
            action='store_true', dest='sync_all',
        )
        group.add_argument(
            '-d', '--domain',
            help='Sync connected shop by domain',
            action='store', dest='domain',
        )
        parser.add_argument(
            '-m', '--model',
            help='Sync defined only this model',
            action='store', dest='model_name',
        )

    def full_sync(self, shop):
        for sync_name in self.sync_names:
            self.sync_model(shop, sync_name)

    def sync_model(self, shop, model_name):
        Syncer(shop, model_name).sync()

    def handle(self, sync_all, domain, model_name, *args, **options):
        qs = Shop.objects.filter(enabled=True)
        if domain:
            qs = qs.filter(domain=domain)
            if not qs.exists():
                if Shop.objects.filter(enabled=False, domain=domain).exists():
                    print(domain + ' is sync disabled.')
                print(domain + ' doesn\'t exist.')
                return
        for shop in qs:
            print(f'{shop.domain} sync starts at {now()}')
            if model_name:
                self.sync_model(shop, model_name)
            else:
                self.full_sync(shop)
            print(f'{shop.domain} sync finished at {now()}')
