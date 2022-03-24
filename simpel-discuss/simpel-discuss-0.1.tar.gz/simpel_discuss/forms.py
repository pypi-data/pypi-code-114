import logging

from django_comments_xtd.forms import XtdCommentForm

from simpel_discuss.settings import discuss_settings

logger = logging.getLogger(__name__)

try:
    from snowpenguin.django.recaptcha2.fields import ReCaptchaField
    from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

    CAPTCHA_INSTALLED = True
except ImportError:
    if discuss_settings.CAPTCHA_ENABLED:
        logger.warning("discuss captcha feature enabled, but django-recaptcha2 is not installed!")
    CAPTCHA_INSTALLED = False


class ThreatForm(XtdCommentForm):
    captcha_enabled = discuss_settings.CAPTCHA_ENABLED
    # title = forms.CharField(
    #     max_length=256,
    #     widget=forms.TextInput(attrs={'placeholder': _('title')})
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.captcha_enabled and CAPTCHA_INSTALLED:
            self.fields["captcha"] = ReCaptchaField(widget=ReCaptchaWidget())

    def get_comment_create_data(self, site_id=None):
        data = super(ThreatForm, self).get_comment_create_data(site_id=site_id)
        # data.update({
        #     'title': self.cleaned_data['title'],
        # })
        return data
