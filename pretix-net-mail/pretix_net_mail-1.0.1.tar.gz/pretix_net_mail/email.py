from pretix.base.email import TemplateBasedMailRenderer
from django.template.loader import get_template
template = get_template('pretix_net_mail/NES.html')

class NESMailRenderer(TemplateBasedMailRenderer):
    verbose_name = "NES Mail"
    identifier = "NES"
    thumbnail_filename = "pretix_net_mail/NETthumb.png"
    template_name = "pretix_net_mail/NES.html"
