from oscar.apps.offer import applicator


class Applicator(applicator.Applicator):
    def get_offers(self, basket, user=None, request=None):
        assert request.site
        offers = super().get_offers(basket, user=user, request=request)
        return [x for x in offers if x.partner in request.partners]
