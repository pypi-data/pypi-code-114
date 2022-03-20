from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _
from django_hookup import core as hookup

from simpel.simpel_accounts.models import AccountType
from simpel.simpel_accounts.settings import simpel_accounts_settings
from simpel.simpel_accounts.utils import get_or_create_account

from .models import Parameter

names = simpel_accounts_settings.NAMES


class Lembaga(TextChoices):
    LABORATORIUM = "LAB", _("Laboratorium")
    INSPECTION = "LIT", _("Technical Inspection")
    CALIBRATION = "KAL", _("Calibration")
    CERTIFICATION = "PRO", _("Product Certification")
    CONSULTANCY = "KSL", _("Consultancy")
    RESEARCH = "LIB", _("Research and Development")
    TRAINING = "LAT", _("Training")
    SERVICE = "SRV", _("Service")


@hookup.register("REGISTER_DEMO_USERS")
def register_simpellab_demo_users():
    from simpellab.setup import init_demo_users

    init_demo_users()


@hookup.register("REGISTER_INITIAL_PERMISSIONS")
def register_simpellab_initial_perms():
    from simpellab.setup import init_permissions

    init_permissions()


@hookup.register("REGISTER_PRODUCT_CHILD_MODELS")
def register_parameter_service():
    return Parameter


@hookup.register("REGISTER_INITIAL_ACCOUNTS")
def register_baristand_accounts():
    pymhd_type, _ = AccountType.objects.get_or_create(name="PYMD")
    pymhd_type.save()
    pymhd_reverse_type, _ = AccountType.objects.get_or_create(name="PYMHD Reverse")
    pymhd_reverse_type.debit = AccountType.DECREASE
    pymhd_reverse_type.save()

    for name, value in Lembaga.choices:
        account, _ = get_or_create_account(
            name="Pendapatan %s" % value,
            code="%s.REV" % name,
            type_name=names["REVENUE"],
        )
        pymhd, _ = get_or_create_account(
            name="PYMHD %s" % value,
            code="%s.PYMHD" % name,
            type_name="PYMD",
        )
        pymhd_reverse, _ = get_or_create_account(
            name=value,
            code="%s.PYMHD.REV" % name,
            type_name="PYMHD Reverse",
        )
