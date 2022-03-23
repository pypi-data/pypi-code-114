from polymorphic.managers import PolymorphicManager


class ProductManager(PolymorphicManager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.select_related("unit")

    def get_by_natural_key(self, inner_id):
        return self.get(inner_id=inner_id)

    def get_spareparts(self):
        return self.get_queryset().filter(is_spareparts=True)

    def get_stockable(self):
        return self.get_queryset().filter(is_stockable=True)

    def can_be_purchased(self):
        return self.get_queryset().filter(can_be_purchased=True)

    def can_be_sold(self):
        return self.get_queryset().filter(can_be_sold=True)

    def get_available(self):
        return self.get_queryset().filter(status="Available")
