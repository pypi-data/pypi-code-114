import hashlib
import logging
import os
import sys
import uuid

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.template.loader import render_to_string
from django.utils.http import urlencode

from .settings import simpel_auth_settings as auth_settings

if sys.version > "3":
    long = int  # pylint: disable=invalid-name


logger = logging.getLogger("engine")


def render_notice(request, notice):
    context = {"notice": notice}
    return render_to_string(
        "admin/notice_line.html",
        context=context,
        request=request,
    )


def slug2id(slug):
    return long(slug) - 110909


def id2slug(notification_id):
    return notification_id + 110909


def is_soft_delete():
    return auth_settings.NOTIFICATION_SOFT_DELETE


def assert_soft_delete():
    if not is_soft_delete():
        # msg = """To use 'deleted' field, please set 'SOFT_DELETE'=True in settings.
        # Otherwise NotificationQuerySet.unread and NotificationQuerySet.read do NOT filter by 'deleted' field.
        # """
        msg = "REVERTME"
        raise ImproperlyConfigured(msg)


def upload_avatar_to(instance, filename, uid=None):
    filename, ext = os.path.splitext(filename)
    uid = uid or uuid.uuid4()
    return os.path.join(
        "avatar_images",
        "avatar_{uuid}_{filename}{ext}".format(
            uuid=uid,
            filename=filename,
            ext=ext,
        ),
    )


def get_bot_user():
    User = get_user_model()
    bot_username = getattr(settings, "BOT_USERNAME", None)
    if bot_username:
        bot = User.objects.get(username=bot_username)
    else:
        bot = User.objects.filter(is_superuser=True).first()
    return bot


def get_perms(actions, model):
    """returns"""
    from django.contrib.auth import get_permission_codename
    from django.contrib.auth.models import Permission

    perms = []
    for act in actions:
        perm_name = get_permission_codename(act, model._meta)
        try:
            perm = Permission.objects.get(codename=perm_name)
            perms.append(perm)
        except Permission.DoesNotExist:
            continue
    return tuple(perms)


def get_perms_dict(actions, model):
    """returns"""
    from django.contrib.auth import get_permission_codename
    from django.contrib.auth.models import Permission

    perms = dict()
    for act in actions:
        perm_name = get_permission_codename(act, model._meta)
        try:
            perm = Permission.objects.filter(codename=perm_name).first()
            perms[act] = perm
        except Permission.DoesNotExist:
            continue
    return perms


def add_perms(group_names, permission_list):
    for perm_obj in permission_list:
        if isinstance(group_names, list):
            actors = group_names
        else:
            actors = [group_names]
        for actor in actors:
            actor.permissions.add(perm_obj)


def add_group_perms(group, perm_dict, actions):
    perms = list()
    for key in actions:
        perms.append(perm_dict[key])
    add_perms(group, perms)


def get_gravatar_url(email, size=50):
    default = "mm"
    size = int(size) * 2  # requested at retina size by default and scaled down at point of use with css
    gravatar_provider_url = "//www.gravatar.com/avatar"

    if (not email) or (gravatar_provider_url is None):
        return None

    gravatar_url = "{gravatar_provider_url}/{hash}?{params}".format(
        gravatar_provider_url=gravatar_provider_url.rstrip("/"),
        hash=hashlib.md5(email.lower().encode("utf-8")).hexdigest(),
        params=urlencode({"s": size, "d": default}),
    )
    return gravatar_url


def create_demo_users(users_and_group):
    from django.contrib.auth import get_user_model
    from django.contrib.auth.models import Group

    User = get_user_model()
    password = "demo_pwd"
    for username, group_name in users_and_group.items():
        try:
            user = User.objects.get(username=username)
            print("%s has been created" % user)
        except User.DoesNotExist:
            name = username.split("_")
            print(name)
            first_name = name[0]
            last_name = name[1]
            user = User.objects.create_user(
                username=username,
                password=password,
                email="%s@gmail.com" % username,
                first_name=first_name,
                last_name=last_name,
                is_staff=True,
                is_superuser=False,
            )
            print("Create new user %s" % user)
        user.save()

        if group_name is not None:
            group, _ = Group.objects.get_or_create(name=group_name)
            group.user_set.add(user)
            print("Add %s to '%s' group" % (user, group))


def get_activities(obj):
    from .models import Activity

    contenttype = ContentType.objects.get_for_model(obj.__class__)
    activities = Activity.objects.filter(
        models.Q(
            action_object_type=contenttype,
            action_object_id=obj.id,
        )
    )
    return activities


def get_notifications(obj):
    from .models import Notification

    contenttype = ContentType.objects.get_for_model(obj.__class__)
    as_actor = models.Q(
        actor_content_type=contenttype,
        actor_object_id=obj.id,
    )
    as_actions = models.Q(
        action_object_content_type=contenttype,
        action_object_object_id=obj.id,
    )
    as_targets = models.Q(
        target_content_type=contenttype,
        target_object_id=obj.id,
    )
    notifications = Notification.objects.filter(as_actor | as_actions | as_targets)
    return notifications
