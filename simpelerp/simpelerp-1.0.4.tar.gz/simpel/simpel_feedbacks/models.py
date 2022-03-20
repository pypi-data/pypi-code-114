from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django_comments_xtd.models import XtdComment

User = get_user_model()


class UserComment(XtdComment):
    pass


class UserFlag(models.Model):
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    user = models.ForeignKey(
        User,
        related_name="flags",
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )
    flagged_object_type = models.ForeignKey(
        ContentType,
        related_name="flags",
        on_delete=models.CASCADE,
        help_text=_("Flagged object type"),
    )
    flagged_object_id = models.IntegerField(
        help_text=_("Flagged object primary key."),
    )
    flagged_object = GenericForeignKey(
        "flagged_object_type",
        "flagged_object_id",
    )

    icon = "comment-text-outline"

    class Meta:
        verbose_name = _("Flag")
        verbose_name_plural = _("Flags")
        index_together = ("flagged_object_id", "user")

    def __str__(self):
        return "%s flagged by %s" % (self.flagged_object, self.user)


class UserRating(models.Model):
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    user = models.ForeignKey(
        User,
        related_name="rated_objects",
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )
    rated_object_type = models.ForeignKey(
        ContentType,
        related_name="rates",
        on_delete=models.CASCADE,
        help_text=_("Rated object type"),
    )
    rated_object_id = models.IntegerField(
        help_text=_("Rated object primary key."),
    )
    rated_object = GenericForeignKey(
        "rated_object_type",
        "rated_object_id",
    )
    value = models.IntegerField(
        default=10,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
    )

    icon = "comment-bookmark-outline"

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")
        index_together = ("rated_object_id", "user")

    def __str__(self):
        return _("%s rated by %s") % (self.flagged_object, self.user)


class UserFeedback(models.Model):
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
    )
    user = models.ForeignKey(
        User,
        related_name="feedbacks",
        on_delete=models.CASCADE,
        verbose_name=_("User"),
    )
    feedback_object_type = models.ForeignKey(
        ContentType,
        related_name="feedbacks",
        on_delete=models.CASCADE,
        help_text=_("Object type"),
    )
    feedback_object_id = models.IntegerField(
        help_text=_("Object primary key."),
    )
    feedback_object = GenericForeignKey(
        "feedback_object_type",
        "feedback_object_id",
    )
    content = models.TextField(
        _("content"),
        help_text=_("Please provide feedback!"),
    )
    value = models.IntegerField(
        default=10,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
    )

    icon = "comment-check-outline"

    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")
        index_together = ("feedback_object_id", "user")

    def __str__(self):
        return _("%s feedback by %s") % (self.flagged_object, self.user)
