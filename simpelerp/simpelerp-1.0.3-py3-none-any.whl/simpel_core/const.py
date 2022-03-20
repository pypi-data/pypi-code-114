from django.db.models import TextChoices
from django.utils.translation import ugettext_lazy as _


class Departments(TextChoices):
    LABORATORIUM = "LAB", _("Laboratorium")
    INSPECTION = "LIT", _("Technical Inspection")
    CALIBRATION = "KAL", _("Calibration")
    CERTIFICATION = "PRO", _("Product Certification")
    CONSULTANCY = "KSL", _("Consultancy")
    RESEARCH = "LIB", _("Research and Development")
    TRAINING = "LAT", _("Training")
    SERVICE = "SRV", _("Service")

    __empty__ = _("Not Set")


# WEEKDAY CONSTS
(
    MONDAY,
    TUESDAY,
    WEDNESDAY,
    THURSDAY,
    FRIDAY,
    SATURDAY,
    SUNDAY,
    # DEPARTMENT
    LABORATORIUM,
    INSPECTION,
    CALIBRATION,
    CERTIFICATION,
    CONSULTANCY,
    RESEARCH,
    TRAINING,
    MISC,
    # STATUS CONSTS
    TRASH,
    DRAFT,
    VALID,
    APPROVED,
    REJECTED,
    PROCESSED,
    COMPLETE,
    INVOICED,
    PENDING,
    UNPAID,
    PAID,
    CLOSED,
    POSTED,
    ARCHIVED,
    ACTIVE,
    INACTIVE,
    # PRIVACY CONSTS
    ME,
    USERS,
    FRIENDS,
    STUDENTS,
    TEACHERS,
    EMPLOYEES,
    MANAGERS,
    ANYONE,
    # NEW STATUS
    EXPIRED,
    CANCELED,
) = range(41)

DEPARTMENT_CHOICHES = (
    LABORATORIUM,
    INSPECTION,
    CALIBRATION,
    CERTIFICATION,
    CONSULTANCY,
    RESEARCH,
    TRAINING,
    MISC,
)

WEEKDAY_CHOICES = (
    (MONDAY, _("Monday")),
    (TUESDAY, _("Tesday")),
    (WEDNESDAY, _("Wednesday")),
    (THURSDAY, _("Thursday")),
    (FRIDAY, _("Friday")),
    (SATURDAY, _("Saturday")),
    (SUNDAY, _("Sunday")),
)

STATUS_CHOICES = (
    (TRASH, _("Trash")),
    (DRAFT, _("Draft")),
    (VALID, _("Valid")),
    (APPROVED, _("Approved")),
    (REJECTED, _("Rejected")),
    (PROCESSED, _("Processed")),
    (COMPLETE, _("Complete")),
    (INVOICED, _("invoiced")),
    (PENDING, _("Pending")),
    (UNPAID, _("Unpaid")),
    (PAID, _("Paid")),
    (CLOSED, _("Closed")),
    (POSTED, _("Posted")),
    (ARCHIVED, _("Archived")),
    (EXPIRED, _("Expired")),
    (ACTIVE, _("Active")),
    (INACTIVE, _("Banned")),
)


PRIVACY_CHOICES = (
    (ME, _("Only Me")),
    (USERS, _("Users")),
    (FRIENDS, _("Friends")),
    (STUDENTS, _("Students")),
    (TEACHERS, _("Teachers")),
    (EMPLOYEES, _("Employees")),
    (MANAGERS, _("Managers")),
    (ANYONE, _("Anyone")),
)
