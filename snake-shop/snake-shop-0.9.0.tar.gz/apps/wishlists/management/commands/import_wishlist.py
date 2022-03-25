"""
Select or create user and add a address to it
"""
import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from oscar.core.loading import get_model

WishList = get_model('wishlists', 'WishList')
Line = get_model('wishlists', 'Line')
Product = get_model('catalogue', 'Product')
Tag = get_model('custom', 'Tag')
UserAddress = get_model('address', 'UserAddress')
User = get_user_model()


not_found_users = []
not_found_products = []


class Command(BaseCommand):
    help = 'Import wishlist lines from csv'
    default_fieldnames = ('customer_id,upc')

    def add_arguments(self, parser):
        parser.add_argument(
            '-i', '--input-file',
            required=True, action='store', dest='input_file', type=str,
        )
        parser.add_argument(
            '--fieldnames',
            help='Comma separated fieldnames to use as filename identifier',
            required=False, action='store', dest='fieldnames',
            type=str,
        ),
        parser.add_argument(
            '-n', '--wishlist-name',
            help='Name of the wishlist to import into',
            default='Standard', action='store', dest='wishlist_name', type=str,
        ),
        parser.add_argument(
            '-t', '--tag-name',
            help='Name of the tag to tag the created objects',
            required=True, action='store', dest='tag_name', type=str,
        ),

    def get_fieldnames(self, fieldnames, **options):
        field_str = fieldnames or self.default_fieldnames
        return field_str.split(',')

    @staticmethod
    def get_input_file(input_file, **options):
        if '/' in input_file:
            return input_file

        path = str(settings.BASE_DIR)
        return f'{path}/{input_file}'

    def iterate_file(self, file, fieldnames):
        with open(file, encoding='cp1252') as csv_file:
            csv_reader = csv.DictReader(
                csv_file, delimiter=';', fieldnames=fieldnames
            )
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    yield row
                line_count +=1

    def print_result(self):
        result = f"""
        ### Users not found: ###
        {not_found_users}
        ### /Users not found ###
        
        
        \n\n### Products not found: ###
        {not_found_products}
        ### /Products not found ###
        """
        print(result)
        return result

    def get_tag(self, tag_name):
        return Tag.objects.get_or_create(name=tag_name)[0]

    def handle(self, *args, **options):
        file = self.get_input_file(**options)
        fieldnames = self.get_fieldnames(**options)
        rows_iterator = self.iterate_file(file, fieldnames)
        wishlist_name = options['wishlist_name']
        tag = self.get_tag(options['tag_name'])

        rows = []
        counter = 0
        for row in rows_iterator:
            row = dict(row)
            if None in row:
                row.pop(None)
            rows.append(Row(wishlist_name, tag, **row))
            counter += 1
            if not counter % 1000:
                print(f'{counter} objects done.')
        print('\n')
        tag.description = self.print_result()
        tag.save()


class Row:
    def __init__(self, wishlist_name, tag, **row):
        self.row = row
        self.tag = tag
        self.wishlist_name = wishlist_name
        self.user_address = self.get_user_address()
        self.product = self.get_product()
        if self.user_address and self.product:
            self.user = self.get_user()
            self.wishlist = self.get_wishlist()
            self.wishlist_line = self.get_wishlist_line()
        elif not self.user_address:
            if row['customer_id'] not in not_found_users:
                not_found_users.append(row['customer_id'])
        elif not self.product:
            if row['upc'] not in not_found_products:
                not_found_products.append(row['upc'])

    def get_customer_id(self):
        allowed_chars = '0123456789'
        customer_id = self.row['customer_id']
        customer_id = ''.join([x for x in customer_id if x in allowed_chars])
        return int(customer_id)

    def get_user_address(self):
        customer_id = self.get_customer_id()
        user_address = UserAddress.objects.filter(sage_id=customer_id)
        if not user_address:
            user_address = UserAddress.objects.filter(id=customer_id)
        return user_address.first()

    def get_user(self):
        return self.user_address.user

    def get_product(self):
        return Product.objects.filter(upc=self.row['upc']).first()

    def get_wishlist(self):
        wishlist, created = WishList.objects.get_or_create(
            name=self.wishlist_name,
            owner=self.user,
        )
        if created:
            wishlist.tags.add(self.tag)
        return wishlist

    def get_wishlist_line(self):
        line, created = Line.objects.get_or_create(
            wishlist=self.wishlist,
            product=self.product,
            defaults={
                'title': self.product.title,
                'quantity': 1,
            }
        )
        if created:
            line.tags.add(self.tag)
        return line
