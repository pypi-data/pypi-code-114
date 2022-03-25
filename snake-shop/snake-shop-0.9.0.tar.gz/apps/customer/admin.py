from django.contrib import admin, auth

from apps.payment import models as payment_models
from apps.partner import models as partner_models
from .models import UserPaymentSelection

User = auth.get_user_model()


class UserPaymentSelectionInline(admin.TabularInline):
    model = UserPaymentSelection
    fk_name = 'user'
    fields = ('user', 'cash', 'transfer', 'account', 'sepa', 'reason')
    extra = 0

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class UserBankAccountInLine(admin.TabularInline):
    model = payment_models.Bankcard
    fields = ('name', 'number')
    extra = 0


class UserPartnerInLine(admin.TabularInline):
    model = partner_models.Partner.users.through
    extra = 0


class UserAdmin(auth.admin.UserAdmin):
    inlines = [UserPaymentSelectionInline, UserBankAccountInLine, UserPartnerInLine]
    list_display = ('email', 'is_staff', 'payment_selection')
    ordering = list_display


class UserPaymentSelectionModelAdmin(admin.ModelAdmin):
    fields = ('user', 'cash', 'transfer', 'account', 'sepa', 'reason')
    list_display = ('user', 'cash', 'transfer', 'account', 'sepa', 'reason', 'date_updated')
    ordering = list_display
    list_filter = ('cash', 'transfer', 'account', 'sepa',)
    search_fields = ('user__id', 'user__email', 'user__first_name', 'user__last_name',)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
admin.site.register(UserPaymentSelection, UserPaymentSelectionModelAdmin)
