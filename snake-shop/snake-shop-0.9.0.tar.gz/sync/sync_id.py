from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _


class SyncIdMixin(models.Model):
    """
    Careful when migrating existing models:
    Migration creates one id for all objects.
    Need to create with null=True and migrate the existing.
    """
    sync_id = models.UUIDField(
        _('Sync-Id'),
        help_text=_('Für die Identifizierung des Objekts bei Synchronisierungs'
                    'vorgängen'),
        default=uuid4,
        editable=False,
        unique=True,
        #blank=True, null=True,
    )

    class Meta:
        abstract = True
