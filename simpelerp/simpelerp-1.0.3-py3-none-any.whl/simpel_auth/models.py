import json
from functools import cached_property

from django.conf import settings
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.contrib.admin.utils import quote
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import NoReverseMatch
from django.utils import timezone
from django.utils.text import get_text_list
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

from simpel.simpel_core import utils
from simpel.simpel_core.permissions import user_can_edit_setting
from simpel.utils import reverse

from .managers import ActivityManager, NotificationQuerySet, UserManager
from .utils import get_gravatar_url, id2slug, upload_avatar_to


class LinkedContact(models.Model):
    PHONE = "phone"
    EMAIL = "email"
    MOBILE = "mobile"
    FAX = "fax"
    WHATSAPP = "whatsapp"
    WEBSITE = "website"

    CONTACT_TYPES = (
        (PHONE, _("Phone")),
        (EMAIL, _("Email")),
        (MOBILE, _("Mobile")),
        (WHATSAPP, _("Whatsapp")),
        (WEBSITE, _("Website")),
    )
    linked_object_type = models.ForeignKey(
        ContentType,
        related_name="linked_contacts",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Linked object type"),
    )
    linked_object_id = models.IntegerField(
        null=True,
        blank=True,
        help_text=_("Linked instance primary key."),
    )
    linked_object = GenericForeignKey(
        "linked_object_type",
        "linked_object_id",
    )
    contact_type = models.CharField(
        max_length=255,
        choices=CONTACT_TYPES,
        default=PHONE,
        verbose_name=_("type"),
        help_text=_("E.g. Phone or mobile"),
    )
    contact = models.CharField(
        _("contact"),
        max_length=255,
        help_text="Phone number or etc.",
    )
    is_verified = models.BooleanField(
        default=False,
        editable=False,
    )

    def __str__(self):
        return "(%s) %s" % (self.contact_type.title(), self.contact)

    def to_dict(self):
        return {
            "contact_type": self.primary,
            "contact": self.address_type,
            "is_verified": self.name,
        }


class LinkedAddress(models.Model):
    HOME = "home"
    OFFICE = "office"
    BRANCH_OFFICE = "branch_office"
    SHIPPING = "shipping"
    BILLING = "billing"
    DROPSHIPPING = "drop_shipping"
    DELIVERABLE = "deliverable"
    ELSE = "else"

    ADDRESS_TYPES = (
        (HOME, _("Home")),
        (OFFICE, _("Office")),
        (BRANCH_OFFICE, _("Branch Office")),
        (BILLING, _("Billing")),
        (SHIPPING, _("Shipping")),
        (DROPSHIPPING, _("Dropshipping")),
        (DELIVERABLE, _("Deliverable")),
        (ELSE, _("Else")),
    )
    linked_object_type = models.ForeignKey(
        ContentType,
        related_name="linked_address",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Linked object type"),
    )
    linked_object_id = models.IntegerField(
        null=True,
        blank=True,
        help_text=_("Linked instance primary key."),
    )
    linked_object = GenericForeignKey(
        "linked_object_type",
        "linked_object_id",
    )
    primary = models.BooleanField(default=False)
    address_type = models.CharField(
        max_length=255,
        choices=ADDRESS_TYPES,
        default=BILLING,
        verbose_name=_("type"),
        help_text=_("E.g. Shipping or billing"),
    )
    name = models.CharField(
        _("name"),
        max_length=255,
        help_text="If blank, contact name will be used.",
    )
    phone = models.CharField(
        verbose_name=_("Phone"),
        null=True,
        blank=False,
        max_length=255,
        help_text=_("In case we need to make a call."),
    )
    address = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_("address"),
    )
    city = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_("city"),
    )
    province = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_("province"),
    )
    country = models.CharField(
        null=255,
        max_length=255,
        blank=False,
        verbose_name=_("country"),
    )
    zipcode = models.CharField(
        null=True,
        blank=False,
        max_length=10,
        verbose_name=_("zip code"),
    )

    def __str__(self):
        return "(%s) %s" % (self.address_type.title(), self.name)

    def text_line_1(self):
        address = [self.address, self.city]
        return ", ".join([str(a) for a in address])

    def text_line_2(self):
        address = [self.province, self.country, self.zipcode]
        return ", ".join([str(a) for a in address])

    def to_dict(self):
        return {
            "primary": self.primary,
            "address_type": self.address_type,
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "province": self.province,
            "country": self.country,
            "zipcode": self.zipcode,
        }


class User(AbstractUser):

    addresses = GenericRelation(
        LinkedAddress,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )
    contacts = GenericRelation(
        LinkedContact,
        content_type_field="linked_object_type",
        object_id_field="linked_object_id",
    )

    objects = UserManager()

    class Meta(AbstractUser.Meta):
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    @cached_property
    def avatar(self):
        return self.profile.get_avatar()

    def has_setting_perm(self, model=None):
        return user_can_edit_setting(self, model)

    def member_of(self, group_names):
        """Check if user is staff member"""
        filters = dict()
        if isinstance(group_names, (list, tuple)):
            filters = {"name__in": group_names}
        elif isinstance(group_names, str):
            filters = {"name": group_names}
        else:
            raise ValueError(_("group_names arg shoulbe string or list of string"))
        return self.groups.filter(**filters).exists()


class Biography(models.Model):
    MALE = "L"
    FEMALE = "P"

    GENDER = (
        (MALE, _("Male").title()),
        (FEMALE, _("Female").title()),
    )
    pid = models.CharField(
        null=True,
        blank=False,
        max_length=15,
        verbose_name=_("PID"),
        help_text=_("Personal Identifier Number"),
    )
    tax_id = models.CharField(
        null=True,
        blank=True,
        max_length=15,
        verbose_name=_("Tax ID"),
        help_text=_("Tax ID"),
    )
    full_name = models.CharField(
        _("full name"),
        max_length=50,
        null=False,
        blank=False,
    )
    short_name = models.CharField(
        _("short name"),
        max_length=150,
        blank=True,
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_("Title"),
    )
    blood_type = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name=_("blood_type"),
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        default=MALE,
        verbose_name=_("gender"),
    )

    religion = models.CharField(
        max_length=25,
        null=True,
        blank=True,
        verbose_name=_("religion"),
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        default=timezone.now,
        verbose_name=_("date of birth"),
    )
    place_of_birth = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_("place of birth"),
    )

    class Meta:
        abstract = True


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        editable=False,
    )
    avatar = models.ImageField(
        verbose_name=_("profile picture"),
        upload_to=upload_avatar_to,
        blank=True,
    )

    # PREFERENCES
    preferred_language = models.CharField(
        verbose_name=_("preferred language"),
        max_length=10,
        help_text=_("Select language for the admin"),
        default="",
    )
    current_time_zone = models.CharField(
        verbose_name=_("current time zone"),
        max_length=40,
        help_text=_("Select your current time zone"),
        default="",
    )

    # submitted_notifications = models.BooleanField(
    #     verbose_name=_("submitted notifications"),
    #     default=True,
    #     help_text=_("Receive notification when a page is submitted for moderation"),
    # )
    # approved_notifications = models.BooleanField(
    #     verbose_name=_("approved notifications"),
    #     default=True,
    #     help_text=_("Receive notification when your page edit is approved"),
    # )
    # rejected_notifications = models.BooleanField(
    #     verbose_name=_("rejected notifications"),
    #     default=True,
    #     help_text=_("Receive notification when your page edit is rejected"),
    # )
    # updated_comments_notifications = models.BooleanField(
    #     verbose_name=_("updated comments notifications"),
    #     default=True,
    #     help_text=_(
    #         "Receive notification when comments have been created, resolved, "
    #         "or deleted on a page that you have subscribed to receive comment notifications on",
    #     ),
    # )

    @classmethod
    def get_for_user(cls, user):
        profile, _ = cls.objects.get_or_create(user=user, defaults={})
        return profile

    def get_preferred_language(self):
        return self.preferred_language or get_language()

    def get_current_time_zone(self):
        return self.current_time_zone or settings.TIME_ZONE

    def get_avatar(self):
        if bool(self.avatar):
            return self.avatar.url
        return get_gravatar_url(self.user.email)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("user profile")
        verbose_name_plural = _("user profiles")


class Activity(models.Model):
    ADDITION = 1
    CHANGE = 2
    DELETION = 3
    CREATION = 4
    VALIDATION = 5
    APPROVAL = 6
    REJECTION = 7
    PROCESS = 8
    CLOSING = 9
    CLONE = 10
    CONVERTION = 11
    COMPLETION = 12
    CANCELATION = 13

    ACTION_FLAGS = (
        (ADDITION, _("Addition")),
        (CHANGE, _("Change")),
        (DELETION, _("Deletion")),
        (CREATION, _("Creation")),
        (VALIDATION, _("Validation")),
        (APPROVAL, _("Approval")),
        (REJECTION, _("Rejection")),
        (PROCESS, _("Process")),
        (CLOSING, _("Closing")),
        (CLONE, _("Clone")),
        (CONVERTION, _("Convertion")),
        (COMPLETION, _("Completion")),
        (CANCELATION, _("Cancelation")),
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        verbose_name=_("actor"),
    )
    timestamp = models.DateTimeField(
        _("action time"),
        default=timezone.now,
        editable=False,
    )
    action_object_type = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name="activities",
        on_delete=models.CASCADE,
    )
    action_object_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    action_object = GenericForeignKey(
        "action_object_type",
        "action_object_id",
    )
    action_flag = models.PositiveSmallIntegerField(
        _("action flag"),
        choices=ACTION_FLAGS,
    )

    note = models.TextField(
        _("activity note"),
        blank=True,
    )
    data = models.JSONField(
        _("activity data"),
        null=True,
        blank=True,
    )

    objects = ActivityManager()

    class Meta:
        db_table = "simpel_auth_activity"
        verbose_name = _("Activity")
        verbose_name_plural = _("Activities")
        index_together = ("timestamp", "actor", "action_flag")
        ordering = ["-timestamp"]

    def __str__(self):
        ctx = {
            "actor": self.actor,
            "verb": self.get_action_flag_display(),
            "action_object": self.action_object,
            "timesince": self.timesince(),
        }
        if self.action_object:
            return "%(actor)s %(verb)s %(action_object)s %(timesince)s ago" % ctx
        return "%(actor)s %(verb)s %(timesince)s ago" % ctx

    def timesince(self, now=None):
        """
        Shortcut for the ``django.utils.timesince.timesince`` function of the
        current timestamp.
        """
        from django.utils.timesince import timesince as timesince_

        return timesince_(self.timestamp, now)

    def __repr__(self):
        return str(self.timestamp)

    def is_addition(self):
        return self.action_flag == self.ADDITION

    def is_change(self):
        return self.action_flag == self.CHANGE

    def is_deletion(self):
        return self.action_flag == self.DELETION

    def get_note(self):
        """
        If self.note is a JSON structure, interpret it as a change
        string, properly translated.
        """
        if self.note and self.note[0] == "[":
            try:
                note = json.loads(self.note)
            except json.JSONDecodeError:
                return self.note
            notes = []
            for sub_note in note:
                if "added" in sub_note:
                    if sub_note["added"]:
                        sub_note["added"]["name"] = _(sub_note["added"]["name"])
                        notes.append(_("Added {name} “{object}”.").format(**sub_note["added"]))
                    else:
                        notes.append(_("Added."))

                if "created" in sub_note:
                    if sub_note["created"]:
                        sub_note["created"]["name"] = _(sub_note["created"]["name"])
                        notes.append(_("Created {name} “{object}”.").format(**sub_note["created"]))
                    else:
                        notes.append(_("Created."))

                if "validate" in sub_note:
                    if sub_note["validate"]:
                        sub_note["validate"]["name"] = _(sub_note["validate"]["name"])
                        notes.append(_("Validate {name} “{object}”.").format(**sub_note["validate"]))
                    else:
                        notes.append(_("Validate."))

                if "approve" in sub_note:
                    if sub_note["approve"]:
                        sub_note["approve"]["name"] = _(sub_note["approve"]["name"])
                        notes.append(_("Approve {name} “{object}”.").format(**sub_note["approve"]))
                    else:
                        notes.append(_("Approve."))

                if "reject" in sub_note:
                    if sub_note["reject"]:
                        sub_note["reject"]["name"] = _(sub_note["reject"]["name"])
                        notes.append(_("Reject {name} “{object}”.").format(**sub_note["reject"]))
                    else:
                        notes.append(_("Reject."))

                if "process" in sub_note:
                    if sub_note["process"]:
                        sub_note["process"]["name"] = _(sub_note["reject"]["name"])
                        notes.append(_("Process {name} “{object}”.").format(**sub_note["process"]))
                    else:
                        notes.append(_("Process."))

                elif "changed" in sub_note:
                    sub_note["changed"]["fields"] = get_text_list(
                        [_(field_name) for field_name in sub_note["changed"]["fields"]], _("and")
                    )
                    if "name" in sub_note["changed"]:
                        sub_note["changed"]["name"] = _(sub_note["changed"]["name"])
                        notes.append(_("Changed {fields} for {name} “{object}”.").format(**sub_note["changed"]))
                    else:
                        notes.append(_("Changed {fields}.").format(**sub_note["changed"]))

                elif "deleted" in sub_note:
                    sub_note["deleted"]["name"] = _(sub_note["deleted"]["name"])
                    notes.append(_("Deleted {name} “{object}”.").format(**sub_note["deleted"]))

            note = " ".join(msg[0].upper() + msg[1:] for msg in notes)
            return note or _("No fields changed.")
        else:
            return self.note

    def get_edited_object(self):
        """Return the edited object represented by this log entry."""
        return self.action_object_type.get_object_for_this_type(pk=self.action_object_id)

    def get_admin_url(self):
        """
        Return the admin URL to edit the object represented by this activity log.
        """
        if self.action_object_type and self.action_object_id:
            try:
                return reverse(
                    admin_urlname(self.action_object._meta, "change"),
                    args=(quote(self.action_object),),
                    host="admin",
                )
            except NoReverseMatch:
                pass
        return None


class Notification(models.Model):
    """
    Action model describing the actor acting out a verb (on an optional
    target).
    Nomenclature based on http://activitystrea.ms/specs/atom/1.0/

    Generalized Format::

        <actor> <verb> <time>
        <actor> <verb> <target> <time>
        <actor> <verb> <action_object> <target> <time>

    Examples::

        <justquick> <reached level 60> <1 minute ago>
        <brosner> <commented on> <pinax/pinax> <2 hours ago>
        <washingtontimes> <started follow> <justquick> <8 minutes ago>
        <mitsuhiko> <closed> <issue 70> on <mitsuhiko/flask> <about 2 hours ago>

    Unicode Representation::

        justquick reached level 60 1 minute ago
        mitsuhiko closed issue 70 on mitsuhiko/flask 3 hours ago

    HTML Representation::

        <a href="http://oebfare.com/">brosner</a> commented on <a href="http://github.com/pinax/pinax">pinax/pinax</a> 2 hours ago # noqa

    """

    LEVELS = utils.Choices("success", "info", "warning", "error")

    level = models.CharField(
        choices=LEVELS,
        default=LEVELS.info,
        max_length=20,
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=False,
        related_name="notifications",
        on_delete=models.CASCADE,
    )
    unread = models.BooleanField(
        default=True,
        blank=False,
        db_index=True,
    )

    actor_content_type = models.ForeignKey(
        ContentType,
        related_name="notify_actor",
        on_delete=models.CASCADE,
    )
    actor_object_id = models.CharField(
        max_length=255,
    )
    actor = GenericForeignKey(
        "actor_content_type",
        "actor_object_id",
    )

    verb = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    target_content_type = models.ForeignKey(
        ContentType,
        related_name="notify_target",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    target_object_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    target = GenericForeignKey(
        "target_content_type",
        "target_object_id",
    )

    action_object_content_type = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name="notify_action_object",
        on_delete=models.CASCADE,
    )
    action_object_object_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    action_object = GenericForeignKey(
        "action_object_content_type",
        "action_object_object_id",
    )

    timestamp = models.DateTimeField(
        default=timezone.now,
        db_index=True,
    )

    public = models.BooleanField(default=True, db_index=True)
    deleted = models.BooleanField(default=False, db_index=True)
    emailed = models.BooleanField(default=False, db_index=True)

    data = models.JSONField(blank=True, null=True)
    objects = NotificationQuerySet.as_manager()

    class Meta:
        ordering = ("-timestamp",)
        db_table = "simpel_auth_notification"
        index_together = ("recipient", "unread")

    def __str__(self):
        ctx = {
            "actor": self.actor,
            "verb": self.verb,
            "action_object": self.action_object,
            "target": self.target,
            "timesince": self.timesince(),
        }
        if self.target:
            if self.action_object:
                return "%(actor)s %(verb)s %(action_object)s on %(target)s %(timesince)s ago" % ctx
            return "%(actor)s %(verb)s %(target)s %(timesince)s ago" % ctx
        if self.action_object:
            return "%(actor)s %(verb)s %(action_object)s %(timesince)s ago" % ctx
        return "%(actor)s %(verb)s %(timesince)s ago" % ctx

    def timesince(self, now=None):
        """
        Shortcut for the ``django.utils.timesince.timesince`` function of the
        current timestamp.
        """
        from django.utils.timesince import timesince as timesince_

        return timesince_(self.timestamp, now)

    @property
    def slug(self):
        return id2slug(self.id)

    def mark_as_read(self):
        if self.unread:
            self.unread = False
            self.save()

    def mark_as_unread(self):
        if not self.unread:
            self.unread = True
            self.save()
