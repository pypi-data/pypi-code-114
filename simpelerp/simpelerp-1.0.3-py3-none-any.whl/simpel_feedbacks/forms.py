# from django import forms
# from django.utils.translation import gettext_lazy as _
from django_comments_xtd.forms import XtdCommentForm
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

# from django_comments_xtd.models import TmpXtdComment


class UserCommentForm(XtdCommentForm):
    captcha_enabled = False
    # title = forms.CharField(
    #     max_length=256,
    #     widget=forms.TextInput(attrs={'placeholder': _('title')})
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.captcha_enabled:
            self.fields["captcha"] = ReCaptchaField(widget=ReCaptchaWidget())

    def get_comment_create_data(self, site_id=None):
        data = super(UserCommentForm, self).get_comment_create_data(site_id=site_id)
        # data.update({
        #     'title': self.cleaned_data['title'],
        # })
        return data
