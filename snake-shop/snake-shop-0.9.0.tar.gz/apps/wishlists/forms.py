from django import forms
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from oscar.apps.wishlists import forms as base_forms
from apps.partner.strategy import Selector


class WishListControlForm(forms.Form):
    choices = [
        ('position', _('Eigene sortierung')),
        ('product__title', _('Produkt Titel A-Z')),
        ('-product__title', _('Produkt Titel Z-A')),
    ]
    sort_by = forms.ChoiceField(label=_('Sortieren nach'), choices=choices)


class WishListLineForm(base_forms.WishListLineForm):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

        index = int(self.prefix.split('-')[1])
        self.fields['quantity'].widget.attrs['tabindex'] = index + 100

        self.fields['quantity'].widget.attrs['class'] = 'input-mini'
        self.fields['quantity'].widget.attrs['type'] = 'submit'

        product_id = getattr(self.instance.product, 'id', None)
        self.fields['quantity'].widget.attrs['data-product-id'] = product_id

    def get_initial_for_field(self, field, field_name):
        if field_name == 'quantity':
            product = self.instance.product
            basket = self.request.basket
            quantity = basket.product_quantity(product)
            field.widget.attrs['data-previous'] = quantity
            return quantity
        return super().get_initial_for_field(field, field_name)

    def process_basket_replacement(self, product, quantity):
        basket_qty = self.request.basket.product_quantity(product)

        updated = quantity and basket_qty
        if updated:
            self.request.basket.lines.filter(product=product).update(
                quantity=quantity
            )

        added = quantity and not basket_qty
        if added:
            self.request.basket.add_product(product, quantity=quantity)

        deleted = basket_qty and not quantity
        if deleted:
            self.request.basket.lines.filter(product=product).delete()

        noop = quantity == basket_qty
        if noop:
            action = ''
        elif updated:
            action = 'angepasst'
        elif added:
            action = 'hinzugefügt'
        elif deleted:
            action = 'entfernt'

        msg_method = {
            'hinzugefügt': messages.success,
            'angepasst': messages.warning,
            'entfernt': messages.error,
        }.get(action)

        if action:
            msg = 'Warenkorb Position {} für {}.'.format(action, product.title)
            msg_method(self.request, msg)

    def save(self, **kwargs):  # pylint: disable=arguments-differ
        product = self.cleaned_data['id'].product
        product_id = int(self.request.POST['product_id'])
        quantity = self.cleaned_data['quantity']
        # Avoid running on all products when submitting:
        if product and product.id == product_id and product.is_public:
            strategy = Selector().strategy(self.request)
            is_buyable = strategy.select_stockrecord(product)
            if is_buyable and product.is_public:
                self.process_basket_replacement(product, quantity)
            else:
                messages.error(
                    self.request,
                    'Derzeit nicht verfügbar: '+ product.title,
                )
                super().save(**kwargs)
