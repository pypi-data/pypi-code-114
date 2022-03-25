from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractProfile(models.Model):
    MR, MISS, MRS, MS, DR = ("Mr", "Miss", "Mrs", "Ms", "Dr")
    TITLE_CHOICES = (
        (MR, _("Mr")),
        (MISS, _("Miss")),
        (MRS, _("Mrs")),
        (MS, _("Ms")),
        (DR, _("Dr")),
    )

    title = models.CharField(
        _("title"),
        max_length=64,
        choices=TITLE_CHOICES,
        blank=True,
        help_text=_(
            "Treatment Pronouns for the human.",
        ),
    )
    full_name = models.CharField(
        max_length=255,
        verbose_name=_("Full name"),
    )

    class Meta:
        abstract = True
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return "%s. %s" % (self.title, self.full_name)
