from django.views.generic.edit import FormView
from apps.address.models import UserAddress
from .forms import PostcodeCheckerInputForm
from .models import Tour

class DeliveryTimesFormView(FormView):
    form_class = PostcodeCheckerInputForm
    template_name = 'delivery/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tours'] = Tour.get_cached()
        postcode = self.request.GET.get('postcode')
        if postcode:
            postcode = int(postcode)
        else:
            postcode = self.request.session.get('postcode')

        postcode = [UserAddress(postcode=postcode)] if postcode else []
        user = self.request.user
        if user.is_authenticated:
            addresses = UserAddress.objects.filter(user=user)
        else:
            addresses = []
        context['addresses'] = [*postcode, *addresses]
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
