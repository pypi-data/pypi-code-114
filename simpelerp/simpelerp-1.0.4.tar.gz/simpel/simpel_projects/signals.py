from django.db.models import signals
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from simpel.simpel_auth.tasks import send_notification_job
from simpel.simpel_core.signals import post_complete, post_validate, pre_complete

from .models import CancelationDeliverable, Deliverable, DocumentDeliverable, WorkOrder


def action_save_deliverable(sender, instance, created):
    instance.task.save()
    instance.task.workorder.save()


@receiver(signals.post_save, sender=Deliverable)
def after_save_deliverable(sender, instance, created, **kwargs):
    action_save_deliverable(sender, instance, created)


@receiver(signals.post_save, sender=CancelationDeliverable)
def after_save_cancel_deliverable(sender, instance, created, **kwargs):
    action_save_deliverable(sender, instance, created)


@receiver(signals.post_save, sender=DocumentDeliverable)
def after_save_doc_deliverable(sender, instance, created, **kwargs):
    action_save_deliverable(sender, instance, created)


@receiver(post_validate, sender=WorkOrder)
def after_validate_wo(sender, instance, actor, request, **kwargs):
    instance.reference.process(request)
    send_notification_job.delay(
        actor_id=actor.id,
        groups=["Customer Service", "Project Manager"],
        verb=_("validate"),
        object_model=sender,
        object_id=instance.id,
        target_model=instance.reference.__class__,
        target_id=instance.reference_id,
    )


@receiver(pre_complete, sender=WorkOrder)
def before_complete_wo(sender, instance, actor, request, **kwargs):
    if not instance.progress_complete:
        raise PermissionError(_("%s progress is not complete!") % instance)
    else:
        pass


@receiver(post_complete, sender=WorkOrder)
def after_complete_wo(sender, instance, actor, request, **kwargs):
    instance.reference.complete(request)
    send_notification_job.delay(
        actor_id=actor.id,
        groups=["Customer Service", "Project Manager"],
        verb=_("complete"),
        object_model=sender,
        object_id=instance.id,
        target_model=instance.reference.__class__,
        target_id=instance.reference_id,
    )
