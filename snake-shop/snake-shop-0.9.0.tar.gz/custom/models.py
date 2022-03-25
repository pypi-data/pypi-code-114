"""
This ist the central Configuration of the Shop to manage settings from admin.
"""
from django.db import models
from django.db.models import Q
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site
from django.core.mail import get_connection
from filer.fields.image import FilerImageField
from apps.partner.models import Partner


SOCIAL_DEFAULT_HTML = {
    1: '''<i class="fab fa-facebook-f mx-auto mt-auto" style="font-size: 22px;
        color: #757575;"></i>''',
    2: '''<i class="fab fa-instagram m-auto" style="font-size: 17px; color:
        #757575;"></i>''',
}


class TagValue(models.Model):
    tag = models.ForeignKey(
        'Tag',
        on_delete=models.CASCADE,
        related_name='values',
    )
    value = models.TextField(
        default=None,
        blank=True, null=True,
    )
    modified = models.DateTimeField(
        auto_now=True
    )

    product = models.ForeignKey(
        'catalogue.Product',
        on_delete=models.CASCADE,
        related_name='tag_values',
        blank=True, null=True,
    )
    user_address = models.ForeignKey(
        'address.UserAddress',
        on_delete=models.CASCADE,
        related_name='tag_values',
        blank=True, null=True,
    )
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
        related_name='tag_values',
        blank=True, null=True,
    )
    wishlist = models.ForeignKey(
        'wishlists.Wishlist',
        on_delete=models.CASCADE,
        related_name='tag_values',
        blank=True, null=True,
    )
    wishlist_line = models.ForeignKey(
        'wishlists.Line',
        on_delete=models.CASCADE,
        related_name='tag_values',
        blank=True, null=True,
    )

    def get_object(self):
        return self.product \
            or self.user_address\
            or self.user \
            or self.wishlist \
            or self.wishlist_line

    def __str__(self):
        return f'{self.tag} {self.get_object()}'


class Tag(models.Model):
    """
    Tag for identifying objects.
    Use this when tagging imports.

    Add a Value from related object like this:
    user_address.tags.add(tag, through_defaults={'value': 'fasdf'})

    Never use this for productive logic!!!
    """
    name = models.CharField(max_length=150)
    description = models.TextField(
        default=None,
        blank=True, null=True,
    )
    created = models.DateTimeField(auto_now_add=True)

    products = models.ManyToManyField(
        'catalogue.Product',
        related_name='tags',
        through=TagValue,
    )
    addresses = models.ManyToManyField(
        'address.Useraddress',
        related_name='tags',
        through=TagValue,
    )
    users = models.ManyToManyField(
        'user.User',
        related_name='tags',
        through=TagValue,
    )
    wishlists = models.ManyToManyField(
        'wishlists.Wishlist',
        related_name='tags',
        through=TagValue,
    )
    wishlist_lines = models.ManyToManyField(
        'wishlists.Line',
        related_name='tags',
        through=TagValue,
    )

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    class CodeChoices(models.IntegerChoices):
        FACEBOOK = 1, 'Facebook'
        INSTAGRAM = 2, 'Instagram'
        CUSTOM = 100, 'Custom'

    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    configuration = models.ForeignKey(
        'Configuration',
        on_delete=models.CASCADE,
        related_name='sociallinks',
    )
    code = models.PositiveSmallIntegerField('Code', choices=CodeChoices.choices)
    url = models.URLField()
    html = models.TextField(blank=True, null=True,)

    def get_default_html(self):
        return SOCIAL_DEFAULT_HTML.get(self.code)

    def get_html(self):
        return self.html or self.get_default_html()

    def __str__(self):
        return self.CodeChoices(self.code).label

    class Meta:
        ordering = ('code',)
        unique_together = ('site', 'code')


class CompanyMixin(models.Model):
    company_name = models.CharField(
        _('Full company name'), max_length=150,
        help_text=_('This is the full company name (eg. Company GmbH&Co KG)'),
    )
    company_short_name = models.CharField(
        _('Short company name'), max_length=150,
        help_text=_('This is the short company name (eg. Company)'),
    )
    company_street = models.CharField(
        _("First line of address"),
        max_length=255,
    )
    company_postcode = models.CharField(
        _("Post/Zip-code"),
        max_length=64,
    )
    company_city = models.CharField(
        _("City"),
        max_length=255,
    )
    company_contact = models.TextField(
        _('Company contact information'),
        help_text=_(
            'The full contact information of the customers shop manager.'
        ),
    )
    company_support_email = models.EmailField(
        _('Company support email'),
        help_text=_(
            'The email of the support for the shop customers'
        ),
    )
    company_support_phone = models.CharField(
        _('Company support phone'),
        max_length=255,
        help_text=_(
            'The number of the support for the shop customers'
        ),
    )

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    logo = FilerImageField(
        verbose_name=_('Logo'),
        on_delete=models.SET_NULL, related_name='logo_image',
        blank=True, null=True,
    )
    logo_square = FilerImageField(
        verbose_name=_('Logo square'),
        on_delete=models.SET_NULL, related_name='logo_image_square',
        blank=True, null=True,
    )
    no_image = FilerImageField(
        verbose_name=_('No image'),
        on_delete=models.SET_NULL, related_name='no_image',
        blank=True, null=True,
    )
    offer_image = FilerImageField(
        verbose_name=_('Offer image'),
        on_delete=models.SET_NULL, related_name='offer_image',
        blank=True, null=True,
    )
    header_hints_top_1 = FilerImageField(
        verbose_name=_('Header hints block top image'),
        on_delete=models.SET_NULL, related_name='header_hints_top_1',
        blank=True, null=True,
    )
    header_hints_top_1_responsive = FilerImageField(
        verbose_name=_('Header hints block top image responsive'),
        on_delete=models.SET_NULL, related_name='header_hints_top_1_responsive',
        blank=True, null=True,
    )
    header_hints_top_1_url = models.URLField(
        _('Header hints block top url'),
        blank=True, null=True,
    )
    header_hints_bottom_1 = FilerImageField(
        verbose_name=_('Header hints block bottom left image'),
        on_delete=models.SET_NULL, related_name='header_hints_bottom_1',
        blank=True, null=True,
    )
    header_hints_bottom_1_url = models.URLField(
        _('Header hints block bottom left url'),
        blank=True, null=True,
    )
    header_hints_bottom_2 = FilerImageField(
        verbose_name=_('Header hints block bottom right image'),
        on_delete=models.SET_NULL, related_name='header_hints_bottom_2',
        blank=True, null=True,
    )
    header_hints_bottom_2_url = models.URLField(
        _('Header hints block bottom right url'),
        blank=True, null=True,
    )
    slider_intro = FilerImageField(
        verbose_name=_('Slider intro image'),
        on_delete=models.SET_NULL, related_name='slider_intro',
        blank=True, null=True,
    )
    slider_intro_responsive = FilerImageField(
        verbose_name=_('Slider intro image responsive'),
        on_delete=models.SET_NULL, related_name='slider_intro_responsive',
        blank=True, null=True,
    )
    first_slider_element = FilerImageField(
        verbose_name=_('First slider element'),
        on_delete=models.SET_NULL, related_name='first_slider_element',
        blank=True, null=True,
    )
    class Meta:
        abstract = True


class ColorMixin(models.Model):
    color_1 = models.CharField(
        _('Main accent color'), max_length=50,
        help_text=_('CSS main color of the brand.'),
    )
    color_2 = models.CharField(
        _('Second accent color'), max_length=50,
        help_text=_('CSS second color of the brand.'),
    )
    color_background = models.CharField(
        _('Background color'), max_length=50,
        help_text=_('CSS background color of the page.'),
        default='white',
    )
    class Meta:
        abstract = True

class EmailConfigMixin(models.Model):
    email_host = models.CharField(
        _('Email Hostname'),
        help_text=_('Für den Login beim Email Provider'),
        max_length=100,
    )
    email_port = models.PositiveSmallIntegerField(
        _('Email Port'),
        help_text=_('Für den Login beim Email Provider'),
        default=587,
    )
    email_user = models.CharField(
        _('Email Benutzername'),
        help_text=_('Für den Login beim Email Provider'),
        max_length=100,
    )
    email_password = models.CharField(
        _('Email Password'),
        help_text=_('Für den Login beim Email Provider'),
        max_length=100,
    )
    email_use_tls = models.BooleanField(
        _('TLS verwenden'),
        help_text=_('Für den Login beim Email Provider'),
        default=True,
    )
    email_name = models.CharField(
        _('Email Absender Name'),
        help_text=_('z.B. Company.de wird zu "Company.de <info@company.de>"'),
        max_length=100,
    )
    email_sender = models.EmailField(
        _('Email Absender Adresse'),
        help_text=_('z.B. info@company.de wird zu "Company.de <info@company.de>"'),
        default=email_user,
    )
    email_reply_to = models.EmailField(
        _('Email Antwort Adresse'),
        help_text=_('Wird in der Email als Antwortadresse angegeben'),
        blank=True, null=True
    )

    def get_email_sender(self):
        return f'{self.email_name} <{self.email_sender}>'

    def get_mail_connection(self):
        backend_kwargs = {
            'host': self.site.configuration.email_host,
            'port': self.site.configuration.email_port,
            'username': self.site.configuration.email_user,
            'password': self.site.configuration.email_password,
            'use_tls': self.site.configuration.email_use_tls,
            'use_ssl': not self.site.configuration.email_use_tls,
            'fail_silently': not settings.DEBUG,
        }
        return get_connection(**backend_kwargs)

    class Meta:
        abstract = True


class Configuration(CompanyMixin, ColorMixin, ImageMixin, EmailConfigMixin,
                    models.Model):

    site = models.OneToOneField(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    show_all_products = models.BooleanField(
        _('Alle Produkte'),
        help_text=_('Wenn aktiviert, werden alle Produkte angezeigt statt der '
                    'abonnierten'),
        default=False,
    )
    home_bottom_text = models.TextField(
        _('content'),
        help_text=_('Text on the bottom of the start page, sometimes used for seo'),
        blank=True, null=True,
    )
    google_site_id = models.CharField(
        max_length=100,
        null=True, blank=True
    )
    basket_sumup_with_deposit = models.BooleanField(
        _('Warenkorb Summe mit Pfand'),
        default=True,
        help_text=_('In Warenkorb und Checkout wird der Preis nicht summiert angezeigt.'),
    )

    @property
    def settings(self):
        """
        :returns: Django Settings
        """
        return settings

    def get_color1(self):
        return self.color_1

    def get_color2(self):
        return self.color_2 or self.get_color1()

    def __str__(self):
        return 'Site Configuration ' + str(self.site)

    def save(self, **kwargs):
        Partner.objects.get_or_create(
            site=self.site,
            code=Partner.default_code,
            defaults={
                'name': Partner.default_name,
            }
        )
        return super().save(**kwargs)
