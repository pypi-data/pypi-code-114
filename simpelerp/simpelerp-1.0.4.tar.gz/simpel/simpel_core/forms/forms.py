from django import forms

from simpel.utils import extract_contenttype


class ContentTypeMixinForm(forms.ModelForm):
    ct_data = None
    contenttype = forms.CharField()
    contenttype_id = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput(),
    )
    contenttype_slug = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["contenttype"] = forms.ChoiceField(
            label=self.get_contenttype_label(),
            choices=self.get_contenttype_choices(),
            widget=forms.Select(),
        )

    def get_contenttype_label(self):
        return "Content Type"

    def get_contenttype_choices(self):
        raise NotImplementedError("%s Should implement get_contenttype_choices" % self.__class__.__name__)

    def get_ct_data(self, data):
        if not self.ct_data:
            self.ct_data = extract_contenttype(self.cleaned_data["contenttype"])
        return self.ct_data

    def clean_contenttype_id(self):
        ct_data = self.get_ct_data(self.cleaned_data["contenttype"])
        return ct_data["contenttype_id"]

    def clean_contenttype_slug(self):
        ct_data = self.get_ct_data(self.cleaned_data["contenttype"])
        return ct_data["contenttype_slug"]
