from django.contrib import admin
from .models import Tour, DeliveryTime, TourBlocklist, GlobalBlocklist, Postcode, Delivery


class DeliveryTimeInline(admin.TabularInline):
    model = DeliveryTime
    extra = 0


class TourBlocklistInline(admin.TabularInline):
    model = TourBlocklist
    extra = 0


class PostcodeInLine(admin.StackedInline):
    model = Tour.postcodes.through  # @UndefinedVariable
    extra = 1


class TourAdmin(admin.ModelAdmin):
    inlines = [PostcodeInLine, DeliveryTimeInline, TourBlocklistInline, ]
    exclude = ('postcodes', )


admin.site.register(Tour, TourAdmin)
admin.site.register(GlobalBlocklist)
admin.site.register(Postcode)
admin.site.register(Delivery)
