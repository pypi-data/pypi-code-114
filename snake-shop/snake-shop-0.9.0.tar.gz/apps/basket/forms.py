from django import forms
from django.conf import settings
from django.db.models import Sum
from django.forms.utils import ErrorDict
from django.utils.translation import gettext_lazy as _

from oscar.core.loading import get_model
from oscar.forms import widgets
from oscar.apps.basket.forms import AddToBasketForm
Line = get_model('basket', 'line')
Basket = get_model('basket', 'basket')
Option = get_model('catalogue', 'option')
Product = get_model('catalogue', 'product')


class AddToBasketForm(AddToBasketForm):

    def __init__(self, basket, product, *args, **kwargs):
        super().__init__(basket, product, *args, **kwargs)
        self.fields['quantity'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['onclick'] = '$(this).select();'
