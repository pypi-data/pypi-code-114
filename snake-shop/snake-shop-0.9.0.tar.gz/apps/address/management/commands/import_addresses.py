"""
Select or create user and add a address to it
"""
import csv
from decimal import Decimal as D
from django.core.management.base import BaseCommand
from django.conf import settings
from oscar.core.loading import get_model
from django.contrib.auth import get_user_model
from apps.partner.models import Partner
from django.contrib.auth.models import UserManager
from datetime import date
from oscar.apps.customer.utils import CustomerDispatcher, get_password_reset_url
from django.contrib.sites.models import Site

Tag = get_model('custom', 'Tag')
UserAddress = get_model('address', 'UserAddress')
User = get_user_model()

PARTNERS = {partner.code: partner for partner in Partner.objects.all()}
created_users = []
not_created_users = []
not_created_addresses = []


class Command(BaseCommand):
    help = 'Import users and address from csv'
    default_fieldnames = ('username,first_name,last_name,email,birth_date,'
                          'title,addr_first_name,addr_last_name,str,ort,'
                          'postcode,phone,company,sage_id,is_company,'
                          'cost_center,floor_number,bla')
    tag = None

    def add_arguments(self, parser):
        parser.add_argument(
            '-i', '--input-file',
            required=True, action='store', dest='input_file', type=str,
        )
        parser.add_argument(
            '-p', '--partner',
            help='Add user to Partner',
            action='store', dest='partner', type=str,
        )
        parser.add_argument(
            '-u', '--url',
            help='Send registration emails to this email address, doesnt send '
                'if not set',
            action='store', dest='url', type=str,
        )
        parser.add_argument(
            '--fieldnames',
            help='Comma separated fieldnames to use as filename identifier',
            required=False, action='store', dest='fieldnames',
            type=str,
        )
        parser.add_argument(
            '-t', '--tag',
            help='Set a tag with this name for all created objects',
            default='', action='store', dest='tag',
        )

    def get_partner_code(self, row, options):
        return options.get('partner', None) or row.get('partner')

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
                csv_file,
                delimiter=';',
                fieldnames=fieldnames,
            )
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    yield row
                line_count +=1

    def get_tag(self, tag, **options):
        return Tag.objects.get_or_create(name=tag)[0]

    def print_result(self):
        result = f"""
        ### Users not Created: ###
        {not_created_users}
        ### /Users not Created ###
        
        #############################

        ### Addresses not Created: ###
        {not_created_addresses}
        ### /Addresses not Created ###
        """
        self.tag.description = result
        self.tag.save()
        print('\n\n### Users Created: ###\n')
        for username, password, reset_url, reset_url_html in created_users:
            print('Username: ' + username)
            print('Password: ' + password)
        print('### /Users Created ###\n\n')

    def handle(self, *args, **options):
        file = self.get_input_file(**options)
        fieldnames = self.get_fieldnames(**options)
        rows_iterator = self.iterate_file(file, fieldnames)
        self.tag = self.get_tag(**options)

        rows = []
        for row in rows_iterator:
            row = dict(row)
            row['partner'] = self.get_partner_code(row, options)
            row['admin_email'] = options.get('admin_email', None)
            row['url'] = options['url']
            row['tag'] = self.tag
            rows.append(Row(**row))
        print('\n')
        print(created_users)
        self.print_result()


class Row:
    def __init__(self, url, tag, force=False, admin_email=None, **row):
        self.row = row
        self.tag = tag
        self.url = url
        self.force = force
        self.partner = self.get_partner()
        self.user = self.get_user()
        self.useraddress = self.get_useraddress()

    @staticmethod
    def clean(element, data_type=str):
        if data_type is str:
            result = data_type(element.strip())
        elif data_type is date:
            result = date(data_type) if element else None
        elif data_type is int:
            element = ''.join(
                [char for char in element if char in '0123456789']
            )
            result = int(element) if element is 0 or element else None
        elif data_type is bool:
            result = bool(element)
        return result

    @staticmethod
    def make_password():
        return UserManager().make_random_password()

    def get_partner(self):
        return PARTNERS[self.row['partner']]

    def get_user(self):
        row, clean = self.row, self.clean
        password = self.make_password()
        user, created = User.objects.get_or_create(
            email=clean(row['email']),
            defaults={
                #'password': password,
                'username': clean(row['username']),
                'first_name': clean(row['first_name']),
                'last_name': clean(row['last_name']),
                'birth_date': clean(row['birth_date'], date),
            }
        )
        user.partners.add(self.partner)
        if created:
            user.set_password(password)
            user.save()
            url_prefix = self.url or ''
            reset_url = url_prefix + get_password_reset_url(user)
            reset_url_html = f'<a href="{reset_url}">{reset_url}</a>'
            print(user.email, password, reset_url, reset_url_html)
            created_users.append(
                [user.email, password, reset_url, reset_url_html]
            )
            self.tag.users.add(user)
        else:
            not_created_users.append(row['email'])
        return user

    def get_useraddress(self):
        row, clean = self.row, self.clean
        useraddress, created = UserAddress.objects.get_or_create(
            user=self.user,
            defaults={
                'title': clean(row['title']),
                'first_name': clean(row['addr_first_name']),
                'last_name': clean(row['addr_last_name']),
                'line1': clean(row['str']),
                'line4': clean(row['ort']),
                'postcode': clean(row['postcode'], int) or 1,
                'phone_number': clean(row['phone']),
                'company': clean(row['company']),
                'sage_id': clean(row['sage_id'], int),
                'is_company': clean(row['is_company'], bool),
                'cost_center': clean(row['cost_center']),
                'floor_number': clean(row['floor_number'], int),
            }
        )

        if created:
            self.tag.addresses.add(useraddress)
        else:
            not_created_addresses.append(row['email'])
        return useraddress
