from functools import cached_property

from django.apps import apps
from django.db import models, transaction
from django.utils import timezone, translation
from django_numerators.models import NumeratorMixin as NumeratorMixinBase
from django_numerators.models import NumeratorReset

from .. import const, signals

_ = translation.gettext_lazy


class NumeratorMixin(NumeratorMixinBase):
    reset_mode = NumeratorReset.MONTHLY

    def format_inner_id(self):
        """Inner ID final format"""
        form = [self.get_doc_prefix(), self.format_date(form="%m%y"), self.format_number()]
        inner_id = "{}.{}.{}".format(*form)
        return setattr(self, self.inner_id_field, inner_id)

    class Meta:
        abstract = True


class ContentTypeMixin(models.Model):
    contenttype_id = models.IntegerField(
        null=True,
        blank=True,
        db_index=True,
    )
    contenttype_slug = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        db_index=True,
    )

    class Meta:
        abstract = True

    @cached_property
    def contenttype(self):
        try:
            return apps.get_model(self.contenttype_slug)
        except LookupError:
            return self.__class__

    @cached_property
    def contenttype_opts(self):
        return self.contenttype._meta


class StatusMessage(models.Model):
    class Meta:
        abstract = True

    @property
    def opts(self):
        return self.__class__._meta

    def get_error_msg(self, action):
        msg = _("{}, {} is {}, it can't be {}.")
        return str(msg).format(
            self.opts.verbose_name,
            self,
            self.get_status_display(),
            action,
        )


class TrashMixin(StatusMessage, models.Model):

    date_trashed = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date trashed"),
    )

    class Meta:
        abstract = True

    @property
    def is_trash(self):
        """Check order status is trashed"""
        return self.status == const.TRASH

    @property
    def trash_ignore_condition(self):
        raise NotImplementedError

    @property
    def trash_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def trash(self, request=None):
        """Trash drafted order"""
        if self.trash_ignore_condition:
            return
        if self.trash_valid_condition:
            signals.pre_trash.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.TRASH
            self.date_trashed = timezone.now()
            self.save()
            signals.post_trash.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("trash"))


class DraftMixin(StatusMessage, models.Model):

    date_drafted = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date drafted"),
    )

    class Meta:
        abstract = True

    @property
    def is_draft(self):
        """Check order status is draft"""
        return self.status == const.DRAFT

    @property
    def draft_ignore_condition(self):
        raise NotImplementedError

    @property
    def draft_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def draft(self, request=None):
        """Draft trashed"""
        if self.draft_ignore_condition:
            return
        if self.draft_valid_condition:
            signals.pre_draft.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.DRAFT
            self.date_drafted = timezone.now()
            self.save()
            signals.post_draft.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("draft"))


class PendingMixin(StatusMessage, models.Model):

    date_pending = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date pending"),
    )

    class Meta:
        abstract = True

    @property
    def is_pending(self):
        """Check order status is pending"""
        return self.status == const.PENDING

    @transaction.atomic
    def pending(self, request=None):
        """pending trashed"""
        if self.is_pending:
            return
        if self.is_trash:
            self.status = const.PENDING
            self.date_pending = timezone.now()
            self.save()
        else:
            raise PermissionError(self.get_error_msg("pending"))


class ValidateMixin(StatusMessage, models.Model):

    date_validated = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date validated"),
    )

    class Meta:
        abstract = True

    @property
    def is_valid(self):
        """Check order status is valid"""
        return self.status == const.VALID

    @property
    def validate_ignore_condition(self):
        raise NotImplementedError

    @property
    def validate_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def validate(self, request=None):
        """Validate drafted order"""
        if self.validate_ignore_condition:
            return
        if self.validate_valid_condition:
            signals.pre_validate.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.VALID
            self.date_validated = timezone.now()
            self.save()
            signals.post_validate.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("validated"))


class CancelMixin(StatusMessage, models.Model):

    date_canceled = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date canceled"),
    )

    class Meta:
        abstract = True

    @property
    def is_canceled(self):
        """Check order status is canceled"""
        return self.status == const.CANCELED

    @property
    def cancel_ignore_condition(self):
        raise NotImplementedError

    @property
    def cancel_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def cancel(self, request=None):
        """Validate drafted order"""
        if self.cancel_ignore_condition:
            return
        if self.cancel_valid_condition:
            signals.pre_cancel.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.CANCELED
            self.date_canceled = timezone.now()
            self.save()
            signals.post_cancel.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("canceled"))


class ApproveMixin(StatusMessage, models.Model):

    date_approved = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date approved"),
    )

    class Meta:
        abstract = True

    @property
    def is_approved(self):
        """Check order status is approved"""
        return self.status == const.APPROVED

    @property
    def approve_ignore_condition(self):
        raise NotImplementedError

    @property
    def approve_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def approve(self, request=None):
        """Approve valid order"""
        if self.approve_ignore_condition:
            return
        if self.approve_valid_condition:
            signals.pre_approve.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.APPROVED
            self.date_approved = timezone.now()
            self.save()
            signals.post_approve.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("approved"))


class RejectMixin(StatusMessage, models.Model):

    date_rejected = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date rejected"),
    )

    class Meta:
        abstract = True

    @property
    def is_rejected(self):
        """Check order status is rejected"""
        return self.status == const.REJECTED

    @property
    def reject_ignore_condition(self):
        raise NotImplementedError

    @property
    def reject_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def reject(self, request=None):
        """Reject valid order"""
        if self.reject_ignore_condition:
            return
        if self.reject_valid_condition:
            signals.post_reject.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.REJECTED
            self.date_rejected = timezone.now()
            self.save()
            signals.post_reject.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("rejected"))


class CompleteMixin(StatusMessage, models.Model):

    date_completed = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date completed"),
    )

    class Meta:
        abstract = True

    @property
    def is_complete(self):
        """Check order status is complete"""
        return self.status == const.COMPLETE

    @property
    def complete_ignore_condition(self):
        raise NotImplementedError

    @property
    def complete_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def complete(self, request=None):
        """Complete validated order"""
        if self.complete_ignore_condition:
            return
        if self.complete_valid_condition:
            signals.pre_complete.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.COMPLETE
            self.date_completed = timezone.now()
            self.save()
            signals.post_complete.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("completed"))


class ProcessMixin(StatusMessage, models.Model):

    date_processed = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date processed"),
    )

    class Meta:
        abstract = True

    @property
    def is_processed(self):
        """Check order status is processed"""
        return self.status == const.PROCESSED

    @property
    def process_ignore_condition(self):
        raise NotImplementedError

    @property
    def process_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def process(self, request=None):
        """Process valid order"""
        if self.process_ignore_condition:
            return
        if self.process_valid_condition:
            signals.pre_process.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.PROCESSED
            self.date_processed = timezone.now()
            self.save()
            signals.post_process.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("processed"))


class PaidMixin(StatusMessage, models.Model):

    date_paid = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date paid"),
    )

    class Meta:
        abstract = True

    @property
    def is_paid(self):
        return self.status == const.REJECTED

    @property
    def pay_ignore_condition(self):
        raise NotImplementedError

    @property
    def pay_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def pay(self, request=None):
        """Paid pending order"""
        if self.pay_ignore_condition:
            return
        if self.pay_valid_condition:
            signals.pre_pay.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.PAID
            self.date_paid = timezone.now()
            self.save()
            signals.post_pay.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("paid"))


class CloseMixin(StatusMessage, models.Model):

    date_closed = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date closed"),
    )

    class Meta:
        abstract = True

    @property
    def is_closed(self):
        """Check object is closed"""
        return self.status == const.CLOSED

    @property
    def close_ignore_condition(self):
        raise NotImplementedError

    @property
    def close_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def close(self, request=None):
        """Close the order"""
        if self.close_ignore_condition:
            return
        if self.close_valid_condition:
            signals.pre_close.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.CLOSED
            self.date_closed = timezone.now()
            self.save()
            signals.post_close.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("closed"))


class ArchiveMixin(StatusMessage, models.Model):

    date_archived = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("date archived"),
    )

    class Meta:
        abstract = True

    @property
    def is_archived(self):
        """Check order status is archived"""
        return self.status == const.ARCHIVED

    @property
    def archive_ignore_condition(self):
        raise NotImplementedError

    @property
    def archive_valid_condition(self):
        raise NotImplementedError

    @transaction.atomic
    def archive(self, request=None):
        """Archive the object"""
        if self.archive_ignore_condition:
            return
        if self.archive_valid_condition:
            signals.pre_archive.send(sender=self.__class__, instance=self, actor=request.user, request=request)
            self.status = const.ARCHIVED
            self.date_archived = timezone.now()
            self.save()
            signals.post_archive.send(sender=self.__class__, instance=self, actor=request.user, request=request)
        else:
            raise PermissionError(self.get_error_msg("archived"))


class StatusMixin(models.Model):
    """Base for status mixin used in sales order,
    warehouse transfer or invoice"""

    status = NotImplementedError

    class Meta:
        abstract = True

    @property
    def is_editable(self):
        """Check order is editable"""
        return self.is_trash or self.is_draft


class ThreeStepStatusMixin(
    DraftMixin,
    TrashMixin,
    ValidateMixin,
    CompleteMixin,
    StatusMixin,
):
    """Give model status three step status tracking and action,
    draft -> validate or trash -> complete
    """

    STATUS_CHOICES = (
        (const.DRAFT, _("Draft")),
        (const.TRASH, _("Trash")),
        (const.VALID, _("Valid")),
        (const.COMPLETE, _("Complete")),
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=const.DRAFT)

    class Meta:
        abstract = True

    @property
    def validate_valid_condition(self):
        return self.is_draft

    @property
    def validate_ignore_condition(self):
        return self.is_valid

    @property
    def complete_ignore_condition(self):
        return self.is_complete

    @property
    def complete_valid_condition(self):
        return self.is_valid


class FourStepStatusMixin(
    DraftMixin,
    TrashMixin,
    ValidateMixin,
    ProcessMixin,
    CompleteMixin,
    StatusMixin,
):
    """Give model status three step status tracking and action,
    draft -> validate or trash -> process -> complete
    """

    STATUS_CHOICES = (
        (const.DRAFT, _("Draft")),
        (const.TRASH, _("Trash")),
        (const.VALID, _("Valid")),
        (const.APPROVED, _("Approved")),
        (const.PROCESSED, _("Processed")),
        (const.COMPLETE, _("Complete")),
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=const.DRAFT)

    class Meta:
        abstract = True

    @property
    def validate_ignore_condition(self):
        return self.is_valid

    @property
    def validate_valid_condition(self):
        return self.is_draft

    @property
    def process_ignore_condition(self):
        return self.is_processed

    @property
    def process_valid_condition(self):
        return self.is_valid

    @property
    def complete_ignore_condition(self):
        return self.is_complete

    @property
    def complete_valid_condition(self):
        return self.is_valid


class FiveStepStatusMixin(
    DraftMixin,
    TrashMixin,
    ValidateMixin,
    ApproveMixin,
    RejectMixin,
    ProcessMixin,
    CompleteMixin,
    StatusMixin,
):
    """Give model status three step status tracking and action,
    draft -> validate or trash -> approve/reject -> process -> complete
    """

    STATUS_CHOICES = (
        (const.DRAFT, _("Draft")),
        (const.TRASH, _("Trash")),
        (const.VALID, _("Valid")),
        (const.APPROVED, _("Approved")),
        (const.REJECTED, _("Rejected")),
        (const.PROCESSED, _("Processed")),
        (const.COMPLETE, _("Complete")),
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=const.DRAFT)

    class Meta:
        abstract = True

    @property
    def validate_ignore_condition(self):
        return self.is_valid

    @property
    def validate_valid_condition(self):
        return self.is_draft

    @property
    def approve_ignore_condition(self):
        return self.is_approved

    @property
    def approve_valid_condition(self):
        return self.is_valid

    @property
    def reject_ignore_condition(self):
        return self.is_rejected

    @property
    def reject_valid_condition(self):
        return self.is_valid

    @property
    def process_ignore_condition(self):
        return self.is_processed

    @property
    def process_valid_condition(self):
        return self.is_approved

    @property
    def complete_ignore_condition(self):
        return self.is_complete

    @property
    def complete_valid_condition(self):
        return self.is_processed
