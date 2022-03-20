import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import render_to_string
from django_rq import job

from .signals import notify
from .utils import get_bot_user

logger = logging.getLogger("engine")


def message(msg, level=0):
    print(f"{msg}")


def send_bot_message(recipient, verb):
    try:
        actor = get_bot_user()
        notify.send(actor, recipient=recipient, verb=verb)
    except Exception as exc:
        message(f"{exc}")


def render_mail(template_prefix, context):
    """
    Renders an e-mail to `email`.  `template_prefix` identifies the
    e-mail that is to be sent, e.g. "account/email/email_confirmation"
    """
    email = context.get("to_email", list())
    to_emails = [email] if isinstance(email, str) else email
    subject = context.get("subject", "Email form %s" % settings.SITE_DOMAIN).strip()

    get_from_email = context.get("from_email", None)
    from_email = get_from_email if get_from_email else settings.DEFAULT_FROM_EMAIL

    bodies = {}
    for ext in ["html", "txt"]:
        try:
            template_name = "{0}_message.{1}".format(template_prefix, ext)
            bodies[ext] = render_to_string(template_name, context).strip()
        except TemplateDoesNotExist:
            if ext == "txt" and not bodies:
                # We need at least one body
                raise
    if "txt" in bodies:
        msg = EmailMultiAlternatives(subject, bodies["txt"], from_email, to_emails)
        if "html" in bodies:
            msg.attach_alternative(bodies["html"], "text/html")
    else:
        msg = EmailMessage(subject, bodies["html"], from_email, to_emails)
        msg.content_subtype = "html"  # Main content is now text/html
    return msg


@job
def send_mail(template_prefix, context):
    msg = render_mail(template_prefix, context)
    msg.send()


def send_notification(user_id, group_list, verb, action_object=None, target_object=None):
    actor = get_user_model().objects.get(pk=user_id)
    recipients_group = Group.objects.filter(name__in=group_list).first()

    recipient_ids = []

    content = {"verb": verb}

    if action_object is not None:
        content["action_object"] = action_object

    if target_object is not None:
        content["target"] = target_object

    if recipients_group:
        for user in recipients_group.user_set.all():
            notify.send(actor, recipient=user, **content)
            recipient_ids.append(user.id)

    action_obj_user = getattr(action_object, "user", None)
    if action_obj_user is not None and action_obj_user.id not in recipient_ids:
        notify.send(actor, recipient=action_obj_user, **content)


@job
def send_notification_job(
    actor_id,
    groups,
    verb,
    object_model,
    object_id,
    target_model=None,
    target_id=None,
):
    # Send after create new sales order called in signals
    instance = None
    if object_model is not None and object_id is not None:
        try:
            instance = object_model.objects.get(pk=object_id)
        except Exception:
            instance = None
    target = None
    if target_model is not None and target_id is not None:
        try:
            target = target_model.objects.get(pk=target_id)
        except Exception:
            target = None
    send_notification(actor_id, groups, verb, instance, target)
