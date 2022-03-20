from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from .tasks import send_mail


class AccountAdapter(DefaultAccountAdapter):

    """Custom Account Adapter"""

    def send_mail(self, template_prefix, email, context):
        # remove request object form context
        context["request"] = None
        context["to_email"] = email
        context["subject"] = render_to_string("{0}_subject.txt".format(template_prefix), context)
        send_mail.delay(template_prefix, context)

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = get_current_site(request)
        activate_url = self.get_email_confirmation_url(request, emailconfirmation)
        to_email = emailconfirmation.email_address.email
        user = emailconfirmation.email_address.user
        ctx = {
            "user": user,
            "to_email": to_email,
            "activate_url": activate_url,
            "current_site": current_site,
            "key": emailconfirmation.key,
        }
        if signup:
            email_template = "account/email/email_confirmation_signup"
        else:
            email_template = "account/email/email_confirmation"
        self.send_mail(email_template, to_email, ctx)
