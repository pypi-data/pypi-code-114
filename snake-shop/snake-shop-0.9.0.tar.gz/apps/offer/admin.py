from django.utils.translation import gettext_lazy as _
from oscar.apps.offer.admin import *  # noqa
from .models import RangeProduct


class RangeProductAdminProxy(RangeProduct):

    class Meta:
        proxy = True
        verbose_name = _('Special prices and display option')
        verbose_name_plural = _('Special prices and display options')


class RangeProductAdmin(admin.ModelAdmin):
    model = RangeProductAdminProxy
    list_display = (
        'id',
        'display_order',
        'product',
        'special_price',
        'image',
        'link',
        'top',
        'left',
        'main_title',
        'title',
        'sub_title',
        'special_price_start',
        'special_price_end',
    )
    list_filter = (
        'range__benefit__offers',
        'range',
    )


admin.site.register(RangeProductAdminProxy, RangeProductAdmin)
