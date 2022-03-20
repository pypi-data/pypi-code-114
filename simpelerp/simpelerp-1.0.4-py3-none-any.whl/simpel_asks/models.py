from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import Tag, TaggedItemBase


class Question(models.Model):

    OPEN = 1
    SPAM = 2
    CLOSED = 3
    SOLVED = 4
    STATUS = (
        (OPEN, _("Open")),
        (SPAM, _("Spam")),
        (CLOSED, _("Closed")),
    )
    user = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        related_name="questions",
        on_delete=models.SET_NULL,
    )
    title = models.CharField(_("title"), max_length=255)
    text = models.TextField(_("Text"))
    tags = TaggableManager(
        through="TaggedQuestion",
        blank=True,
        related_name="questions",
        verbose_name=_("Tags"),
    )
    status = models.IntegerField(choices=STATUS, default=OPEN)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(default=timezone.now, editable=False)
    last_viewed_at = models.DateTimeField(default=timezone.now, editable=False)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return super().__str__()


class TaggedQuestion(TaggedItemBase):

    content_object = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="tagged_questions",
        db_index=True,
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="tagged_questions",
        db_index=True,
    )

    class Meta:
        verbose_name = _("Tagged Question")
        verbose_name_plural = _("Tagged Questions")

    def __str__(self):
        return str(self.tag)
