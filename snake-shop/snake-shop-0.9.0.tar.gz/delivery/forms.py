from django.utils.translation import gettext_lazy as _
from django import forms

from .models import Postcode
from django.core.validators import MinValueValidator, MaxValueValidator


class ChoosePostcodeForm(forms.Form):
    postcode = forms.MultipleChoiceField(
        widget=forms.Select,
        label=_('Choose your postcode for free delivery:'),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['postcode'].widget.attrs['onchange'] = 'this.form.submit()'
        self.fields['postcode'].choices = [
            (postcode.postcode, postcode.postcode)
            for postcode in Postcode.objects.all()
        ]


class PostcodeCheckerInputForm(forms.Form):
    postcode = forms.IntegerField(
        label=_("Post/Zip-code"),
        min_value=10000, max_value=99999,
    )
    def __init__(self, request, *args, **kwargs):
        if request.method == 'POST':
            super().__init__(request.POST, *args, **kwargs)
        else:
            super().__init__(request.GET, *args, **kwargs)
            self.fields['postcode'].widget.attrs['placeholder'] = 'PLZ eingeben'
