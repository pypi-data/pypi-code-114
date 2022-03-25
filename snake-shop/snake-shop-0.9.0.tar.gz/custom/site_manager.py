import sys
from django.contrib.sites.managers import CurrentSiteManager
from django.db import models
from django.contrib.sites.models import Site
from django.db.utils import ProgrammingError
from django.utils.functional import cached_property
from django.core.exceptions import ObjectDoesNotExist


class BaseSiteManager(CurrentSiteManager):
    use_in_migrations = False
    siteless_cases = ['makemigrations', 'migrate', 'test']

    @property
    def is_siteless_case(self):
        return any([x for x in sys.argv if x not in self.siteless_cases])

    @cached_property
    def site(self):
        return Site.objects.get_current()

    def _base_queryset(self):
        return super(models.Manager, self).get_queryset()  # pylint: disable=bad-super-call

    def get_filter_kwargs(self):
        field_name = self._get_field_name()
        field = self.model._meta.get_field(field_name)
        if field.many_to_many:
            kwargs = {f'{field_name}__id': self.site.id}
        else:
            kwargs = {f'{field_name}__id': self.site.id}
        return kwargs

    def get_queryset(self):
        qs = self._base_queryset()
        if not self.is_siteless_case:
            assert self.site.configuration
            if not self.site.configuration.show_all_products:
                qs = qs.filter(**self.get_filter_kwargs())
        return qs

    def create(self, site=None, **kwargs):
        if not site:
            raise NotImplementedError('Need to implement site logic here')
        super().create(site=site, **kwargs)

    def update(self, site=None, **kwargs):
        if not site:
            raise NotImplementedError('Need to implement site logic here')
        super().update(site=site, **kwargs)


class DefaultSiteManager(BaseSiteManager):
    """ This is for usage to replace default managers with default function """


class SiteMixin:
    """
    Use this mixin for models. In mainly ensures to save the current site.
    """
    # Is replaced when using a custom manager at model !
    objects = DefaultSiteManager()

    def save(self, *args, **kwargs):
        setattr(self, 'site', Site.objects.get_current())
        super().save(*args, **kwargs)
