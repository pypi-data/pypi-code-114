from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.models import Permission
from oscar.apps.dashboard.partners import forms as base_forms
from apps.partner.models import Partner


class PartnerAddressForm(base_forms.PartnerAddressForm):
    def clean(self):
        """
        raise Validation error if
        - default partner not exists and posted not default
        - default partner would be changed
        """
        if Partner.default:
            if self.instance.partner.name == Partner.default_name:
                raise ValidationError({
                    'name': _('Do not rename the default partner')
                })
        else:
            if self.cleaned_data['name'] != Partner.default_name:
                raise ValidationError({
                    'name': _('Create default partner first')
                })
        return super().clean()

    class Meta(base_forms.PartnerAddressForm.Meta):
        fields = ('name',)


ROLE_CHOICES = [
    *base_forms.ROLE_CHOICES, ['no_access', _('No dashboard access')]
]


class PermissionMixin(forms.Form):
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect,
                         label=_('User role'))

    def get_initial_for_field(self, field, field_name):
        if field_name == 'role':
            return self.get_current_role()
        return base_forms.ExistingUserForm.get_initial_for_field(self, field, field_name)

    def get_current_role(self):
        if not self.instance.pk:
            return 'no_access'

        user = self.instance
        dashboard_perm = Permission.objects.get(
            codename='dashboard_access', content_type__app_label='partner')
        user_has_perm = user.user_permissions.filter(
            pk=dashboard_perm.pk).exists()

        if user.is_staff or user.is_superuser:
            return 'staff'
        if user_has_perm:
            return 'limited'
        return 'no_access'

    def save(self):
        user = super().save()
        role = self.cleaned_data.get('role', 'none')
        dashboard_perm = Permission.objects.get(
            codename='dashboard_access', content_type__app_label='partner')
        if role == 'no_access' and not user.is_staff and not user.is_superuser:
            user.user_permissions.remove(dashboard_perm)
        return user


class NewUserForm(PermissionMixin, base_forms.NewUserForm):
    pass


class ExistingUserForm(PermissionMixin, base_forms.ExistingUserForm):
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1', '')
        password2 = self.cleaned_data.get('password2', '')

        if password1 and password2:
            return super().clean_password2()
