from django.contrib import admin
from oscarapi.models import ApiKey
from .models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ['domain', 'schema', 'sync_delete', 'get_key']
    list_filter = ['sync_delete', 'schema']
    search_fields = ['domain', 'products__id', 'products__title', 'key__key']

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields['key'].label_from_instance = \
            lambda x: "{}".format(x.key)
        return form

    @admin.display(description='API Key')
    def get_key(self, obj):
        return getattr(obj.key, 'key', '-')


class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ['key', 'shop']
    search_fields = ['key']
    readonly_fields = ['shop']


admin.site.unregister(ApiKey)
admin.site.register(ApiKey, ApiKeyAdmin)
admin.site.register(Shop, ShopAdmin)
