from django.utils.functional import SimpleLazyObject
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from .models import Partner


class PartnerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        is_productive = settings.STAGE == 'PRODUCTIVE'
        if is_productive and request.site.domain != request.get_host():
            raise AttributeError(
                'Wrong site (%s) for this url(%s)!!!' % (request.site.domain, request.get_host()))

        '''
        Wenn user partner vorhanden -> höchste Priorität
        Wenn nicht, 
        '''
        def load_partners():
            qs = Partner.objects.filter(site=request.site)
            qs = qs.order_by('-priority')
            default_partner = qs.last()

            qs = request.user.partners.filter(site=request.site)
            qs = qs.order_by('-priority')
            user_partner = qs.first() or default_partner
            return Partner.objects.filter(pk=user_partner.pk)

        request.partners = SimpleLazyObject(load_partners)
