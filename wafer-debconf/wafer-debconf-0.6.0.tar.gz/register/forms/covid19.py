from django import forms

from crispy_forms.helper import FormHelper


class Covid19Form(forms.Form):
    vaccinated = forms.BooleanField(
        label='I have been fully vaccinated against COVID-19',
        help_text='You are fully vaccinated if you have completed the full '
                  'course of vaccination, at least 2 weeks before arrival '
                  'at the conference venue.',
        required=False,
    )
    vaccination_notes = forms.CharField(
        label='Notes for the conference organisers',
        help_text='If you have not been vaccinated, please explain the '
                  'situation.',
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.include_media = False


    def clean(self):
        cleaned_data = super().clean()
        if (not cleaned_data.get('vaccinated')
                and not cleaned_data.get('vaccination_notes')):
            self.add_error(
                'vaccination_notes',
                'Please explain the reasons for not receiving a vaccine.')

        return cleaned_data
