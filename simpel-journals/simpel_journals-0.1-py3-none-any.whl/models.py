from decimal import Decimal

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType  # NOQA
from django.db import models, transaction
from django.db.models import Sum
from django.forms import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from polymorphic.managers import PolymorphicManager
from polymorphic.models import PolymorphicModel
from simpel_numerators.models import NumeratorMixin, NumeratorReset

from simpel_utils.models.fields import CustomGenericForeignKey

from .managers import ActiveAccountManager, ExpiredAccountManager, TransactionManager

LEN_SHORT = 128
LEN_LONG = 255


class AccountType(MPTTModel):
    INCREASE = 1
    DECREASE = -1
    DEBITS = (
        (INCREASE, _("Increase")),
        (DECREASE, _("Decrease")),
    )
    parent = TreeForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )
    debit = models.IntegerField(
        choices=DEBITS,
        default=INCREASE,
    )
    code = models.CharField(
        max_length=128,
        unique=True,
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=255,
    )

    class Meta:
        db_table = "simpel_accounting_account_type"
        verbose_name = _("Account Type")
        verbose_name_plural = _("Account Types")

    def __str__(self):
        return self.name

    @property
    def full_name(self):
        names = [a.name for a in self.get_ancestors()]
        names.append(self.name)
        return " / ".join(names)

    def clean(self):
        if self.parent:
            parent = self.parent
            if self.parent == self:
                raise ValidationError("Parent type cannot be self.")
            if parent.parent and parent.parent == self:
                raise ValidationError("Cannot have circular Parents.")

    def save(self, *args, **kwargs):
        parent = getattr(self, "parent", None)
        if parent:
            self.debit = parent.debit
        return super().save(*args, **kwargs)


class Account(PolymorphicModel):

    account_type = TreeForeignKey(
        AccountType,
        models.CASCADE,
        related_name="accounts",
        null=True,
    )
    created_at = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Created at"),
    )

    last_modified_at = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        verbose_name=_("Created at"),
    )

    start_date = models.DateTimeField(
        null=True,
        blank=True,
    )
    end_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    code = models.CharField(
        max_length=128,
        unique=True,
        null=True,
        blank=True,
    )
    linked_object_type = models.ForeignKey(
        ContentType,
        related_name="accounts",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_("Linked instance type"),
    )
    linked_object_id = models.IntegerField(null=True, blank=True, help_text=_("Linked instance primary key."))
    linked_object = GenericForeignKey("linked_object_type", "linked_object_id")

    name = models.CharField(
        max_length=128,
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_("This text is shown to customers during checkout"),
    )

    # Track the status of a account - this is often used so that expired
    # account can have their money transferred back to some parent account and
    # then be closed.
    OPEN, FROZEN, CLOSED = "Open", "Frozen", "Closed"
    STATUS = (
        (OPEN, _("Open")),
        (FROZEN, _("Frozen")),
        (CLOSED, _("Closed")),
    )
    status = models.CharField(max_length=32, choices=STATUS, default=OPEN)

    # This is the limit to which the account can go into debt.  The default is
    # zero which means the account cannot run a negative balance.  A 'source'
    # account will have no credit limit meaning it can transfer funds to other
    # accounts without limit.
    credit_limit = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        default=Decimal("0.00"),
        null=True,
        blank=True,
    )
    balance = models.DecimalField(
        default=0,
        max_digits=15,
        decimal_places=2,
        editable=False,
        verbose_name=_("Balance"),
    )
    objects = PolymorphicManager()
    active = ActiveAccountManager()
    expired = ExpiredAccountManager()

    class Meta:
        db_table = "simpel_accounting_account"
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")

    @property
    def has_credit_limit(self):
        return self.credit_limit is not None

    @property
    def is_open(self):
        return self.status == Account.OPEN

    @property
    def is_closed(self):
        return self.status == Account.CLOSED

    @property
    def is_frozen(self):
        return self.status == Account.FROZEN

    def __str__(self):
        name = _("Anonymous")
        if self.name:
            name = self.name
        return "%s (%s)" % (name, self.account_type)

    def is_active(self):
        if self.start_date is None and self.end_date is None:
            return True
        now = timezone.now()
        if self.start_date and self.end_date is None:
            return now >= self.start_date
        if self.start_date is None and self.end_date:
            return now < self.end_date
        return self.start_date <= now < self.end_date

    def get_balance(self):
        # For performance, we keep a cached balance.  This can always be
        # recalculated from the account transactions.
        aggregates = self.entries.filter(status=Transaction.CONFIRMED).aggregate(sum=Sum("computed_amount"))
        sum = aggregates["sum"]
        balance = Decimal("0.00") if sum is None else sum
        return self.account_type.debit * balance

    def num_entries(self):
        return self.entries.filter(status=Transaction.CONFIRMED).count()

    def compute(self):
        self.balance = self.get_balance()
        self.last_modified = timezone.now()

    def clean(self):
        if self.linked_object_type is not None and self.linked_object is None:
            raise ValidationError({"linked_object_id": _("Reference not found.")})

    def save(self, *args, **kwargs):
        if self.code:
            self.code = self.code.upper()
        # Ensure the balance is always correct when saving
        self.compute()
        return super().save(*args, **kwargs)


class TransactionType(MPTTModel):
    parent = TreeForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )
    code = models.CharField(
        unique=True,
        max_length=3,
        verbose_name=_("Code"),
        help_text=_("This unique code will used as Transaction Inner ID prefix eg: TRX.0202.001"),
    )
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Description"),
    )

    class Meta:
        db_table = "simpel_accounting_transaction_type"
        verbose_name = _("Transaction Type")
        verbose_name_plural = _("Transaction Types")

    def __str__(self):
        return "%s: %s" % (self.code, self.name)

    def clean(self):
        if self.parent:
            parent = self.parent
            if self.parent == self:
                raise ValidationError("Parent type cannot be self.")
            if parent.parent and parent.parent == self:
                raise ValidationError("Cannot have circular Parents.")


class Transaction(PolymorphicModel, NumeratorMixin):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCEL = "canceled"

    CHOICES = [
        (PENDING, _("Pending")),
        (CONFIRMED, _("Confirmed")),
        (CANCEL, _("Canceled")),
    ]
    type = TreeForeignKey(
        TransactionType,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="transactions",
        verbose_name=_("Type"),
    )
    status = models.CharField(
        max_length=15,
        choices=CHOICES,
        default=PENDING,
        verbose_name=_("Status"),
    )
    group = models.CharField(
        max_length=3,
        null=True,
        blank=True,
        verbose_name=_("Group"),
    )

    reference_type = models.ForeignKey(
        ContentType,
        null=True,
        blank=True,
        limit_choices_to={"model__in": ["salesorder", "invoice", "payment"]},
        on_delete=models.SET_NULL,
    )
    reference_id = models.CharField(
        max_length=255,
        verbose_name=_("Reference"),
    )
    reference = CustomGenericForeignKey(
        "reference_type",
        "reference_id",
        "inner_id",
    )

    note = models.CharField(
        max_length=LEN_LONG,
        null=True,
        blank=True,
        verbose_name=_("Memo"),
    )
    objects = TransactionManager()
    doc_prefix = "TRX"
    reset_mode = NumeratorReset.MONTHLY

    class Meta:
        db_table = "simpel_accounting_transaction"
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
        index_together = ("created_at", "inner_id", "status")

    def __str__(self):
        return str(self.inner_id)

    def format_inner_id(self):
        """Inner ID final format"""
        form = [self.get_doc_prefix(), self.format_date(form="%m%y"), self.format_number()]
        inner_id = "{}.{}.{}".format(*form)
        return setattr(self, self.inner_id_field, inner_id)

    @transaction.atomic
    def confirm(self):
        if self.status != Transaction.PENDING:
            raise PermissionError(_("can't confirm transaction #%s") % self.inner_id)
        else:
            self.status = Transaction.CONFIRMED
            self.save()

    @transaction.atomic
    def cancel(self):
        self.status = Transaction.CANCEL
        self.save()

    def get_doc_prefix(self):
        if self.type is not None:
            return self.type.code
        return super().get_doc_prefix()

    def compute(self):
        for entry in self.entries.all():
            entry.save()
            entry.account.save()

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)


class EntryManager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class Entry(models.Model):
    DEBIT = 1
    CREDIT = -1
    FLOW = (
        (DEBIT, _("Debit")),
        (CREDIT, _("Credit")),
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False,
        db_index=True,
    )
    trx = models.ForeignKey(
        Transaction,
        models.CASCADE,
        verbose_name=_("Transaction"),
        related_name="entries",
        db_index=True,
    )
    account = models.ForeignKey(
        Account,
        models.CASCADE,
        related_name="entries",
        db_index=True,
    )
    flow = models.IntegerField(choices=FLOW)
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
    )
    computed_amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
    )
    objects = EntryManager()
    status = models.CharField(
        max_length=15,
        choices=Transaction.CHOICES,
        default=Transaction.PENDING,
        verbose_name=_("Status"),
    )

    class Meta:
        db_table = "simpel_accounting_entry"
        index_together = ("id", "trx", "account")
        unique_together = ("trx", "account")
        verbose_name = _("Entry")
        verbose_name_plural = _("Entries")

    def __str__(self):
        return "Ref: %s, amount: %.2f" % (self.trx.reference, self.amount)

    def delete(self, *args, **kwargs):
        raise RuntimeError("Entries cannot be deleted")

    def reference(self):
        return self.trx.reference

    def note(self):
        return self.trx.note

    def debit(self):
        return Decimal("0.00") if self.flow == Entry.CREDIT else self.amount

    def credit(self):
        return Decimal("0.00") if self.flow == Entry.DEBIT else self.amount

    def get_computed_amount(self):
        # The sum of this field over the whole table should always be 0.
        # Debits should be positive while credits should be negative
        return self.amount * self.flow

    def compute(self):
        self.status = self.trx.status
        self.computed_amount = self.get_computed_amount()

    def save(self, *args, **kwargs):
        self.compute()
        return super().save(*args, **kwargs)
