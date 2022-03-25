from django.utils.translation import gettext_lazy as _
from django.views import generic
from django.urls.base import reverse_lazy
from django.contrib import messages
from oscar.apps.customer import views, mixins

from apps.payment.models import Bankcard
from apps.payment.forms import BankcardForm
from .forms import EmailAuthenticationForm, UserForm


class AccountAuthView(views.AccountAuthView):
    login_form_class = EmailAuthenticationForm


class AddressCreateView(views.AddressCreateView):
    def get_success_url(self):
        messages.success(self.request,
                         _("Address '%s' created") % self.object.summary)
        if self.request.GET.get('next'):
            return self.request.GET.get('next')
        return super().get_success_url()


class ProfileUpdateView(views.ProfileUpdateView):
    form_class = UserForm


class BankAccountBaseView(mixins.PageTitleMixin):
    model = Bankcard
    form_class = BankcardForm
    template_name = "oscar/customer/bank_account/form.html"
    success_url = reverse_lazy('customer:bankaccount-list')
    active_tab = 'bank_account'
    context_object_name = "bank_account"
    page_title = _('Bank Accounts')

    def get_form_kwargs(self):
        kwargs = generic.CreateView.get_form_kwargs(self)
        kwargs['request'] = self.request
        return kwargs

    def get_success_url(self):
        next_url = self.request.GET.get('next', self.success_url)
        if self.request.GET.get('next') and self.object:
            next_url += '?bankacc=' + str(self.object.pk)
        return next_url


class BankAccountListView(BankAccountBaseView, generic.ListView):
    context_object_name = "bank_accounts"
    template_name = "oscar/customer/bank_account/list.html"

    def get_queryset(self):
        return self.request.user.bankcards.all()


class BankAccountCreateView(BankAccountBaseView, generic.CreateView):
    pass


class BankAccountUpdateView(BankAccountBaseView, generic.UpdateView):
    pass


class BankAccountDeleteView(BankAccountBaseView, generic.DeleteView):
    template_name = "oscar/customer/bank_account/delete.html"
