import csv
import io
from django.contrib import admin
from django.utils.html import format_html
from django import forms
from django.shortcuts import redirect, render
from django.urls.conf import path
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from oscar.core.loading import get_model

WishList = get_model('wishlists', 'WishList')
Line = get_model('wishlists', 'Line')
Product = get_model('catalogue', 'Product')
Tag = get_model('custom', 'Tag')
UserAddress = get_model('address', 'UserAddress')
User = get_user_model()


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class WishlistImportMixin(admin.ModelAdmin):
    change_list_template = "admin/wishlists/change_list.html"
    # actions = ["export_csv"]
    csv_field_titles = (
        'email_oder_kdnr',
        'listenname',
        'art_nr',
        'menge_optional',
    )
    csv_fields = (
        'wishlist__owner__email',
        'wishlist__name',
        'product__upc',
        'quantity',
    )

    def export_csv(self, request, queryset):
        response = HttpResponse(
            content_type='text/csv',
            headers={
                'Content-Disposition': \
                'attachment; filename="wishlist_lines_export.csv"'
            },
        )
        csv_writer = csv.writer(response, delimiter=';')
        csv_writer.writerow(self.csv_field_titles)
        for wishlist in queryset:
            for line in wishlist.lines.values_list(*self.csv_fields):
                csv_writer.writerow(line)

        return response
    export_csv.short_description = "Erstelle CSV"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv, name='wishlist-csv-import'),
        ]
        return my_urls + urls

    def _get_user(self, email_or_customer_id):
        user = User.objects.filter(email=email_or_customer_id).first()
        if user:
            return user

        allowed_chars = '0123456789'
        customer_id = email_or_customer_id
        customer_id = ''.join([x for x in customer_id if x in allowed_chars])

        user = User.objects.filter(addresses__sage_id=int(customer_id)).first()
        if user:
            return user

        user = User.objects.filter(addresses__id=customer_id).first()
        if user:
            return user

    def import_csv_row(self, row, objects):
        email_or_customer_id, wishlist_name, upc, quantity = row
        if not quantity:
            quantity = 1

        user = self._get_user(email_or_customer_id)
        if not user:
            objects['users_not_found'].append(email_or_customer_id)
            return

        product = Product.objects.filter(upc=upc).first()
        if not product:
            objects['products_not_found'].append(upc)
            return

        wishlist, wishlist_created = WishList.objects.get_or_create(
            owner=user,
            name=wishlist_name,
            defaults={
                'visibility': 'Private',
            }
        )
        if wishlist_created:
            objects['wishlists_created'].append(wishlist)

        line, line_created = Line.objects.get_or_create(
            wishlist=wishlist,
            product=product,
            defaults={
                'title': product.title,
                'quantity': quantity,
            }
        )
        if line_created:
            objects['lines_created'].append(line)

    def import_csv(self, request):
        objects = {
            'users_not_found': [],
            'products_not_found': [],
            'wishlists_created': [],
            'lines_created': [],
        }
        if request.method == "POST":
            csv_file = io.StringIO(request.FILES["csv_file"].read().decode())
            csv_reader = csv.reader(csv_file, delimiter=';')
            line_num = 0
            for row in csv_reader:
                if line_num > 0:
                    self.import_csv_row(row, objects)
                line_num += 1
            self.message_user(request, objects)
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "admin/wishlists/csv_form.html", payload
        )


class WishListLineAdmin(admin.TabularInline):
    model = Line
    extra = 0


class WishListAdmin(WishlistImportMixin, admin.ModelAdmin):
    inlines = [WishListLineAdmin]
    model = WishList
    list_display = ['owner', 'name', 'date_created', 'products']
    search_fields = ['owner__email', 'name', ]

    def products(self, wishlist):
        result = ''
        for line in wishlist.lines.all():
            title = getattr(line.product, 'title', line.title)
            result += f'{title}<br>'
        return format_html(result)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related(
            'lines', 'lines__product')


admin.site.register(WishList, WishListAdmin)
