from django.db import models


class PartnerAddressManager(models.Manager):
    def get_primary(self, partner):
        try:
            return self.get(partner=partner, primary=True)
        except self.model.DoesNotExist:
            return None
