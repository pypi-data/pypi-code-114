from functools import cached_property

from django.db import models
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField
from simpel_utils.models.fields import NullCharField, UppercaseCharField

from .settings import contacts_settings

REQUIRED_ADDRESS_FIELDS = contacts_settings.REQUIRED_ADDRESS_FIELDS


class AbstractContact(models.Model):
    PHONE = "phone"
    MOBILE = "mobile"
    FAX = "fax"
    WHATSAPP = "whatsapp"
    TELEGRAM = "telegram"

    CONTACT_TYPES = (
        (PHONE, _("Phone")),
        (FAX, _("Fax")),
        (MOBILE, _("Mobile")),
        (WHATSAPP, _("Whatsapp")),
        (TELEGRAM, _("Telegram")),
    )

    contact_type = models.CharField(
        max_length=255,
        choices=CONTACT_TYPES,
        default=PHONE,
        verbose_name=_("type"),
        help_text=_("E.g. Phone or mobile"),
    )
    contact = PhoneNumberField(
        _("Phone number"),
        blank=True,
        help_text=_("Contact number"),
    )
    is_verified = models.BooleanField(
        default=False,
        editable=False,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return "(%s) %s" % (self.contact_type.title(), self.contact)

    def to_dict(self):
        return {
            "contact_type": self.primary,
            "contact": self.address_type,
            "is_verified": self.name,
        }


class AbstractAddress(models.Model):
    """
    Superclass address object

    This is subclassed and extended to provide models for
    user, shipping and billing addresses.
    """

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

    MR, MISS, MRS, MS, DR = ("Mr", "Miss", "Mrs", "Ms", "Dr")
    TITLE_CHOICES = (
        (MR, _("Mr")),
        (MISS, _("Miss")),
        (MRS, _("Mrs")),
        (MS, _("Ms")),
        (DR, _("Dr")),
    )

    POSTCODE_REQUIRED = "postcode" in REQUIRED_ADDRESS_FIELDS

    # Regex for each country. Not listed countries don't use postcodes
    # Based on http://en.wikipedia.org/wiki/List_of_postal_codes
    POSTCODES_REGEX = {
        "AC": r"^[A-Z]{4}[0-9][A-Z]$",
        "AD": r"^AD[0-9]{3}$",
        "AF": r"^[0-9]{4}$",
        "AI": r"^AI-2640$",
        "AL": r"^[0-9]{4}$",
        "AM": r"^[0-9]{4}$",
        "AR": r"^([0-9]{4}|[A-Z][0-9]{4}[A-Z]{3})$",
        "AS": r"^[0-9]{5}(-[0-9]{4}|-[0-9]{6})?$",
        "AT": r"^[0-9]{4}$",
        "AU": r"^[0-9]{4}$",
        "AX": r"^[0-9]{5}$",
        "AZ": r"^AZ[0-9]{4}$",
        "BA": r"^[0-9]{5}$",
        "BB": r"^BB[0-9]{5}$",
        "BD": r"^[0-9]{4}$",
        "BE": r"^[0-9]{4}$",
        "BG": r"^[0-9]{4}$",
        "BH": r"^[0-9]{3,4}$",
        "BL": r"^[0-9]{5}$",
        "BM": r"^[A-Z]{2}([0-9]{2}|[A-Z]{2})",
        "BN": r"^[A-Z]{2}[0-9]{4}$",
        "BO": r"^[0-9]{4}$",
        "BR": r"^[0-9]{5}(-[0-9]{3})?$",
        "BT": r"^[0-9]{3}$",
        "BY": r"^[0-9]{6}$",
        "CA": r"^[A-Z][0-9][A-Z][0-9][A-Z][0-9]$",
        "CC": r"^[0-9]{4}$",
        "CH": r"^[0-9]{4}$",
        "CL": r"^([0-9]{7}|[0-9]{3}-[0-9]{4})$",
        "CN": r"^[0-9]{6}$",
        "CO": r"^[0-9]{6}$",
        "CR": r"^[0-9]{4,5}$",
        "CU": r"^[0-9]{5}$",
        "CV": r"^[0-9]{4}$",
        "CX": r"^[0-9]{4}$",
        "CY": r"^[0-9]{4}$",
        "CZ": r"^[0-9]{5}$",
        "DE": r"^[0-9]{5}$",
        "DK": r"^[0-9]{4}$",
        "DO": r"^[0-9]{5}$",
        "DZ": r"^[0-9]{5}$",
        "EC": r"^EC[0-9]{6}$",
        "EE": r"^[0-9]{5}$",
        "EG": r"^[0-9]{5}$",
        "ES": r"^[0-9]{5}$",
        "ET": r"^[0-9]{4}$",
        "FI": r"^[0-9]{5}$",
        "FK": r"^[A-Z]{4}[0-9][A-Z]{2}$",
        "FM": r"^[0-9]{5}(-[0-9]{4})?$",
        "FO": r"^[0-9]{3}$",
        "FR": r"^[0-9]{5}$",
        "GA": r"^[0-9]{2}.*[0-9]{2}$",
        "GB": r"^[A-Z][A-Z0-9]{1,3}[0-9][A-Z]{2}$",
        "GE": r"^[0-9]{4}$",
        "GF": r"^[0-9]{5}$",
        "GG": r"^([A-Z]{2}[0-9]{2,3}[A-Z]{2})$",
        "GI": r"^GX111AA$",
        "GL": r"^[0-9]{4}$",
        "GP": r"^[0-9]{5}$",
        "GR": r"^[0-9]{5}$",
        "GS": r"^SIQQ1ZZ$",
        "GT": r"^[0-9]{5}$",
        "GU": r"^[0-9]{5}$",
        "GW": r"^[0-9]{4}$",
        "HM": r"^[0-9]{4}$",
        "HN": r"^[0-9]{5}$",
        "HR": r"^[0-9]{5}$",
        "HT": r"^[0-9]{4}$",
        "HU": r"^[0-9]{4}$",
        "ID": r"^[0-9]{5}$",
        "IL": r"^([0-9]{5}|[0-9]{7})$",
        "IM": r"^IM[0-9]{2,3}[A-Z]{2}$$",
        "IN": r"^[0-9]{6}$",
        "IO": r"^[A-Z]{4}[0-9][A-Z]{2}$",
        "IQ": r"^[0-9]{5}$",
        "IR": r"^[0-9]{5}-[0-9]{5}$",
        "IS": r"^[0-9]{3}$",
        "IT": r"^[0-9]{5}$",
        "JE": r"^JE[0-9]{2}[A-Z]{2}$",
        "JM": r"^JM[A-Z]{3}[0-9]{2}$",
        "JO": r"^[0-9]{5}$",
        "JP": r"^[0-9]{3}-?[0-9]{4}$",
        "KE": r"^[0-9]{5}$",
        "KG": r"^[0-9]{6}$",
        "KH": r"^[0-9]{5}$",
        "KR": r"^[0-9]{5}$",
        "KY": r"^KY[0-9]-[0-9]{4}$",
        "KZ": r"^[0-9]{6}$",
        "LA": r"^[0-9]{5}$",
        "LB": r"^[0-9]{8}$",
        "LI": r"^[0-9]{4}$",
        "LK": r"^[0-9]{5}$",
        "LR": r"^[0-9]{4}$",
        "LS": r"^[0-9]{3}$",
        "LT": r"^(LT-)?[0-9]{5}$",
        "LU": r"^[0-9]{4}$",
        "LV": r"^LV-[0-9]{4}$",
        "LY": r"^[0-9]{5}$",
        "MA": r"^[0-9]{5}$",
        "MC": r"^980[0-9]{2}$",
        "MD": r"^MD-?[0-9]{4}$",
        "ME": r"^[0-9]{5}$",
        "MF": r"^[0-9]{5}$",
        "MG": r"^[0-9]{3}$",
        "MH": r"^[0-9]{5}$",
        "MK": r"^[0-9]{4}$",
        "MM": r"^[0-9]{5}$",
        "MN": r"^[0-9]{5}$",
        "MP": r"^[0-9]{5}$",
        "MQ": r"^[0-9]{5}$",
        "MT": r"^[A-Z]{3}[0-9]{4}$",
        "MV": r"^[0-9]{4,5}$",
        "MX": r"^[0-9]{5}$",
        "MY": r"^[0-9]{5}$",
        "MZ": r"^[0-9]{4}$",
        "NA": r"^[0-9]{5}$",
        "NC": r"^[0-9]{5}$",
        "NE": r"^[0-9]{4}$",
        "NF": r"^[0-9]{4}$",
        "NG": r"^[0-9]{6}$",
        "NI": r"^[0-9]{5}$",
        "NL": r"^[0-9]{4}[A-Z]{2}$",
        "NO": r"^[0-9]{4}$",
        "NP": r"^[0-9]{5}$",
        "NZ": r"^[0-9]{4}$",
        "OM": r"^[0-9]{3}$",
        "PA": r"^[0-9]{6}$",
        "PE": r"^[0-9]{5}$",
        "PF": r"^[0-9]{5}$",
        "PG": r"^[0-9]{3}$",
        "PH": r"^[0-9]{4}$",
        "PK": r"^[0-9]{5}$",
        "PL": r"^[0-9]{2}-?[0-9]{3}$",
        "PM": r"^[0-9]{5}$",
        "PN": r"^[A-Z]{4}[0-9][A-Z]{2}$",
        "PR": r"^[0-9]{5}$",
        "PT": r"^[0-9]{4}(-?[0-9]{3})?$",
        "PW": r"^[0-9]{5}$",
        "PY": r"^[0-9]{4}$",
        "RE": r"^[0-9]{5}$",
        "RO": r"^[0-9]{6}$",
        "RS": r"^[0-9]{5}$",
        "RU": r"^[0-9]{6}$",
        "SA": r"^[0-9]{5}$",
        "SD": r"^[0-9]{5}$",
        "SE": r"^[0-9]{5}$",
        "SG": r"^([0-9]{2}|[0-9]{4}|[0-9]{6})$",
        "SH": r"^(STHL1ZZ|TDCU1ZZ)$",
        "SI": r"^(SI-)?[0-9]{4}$",
        "SK": r"^[0-9]{5}$",
        "SM": r"^[0-9]{5}$",
        "SN": r"^[0-9]{5}$",
        "SV": r"^01101$",
        "SZ": r"^[A-Z][0-9]{3}$",
        "TC": r"^TKCA1ZZ$",
        "TD": r"^[0-9]{5}$",
        "TH": r"^[0-9]{5}$",
        "TJ": r"^[0-9]{6}$",
        "TM": r"^[0-9]{6}$",
        "TN": r"^[0-9]{4}$",
        "TR": r"^[0-9]{5}$",
        "TT": r"^[0-9]{6}$",
        "TW": r"^([0-9]{3}|[0-9]{5})$",
        "UA": r"^[0-9]{5}$",
        "US": r"^[0-9]{5}(-[0-9]{4}|-[0-9]{6})?$",
        "UY": r"^[0-9]{5}$",
        "UZ": r"^[0-9]{6}$",
        "VA": r"^00120$",
        "VC": r"^VC[0-9]{4}",
        "VE": r"^[0-9]{4}[A-Z]?$",
        "VG": r"^VG[0-9]{4}$",
        "VI": r"^[0-9]{5}$",
        "VN": r"^[0-9]{6}$",
        "WF": r"^[0-9]{5}$",
        "XK": r"^[0-9]{5}$",
        "YT": r"^[0-9]{5}$",
        "ZA": r"^[0-9]{4}$",
        "ZM": r"^[0-9]{5}$",
    }

    primary = models.BooleanField(default=False)
    address_type = models.CharField(
        max_length=255,
        choices=ADDRESS_TYPES,
        default=BILLING,
        verbose_name=_("type"),
        help_text=_("E.g. Shipping or billing"),
    )
    title = models.CharField(
        _("Title"),
        max_length=64,
        choices=TITLE_CHOICES,
        blank=True,
        help_text=_("Treatment Pronouns for the customer"),
    )
    name = models.CharField(
        _("name"),
        max_length=255,
        help_text="If blank, contact name will be used.",
    )

    line_1 = models.CharField(
        null=True,
        blank=False,
        max_length=255,
        verbose_name=_("line 1"),
    )
    line_2 = NullCharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_("line 2"),
    )
    line_3 = NullCharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_("line 3"),
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
    postcode = UppercaseCharField(
        _("Post/Zip-code"),
        max_length=64,
        blank=True,
    )
    country = models.ForeignKey(
        "simpel_contacts.Country",
        on_delete=models.CASCADE,
        verbose_name=_("Country"),
    )

    class Meta:
        abstract = True

    @cached_property
    def address(self):
        return " ".join([self.line_1, self.line_2, self.line_3])

    def __str__(self):
        return "(%s) %s" % (self.address_type.title(), self.name)

    def text_line_1(self):
        address = [self.address, self.city]
        return ", ".join([str(a) for a in address])

    def text_line_2(self):
        address = [self.province, self.country, self.postcode]
        return ", ".join([str(a) for a in address])

    def to_dict(self):
        return {
            "primary": self.primary,
            "address_type": self.address_type,
            "name": self.name,
            "address": str(self.address).strip(),
            "city": self.city,
            "province": self.province,
            "country": self.country,
            "postcode": self.postcode,
        }


class AbstractCountry(models.Model):
    """
    `ISO 3166 Country Codes <https://www.iso.org/iso-3166-country-codes.html>`_

    The field names are a bit awkward, but kept for backwards compatibility.
    pycountry's syntax of alpha2, alpha3, name and official_name seems sane.
    """

    iso_3166_1_a2 = models.CharField(_("ISO 3166-1 alpha-2"), max_length=2, primary_key=True)
    iso_3166_1_a3 = models.CharField(_("ISO 3166-1 alpha-3"), max_length=3, blank=True)
    iso_3166_1_numeric = models.CharField(_("ISO 3166-1 numeric"), blank=True, max_length=3)

    #: The commonly used name; e.g. 'United Kingdom'
    printable_name = models.CharField(_("Country name"), max_length=128, db_index=True)
    #: The full official name of a country
    #: e.g. 'United Kingdom of Great Britain and Northern Ireland'
    name = models.CharField(_("Official name"), max_length=128)

    display_order = models.PositiveSmallIntegerField(
        _("Display order"), default=0, db_index=True, help_text=_("Higher the number, higher the country in the list.")
    )

    is_shipping_country = models.BooleanField(_("Is shipping country"), default=False, db_index=True)

    class Meta:
        abstract = True
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = (
            "-display_order",
            "printable_name",
        )

    def __str__(self):
        return self.printable_name or self.name

    @property
    def code(self):
        """
        Shorthand for the ISO 3166 Alpha-2 code
        """
        return self.iso_3166_1_a2

    @property
    def numeric_code(self):
        """
        Shorthand for the ISO 3166 numeric code.

        :py:attr:`.iso_3166_1_numeric` used to wrongly be a integer field, but has to
        be padded with leading zeroes. It's since been converted to a char
        field, but the database might still contain non-padded strings. That's
        why the padding is kept.
        """
        return "%.03d" % int(self.iso_3166_1_numeric)
