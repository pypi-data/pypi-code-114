import csv
from collections import defaultdict
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.models import Q
from user.models import OrganizationUnit

User = get_user_model()


class Command(BaseCommand):
    help = 'Import CSV with columns [Sage Customer Number, Manager_email]'
    default_fieldnames = 'customer_id,manager_email'

    def add_arguments(self, parser):
        parser.add_argument(
            '-i', '--input-file',
            required=True, action='store', dest='input_file', type=str,
        )
        parser.add_argument(
            '--fieldnames',
            help='Comma separated fieldnames to use as filename identifier',
            required=False, action='store', dest='fieldnames',
            type=str, default=self.default_fieldnames,
        )

    @staticmethod
    def iterate_file(file, fieldnames):
        with open(file) as csv_file:
            csv_reader = csv.DictReader(
                csv_file, delimiter=';', fieldnames=fieldnames
            )
            for row in csv_reader:
                yield row

    def handle(self, input_file, fieldnames, *args, **options):
        fieldnames = fieldnames.split(',')
        manager_dict = defaultdict(list)

        for row in self.iterate_file(input_file, fieldnames):
            manager_email = row['manager_email']
            customer_id = row['customer_id']
            if manager_email and customer_id:
                manager_dict[manager_email].append(int(customer_id[1:]))
        self.to_objects(manager_dict)

    def to_objects(self, manager_dict):
        manager_objects = {}
        for manager_email, customer_ids in manager_dict.items():
            manager = User.objects.get(email=manager_email)
            customers = User.objects.filter(
                Q(email__in=manager_email)
                | Q(addresses__sage_id__in=customer_ids)
            )
            manager_objects[manager] = customers
        self.create_ous(manager_objects)

    def create_ous(self, manager_objects):
        for manager, customers in manager_objects.items():
            organization_unit = OrganizationUnit.objects.get_or_create(
                name=manager.email
            )[0]
            organization_unit.members.add(manager)
            organization_unit.customers.set(customers)
