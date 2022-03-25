from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render
from django.views import View

from .models import Empfaenger
from fsmedhro_core.models import Studiengang, Studienabschnitt


class SendDiva(LoginRequiredMixin, View):
    def get_context_data(self):
        return {
            'studiengaenge': Studiengang.objects.all(),
            'studienabschnitte': Studienabschnitt.objects.all(),
            'empfaenger': Empfaenger.objects.all(),
        }

    def get(self, request):
        context = self.get_context_data()
        return render(request, 'fsmedhro_diva/send.html', context)

    def post(self, request):
        context = self.get_context_data()
        errors = []

        studiengang = Studiengang.objects.get(
            id=int(request.POST.get('studiengang'))
        )
        studienabschnitt = Studienabschnitt.objects.get(
            id=int(request.POST.get('studienabschnitt'))
        )

        self.betreff = request.POST.get("betreff")
        self.anliegen = request.POST.get("anliegen")

        self.anonymous_mode = bool(request.POST.get('anonymous_mode', False))

        self.pflicht_empfaenger = Empfaenger.objects.filter(required=True)
        sonstige_empfaenger = Empfaenger.objects.filter(
            id__in=map(int, request.POST.getlist('empfaenger')),
        )

        if not (self.pflicht_empfaenger.exists() or sonstige_empfaenger.exists()):
            errors.append(
                'Keine Empfänger angegeben. '
                'Bitte wähle mindestens einen Empfänger aus.'
            )

        if errors:
            context['errors'] = errors
            context['betreff'] = self.betreff
            context['anliegen'] = self.anliegen

            return render(request, 'fsmedhro_diva/send.html', context)

        self.betreff = f'[DIVA] {self.betreff}'
        self.anliegen = (
            f'Studiengang: {studiengang.bezeichnung}\n'
            f'Studienabschnitt: {studienabschnitt.bezeichnung}\n'
            '\n'
            f'{self.anliegen}'
        )

        diva_mail_pflicht = self.baue_pflichtmail()
        diva_mail_sonstige = EmailMessage(
            to=[str(e) for e in sonstige_empfaenger],
            subject=self.betreff,
            body=self.anliegen,
        )

        diva_mail_pflicht.send()
        diva_mail_sonstige.send()

        context['success'] = True
        context['anonymous_mode'] = self.anonymous_mode

        return render(request, 'fsmedhro_diva/send.html', context)

    def baue_pflichtmail(self):
        diva_mail_pflicht = EmailMessage(
            to=[str(e) for e in self.pflicht_empfaenger],
            subject=self.betreff,
        )

        if self.anonymous_mode:
            anliegen_pflicht = (
                f'Diese DIVA-Mail wurde anonym verschickt.\n'
                '\n'
                f'{self.anliegen}'
            )
        else:
            anliegen_pflicht = (
                f'Name: {self.request.user.get_full_name()}\n'
                '\n'
                f'{self.anliegen}'
            )

            diva_mail_pflicht.reply_to = [self.request.user.email]
            diva_mail_pflicht.cc = [self.request.user.email]

        diva_mail_pflicht.body = anliegen_pflicht

        return diva_mail_pflicht
