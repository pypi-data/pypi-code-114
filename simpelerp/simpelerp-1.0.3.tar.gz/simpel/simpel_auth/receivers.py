import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from .helpers import notify_handler
from .models import Profile, User
from .signals import notify
from .tasks import send_bot_message

logger = logging.getLogger("engine")

# connect the signal
notify.connect(notify_handler, dispatch_uid="simpel.simpel_auth.models.notification")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, raw, using, **kwargs):
    Profile.get_for_user(instance)
    if created:
        # Send welcome message for new user
        msg = "Welcome %s" % str(instance)
        send_bot_message(instance, msg)
