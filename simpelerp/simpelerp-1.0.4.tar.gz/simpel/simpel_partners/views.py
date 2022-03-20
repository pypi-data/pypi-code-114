# from functools import cached_property

# from django.contrib import messages
# from django.http import Http404, HttpResponse, HttpResponseBadRequest
# from django.shortcuts import render
# from django.urls import path
# from django.utils.translation import gettext_lazy as _
# from django.views.generic import FormView, TemplateView

# from simpel.simpel_auth.forms import AddressForm

# from .forms import ConfirmationForm, PartnerForm
# from .models import Partner
# from .settings import simpel_partners_settings as partners_settings


# class PartnerUpdateView(FormView):
#     template_name = "dashboard/me_partner_update_form.html"
#     form_class = PartnerForm

#     def dispatch(self, request, *args, **kwargs):
#         self.partner = Partner.get_for_user(self.request.user)
#         return super().dispatch(request, *args, **kwargs)

#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.update(
#             {
#                 "instance": self.partner,
#             }
#         )
#         return kwargs

#     def form_valid(self, form):
#         form.save()
#         messages.success(self.request, _("Your partner profile updated."))
#         return self.render_to_response(self.get_context_data(form=form))

#     def form_invalid(self, form):
#         print(form.data)
#         return super().form_invalid(self.request)

#     def post(self, request):
#         return super().post(request)

#     def put(self, request):
#         return HttpResponse("Returning Initial Form !!")

#     def delete(self, request):
#         return HttpResponse("Returning Initial Form !!")


# class PartnerRegistrationView(TemplateView):

#     template_name = "dashboard/simpel_partners/registration.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context.update(
#             {
#                 "partner_form": PartnerForm(),
#                 "address_form": AddressForm(),
#                 "confirmation_form": ConfirmationForm(),
#             }
#         )
#         return context


# class PartnerDashboardViewset:
#     def _get_contact_or_404(self, partner, contact_id):
#         try:
#             contact = partner.contacts.get(pk=contact_id)
#             return contact
#         except Exception:
#             raise Http404(_("Contact not Found!"))

#     def _get_address_or_404(self, partner, address_id):
#         try:
#             contact = partner.addresses.get(pk=address_id)
#             return contact
#         except Exception:
#             raise Http404(_("Address not Found!"))

#     def register(self, request):
#         view_class = partners_settings.PARTNER_REGISTRATION_VIEW
#         return view_class.as_view()(request)

#     def update(self, request):
#         if request.htmx:
#             return PartnerUpdateView.as_view()(request)
#         else:
#             partner = Partner.get_for_user(request.user)
#             if request.method == "GET":
#                 context = {
#                     "title": _("Partner Information"),
#                     "object": partner,
#                 }
#                 return render(request, "dashboard/me_partner_update.html", context=context)
#             else:
#                 raise HttpResponseBadRequest(_("Bad Request!"))

#     def add_contact(self, request):
#         self.partner = request.user.partner
#         if request.htmx:
#             return
#         else:
#             return

#     def delete_contact(self, request, contact_id):
#         self.partner = request.user.partner
#         contact = self._get_contact_or_404(self.partner, contact_id)
#         if request.htmx:
#             return
#         else:
#             return

#     def update_contact(self, request, contact_id):
#         self.partner = request.user.partner
#         contact = self._get_contact_or_404(self.partner, contact_id)
#         if request.htmx:
#             return
#         else:
#             return

#     def add_address(self, request):
#         self.partner = request.user.partner
#         if request.htmx:
#             return
#         else:
#             return

#     def update_address(self, request, address_id):
#         self.partner = request.user.partner
#         address = self._get_address_or_404(self.partner, address_id)
#         if request.htmx:
#             return
#         else:
#             return

#     def delete_address(self, request, address_id):
#         self.partner = request.user.partner
#         address = self._get_address_or_404(self.partner, address_id)
#         if request.htmx:
#             return
#         else:
#             return

#     @cached_property
#     def urls(self):
#         return self.get_urls()

#     def get_urls(self):
#         return [
#             path("register/", self.register, name="partner_register"),
#             path("update/", self.update, name="partner_update"),
#             path("contact/add/", self.update, name="partner_add_contact"),
#             path("contact/update/<int:pk>/", self.update, name="partner_update_contact"),
#             path("contact/delete/<int:pk>/", self.update, name="partner_delete_contact"),
#             path("address/add/", self.update, name="partner_add_address"),
#             path("address/update/<int:pk>/", self.update, name="partner_update_address"),
#             path("address/delete/<int:pk>/", self.update, name="partner_delete_address"),
#         ]
