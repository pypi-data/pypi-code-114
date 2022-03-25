import io
import csv
from decimal import Decimal as D
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.http.response import HttpResponse
from django.urls.conf import path
from django import forms
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.contrib import messages
from oscar.apps.catalogue.admin import ProductAdmin as BaseProductAdmin
from apps.partner.models import StockRecord, Partner
from .models import Product, Manufacturer


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class ImportAction:
    CREATE, DELETE, UPDATE = 'create', 'delete', 'update'

    def __init__(self, action_type, partner_name, row):
        self.action_type = action_type
        self.partner_name = partner_name
        self.row = row
        self.product = row.db_product
        self.old_value = row.db_prices.get(partner_name)
        self.new_value = row.row_prices.get(partner_name)

    def process(self):
        {
            self.CREATE: self.create,
            self.DELETE: self.delete,
            self.UPDATE: self.update,
        }[self.action_type]()

    def create(self):
        partner = Partner.objects.get(name=self.partner_name)
        StockRecord.objects.create(
            product=self.product,
            price=self.new_value,
            partner=partner,
            partner_sku=self.product.upc,
        )

    def delete(self):
        StockRecord.objects.filter(
            product=self.product,
            price=self.old_value,
            partner__name=self.partner_name,
        ).delete()

    def update(self):
        qs = StockRecord.objects.filter(
            product=self.product,
            partner__name=self.partner_name,
            price=self.old_value,
        )
        for stock_record in qs:
            stock_record.price = self.new_value
            stock_record.partner_sku = self.product.upc
            stock_record.save()


class ProductPriceImportRow:
    def __init__(self, row, db_product, partners):
        self.partner_columns = partners
        self.base_columns = row.keys() - self.partner_columns
        self.row = row
        self.db_product = db_product
        self.actions = self.calculate_diff()

    @property
    def pending(self):
        return self.actions

    def process(self):
        for action in self.actions:
            action.process()

    @property
    def db_prices(self):
        db_prices = {}
        qs = self.db_product.stockrecords.all()  # not evaluating
        db_stockrecords = {x.partner.name: x.price for x in qs}
        for fieldname in self.partner_columns:
            db_prices[fieldname] = db_stockrecords.get(fieldname, None)
        return db_prices

    @property
    def row_prices(self):
        row_prices = {}
        for fieldname in self.partner_columns:
            price = self.row.get(fieldname, None)
            price = D(price.replace(',', '.')) if price else None
            row_prices[fieldname] = price
        return row_prices

    def calculate_diff(self):
        actions = []
        for key, value in self.row_prices.items():
            if self.db_prices[key] != value:
                if value is None:
                    action_type =ImportAction.DELETE
                elif self.db_prices[key] is None:
                    action_type = ImportAction.CREATE
                else:
                    action_type = ImportAction.UPDATE
                actions.append(ImportAction(action_type, key, self))
        return actions

    def __str__(self):
        return self.row['upc']


class ProductPricesExImportMixin(admin.ModelAdmin):
    change_list_template = "admin/products/change_list.html"
    actions = ['export_product_prices']
    csv_field_titles = ['upc', 'title', 'category__name']
    csv_encoding = 'cp1252'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                'product-price-csv/',
                self.import_csv,
                name='product-price-csv-import'
            ),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == 'POST':
            file = request.FILES["csv_file"].read().decode(self.csv_encoding)
            csv_file = io.StringIO(file)
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            qs = Product.objects.all().prefetch_related(  # @UndefinedVariable
                'stockrecords',
                'stockrecords__partner',
            )
            db_products = {x.upc.lstrip('0'): x for x in qs}
            pending_changes = []
            products_not_found = []
            partner_qs = Partner.objects.all().order_by('priority')
            partners = [partner.name for partner in partner_qs]
            for row in csv_reader:
                try:
                    db_product = db_products[row['upc']]
                except KeyError:
                    products_not_found.append(row['upc'])
                    continue
                imported_row = ProductPriceImportRow(row, db_product, partners)
                if imported_row.pending:
                    pending_changes.append(imported_row)
            msg_template_name = 'admin/products/imported_prices_msg.html'
            context = {
                'pending_changes': pending_changes,
                'products_not_found': products_not_found,
            }
            for change in pending_changes:
                change.process()
            msg = get_template(msg_template_name).render(context).strip()
            self.message_user(request, mark_safe(msg))
            if products_not_found:
                msg = f'Products not found: {", ".join(products_not_found)}'
                messages.warning(request, msg)
            return redirect("..")

        form = CsvImportForm(request.POST or None)
        context = {"form": form}
        return render(
            request, "admin/products/csv_form.html", context
        )

    def export_product_prices(self, request, qs):
        response = HttpResponse(
            content_type='text/csv; charset=' + self.csv_encoding,
            headers={
                'Content-Disposition': \
                'attachment; filename="product_prices_export.csv"'
            },
        )
        partner_names = qs.order_by(
            'stockrecords__partner__priority'
        ).distinct(
            'stockrecords__partner__priority'
        ).values_list(
            'stockrecords__partner__name', flat=True
        )
        qs = qs.prefetch_related(
            'stockrecords',
            'stockrecords__partner',
            'productcategory_set',
            'productcategory_set__category',
        ).order_by('title')

        csv_writer = csv.writer(response, delimiter=';')
        csv_writer.writerow(self.csv_field_titles + list(partner_names))
        for product in qs:
            values = [product.upc, product.title]
            values.append(self._extract_category_name(product))
            sr_qs = product.stockrecords.all()
            for partner_name in partner_names:
                # Select the correct Stockrecord to avoid n+1
                values.append(
                    self._extract_stockrecord_price(sr_qs, partner_name)
                )
            csv_writer.writerow(values)
        return response
    export_product_prices.short_description = _('Preis Export')

    @staticmethod
    def _extract_stockrecord_price(qs, partner_name):
        for stockrecord in qs:
            if stockrecord.partner.name == partner_name \
                    and isinstance(stockrecord.price, D):
                return str(stockrecord.price).replace('.', ',')
        return ''

    @staticmethod
    def _extract_category_name(product):
        for product_category in product.productcategory_set.all():
            return product_category.category.name


class StockrecordInLine(admin.TabularInline):
    model = StockRecord
    extra = 0
    fields = ('partner', 'partner_sku', 'price')


class ProductAdmin(ProductPricesExImportMixin, BaseProductAdmin):
    inlines = BaseProductAdmin.inlines + [StockrecordInLine]
    list_filter = BaseProductAdmin.list_filter + [
        'stockrecords__partner__site__domain']


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'url']
    fields = ['name', 'address', 'url', 'logo']


admin.site.unregister(Product)
admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
