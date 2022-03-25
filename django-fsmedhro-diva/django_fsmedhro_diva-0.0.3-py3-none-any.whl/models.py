from django.db import models

class Empfaenger(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    required = models.BooleanField(
        help_text=(
            'DIVA-Mails werden immer an diesen Empfänger versandt. '
            'Nur die Pflichtempfänger erhalten personengebundene Daten für Rückfragen.'
        ),
        verbose_name='Pflichtversand',
    )

    def __str__(self):
        return f'{self.name} <{self.email}>'

    class Meta:
        verbose_name = 'Empfänger'
        verbose_name_plural = 'Empfänger'
        ordering = ['name']
