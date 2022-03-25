from oscar.apps.basket.views import BasketAddView
from django.http import JsonResponse
from custom.views import DynamicDataView


class BasketAddView(BasketAddView):

    def get_dynamic_data_context(self, request, *args, **kwargs):
        return DynamicDataView().get_context_data(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        normal_response = super().post(request, *args, **kwargs)
        if request.POST.get('ajax') == 'true':
            context = self.get_dynamic_data_context(request, *args, **kwargs)
            if 'wishlists' in context:
                del context['wishlists']
            return JsonResponse(context)
        return normal_response
