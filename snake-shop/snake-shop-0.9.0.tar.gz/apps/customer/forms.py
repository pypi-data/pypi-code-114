from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UsernameField
from oscar.apps.customer import forms as base_forms
from oscar.core.compat import existing_user_fields


class UserForm(base_forms.UserForm):
    newsletter_accepted = forms.BooleanField(
        label=_('Newsletter accepted'),
        required=False,
    )

    def get_initial_for_field(self, field, field_name):
        if field_name == 'newsletter_accepted':
            return self.instance.newsletter_accepted
        return super().get_initial_for_field(field, field_name)

    def save(self, commit=True):
        newsletter_accepted = self.cleaned_data['newsletter_accepted']
        self.instance.newsletter_accepted = newsletter_accepted
        return super().save(commit=commit)

    class Meta(base_forms.UserForm.Meta):
        fields = existing_user_fields(
            ['first_name', 'last_name', 'email']
            # , 'birth_date'
        )


class EmailAuthenticationForm(base_forms.EmailAuthenticationForm):
    username = UsernameField(
        label='E-Mail Adresse / Benutzername',
        widget=forms.TextInput(attrs={'autofocus': True}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


ProfileForm = UserForm
