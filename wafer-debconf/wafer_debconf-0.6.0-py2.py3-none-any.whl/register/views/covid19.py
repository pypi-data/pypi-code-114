from register.forms.covid19 import Covid19Form
from register.views.core import RegisterStep
from register.models.attendee import Attendee


class Covid19View(RegisterStep):
    title = 'COVID-19'
    form_class = Covid19Form

    def get_initial(self):
        attendee = self.request.user.attendee
        initial = {
            'vaccinated': attendee.vaccinated,
            'vaccination_notes': attendee.vaccination_notes,
        }
        return initial

    def form_valid(self, form):
        user = self.request.user
        data = form.cleaned_data

        user.attendee  # We should never be creating, here
        user.attendee, created = Attendee.objects.update_or_create(
            user=user, defaults=data)

        return super().form_valid(form)
