from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.aggregates import Max
from oscar.apps.wishlists import abstract_models


class Line(abstract_models.AbstractLine):
    position = models.PositiveIntegerField(
        _('Position'),
        help_text=_('Position innerhalb der Liste'),)

    def save(self, **kwargs):
        if not self.position:
            next_position = self.wishlist.lines.aggregate(Max('position')
                                          ).get('position__max') or 0 + 1
            self.position = next_position
        super().save(**kwargs)

    class Meta:
        ordering = ['position', 'pk']
        app_label = 'wishlists'
        unique_together = (('wishlist', 'product'),)
        verbose_name = _('Orderlistenposition')
        verbose_name_plural = _('Orderlistenpositionen')


class WishList(abstract_models.AbstractWishList):
    def add(self, product, as_first=False):
        lines = self.lines.filter(product=product)
        if len(lines) == 0:
            if as_first:
                updated_lines = []
                for line in self.lines.all():
                    line.position += 1
                    updated_lines.append(line)
                Line.objects.bulk_update(updated_lines, ['position'])

            self.lines.create(
                product=product,
                title=product.get_title(),
                position = 1 if as_first else None  # is set in save
            )

    class Meta:
        app_label = 'wishlists'
        ordering = ('owner', 'date_created', )
        verbose_name = _('Orderliste')
        verbose_name_plural = _('Orderlisten')


from oscar.apps.wishlists.models import *  # noqa isort:skip
