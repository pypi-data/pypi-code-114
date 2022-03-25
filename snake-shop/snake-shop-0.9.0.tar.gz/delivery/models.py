from time import mktime
from datetime import date
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.timezone import now, datetime, timedelta, make_aware
from django.contrib.sites.models import Site
from custom.site_manager import SiteMixin


__all__ = ['Weekday', 'Delivery', 'TourBlocklist', 'GlobalBlocklist',
           'Postcode', 'Tour', 'DeliveryTime']


class ModelMixin(models.Model):
    created = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated at'), auto_now=True)

    class Meta:
        abstract = True


class Weekday(models.IntegerChoices):
    """  """
    MONDAY = (1, _('Monday'))
    TUESDAY = (2, _('Tuesday'))
    WEDNESDAY = (3, _('Wednesday'))
    THURSDAY = (4, _('Thursday'))
    FRIDAY = (5, _('Friday'))
    SATURDAY = (6, _('Saturday'))
    SUNDAY = (7, _('Sunday'))

    def __str__(self):
        return str(self.label)


class Delivery(SiteMixin, models.Model):
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    time = models.ForeignKey(
        'DeliveryTime',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    target_time = models.TimeField(null=True, blank=True)
    date = models.DateField(_('Date'))

    @property
    def is_selectable(self):
        if self.date and self.time and not self.target_time:
            # TODO: Dirty fixed now() is utc
            delta = timedelta(2 if now().hour >= (14 - 1) else 1)
            earliest_delivery_date = (now() + delta).date()
            result = self.date >= earliest_delivery_date

        elif self.date and self.target_time and not self.time:
            combined_datetime = make_aware(
                datetime.combine(self.date, self.target_time)
            )
            result = combined_datetime >= now()

        elif self.date and not self.time and not self.target_time:
            result = self.date >= now().date()

        else:
            result = None
        return result

    def to_id(self):
        serialized_date = mktime(self.date.timetuple())
        if not self.time_id:
            return f'_{serialized_date}'
        return f'{self.time.pk}_{serialized_date}'

    @classmethod
    def from_id(cls, id_string, site):
        time_pk, date_timestamp = id_string.split('_')
        time = DeliveryTime.objects.get(pk=time_pk) if time_pk else None
        date_obj = date.fromtimestamp(float(date_timestamp))
        return cls.objects.get_or_create(site=site, time=time, date=date_obj)[0]

    @property
    def weekday(self):
        return Weekday(self.date.isoweekday())

    def get_time_str(self):
        time_str = ''
        if self.time:
            time_str = self.time.time()
        elif self.target_time:
            time_str = str(self.target_time.strftime('%H:%M'))
        return time_str

    def __str__(self):
        result = '{}, {}'.format(
            self.weekday.label,
            self.date.strftime('%d.%m.%Y')
        )
        if self.time_id and self.time.start and self.time.end:
            result += ' ({} - {})'.format(
                self.time.start.strftime('%H:%M'),
                self.time.end.strftime('%H:%M'),
            )
        elif self.target_time:
            result += ' ({})'.format(
                self.target_time.strftime('%H:%M'),
            )
        return result

    class Meta:
        ordering = ['date', 'time']
        unique_together = ('site', 'time', 'date')
        verbose_name = _('Delivery')
        verbose_name_plural = _('Deliveries')


class AbstractBlocklist(SiteMixin, ModelMixin, models.Model):
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    date = models.DateField(_('Date'))
    name = models.CharField(_('Name'), max_length=50, null=True, blank=True)
    enabled = models.BooleanField(_('Enabled'), default=True)

    @classmethod
    def get_dates(cls):
        return {obj.date for obj in cls.get_all()}

    @classmethod
    def get_all(cls):
        return cls.objects.filter(enabled=True)

    @classmethod
    def date_is_blocked(cls, date):
        return date in (date.date for date in cls.objects.all())

    def __str__(self):
        return '{} {} {}'.format(
            self.date,
            self.name if self.name else '',
            _('is blocked') if self.enabled else _('is not blocked'),
        )

    class Meta:
        abstract = True


class TourBlocklist(AbstractBlocklist):
    tour = models.ForeignKey('tour', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Tour Offday')
        verbose_name_plural = _('Tour Offdays')
        unique_together = ('site', 'date')


class GlobalBlocklist(AbstractBlocklist):
    """ Contains all unpossible days """

    class Meta:
        verbose_name = _('Global Offday')
        verbose_name_plural = _('Global Offdays')
        unique_together = ('site', 'date')


class Postcode(models.Model):
    postcode = models.PositiveIntegerField(_("Postcode"), unique=True)
    city = models.CharField(_('City'), max_length=50)

    def __str__(self):
        return '{} - {}'.format(self.postcode, self.city)

    @property
    def shipping_allowed(self):
        return self.postcode in Postcode.get_all_postcodes()

    def get_next_deliveries(self):
        tour = self.tour_set.first()
        if tour:
            return tour.next_deliveries()

    @classmethod
    def get_all_postcodes(cls):
        return (x.postcode for x in cls.objects.all())

    class Meta:
        ordering = ['postcode']
        verbose_name = _('Postcode')
        verbose_name_plural = _('Postcodes')


class Tour(SiteMixin, ModelMixin, models.Model):
    """ Planned Tour
    Tour times comes from DeliveryTime
    Tour Days comse from DeliveryDays
    """
    site = models.ForeignKey(
        Site, verbose_name=_("Site"),
        on_delete=models.CASCADE,
    )
    postcodes = models.ManyToManyField('postcode')

    @classmethod
    def get_cached(cls, name=None):
        return list(cls.objects.all())

    def get_cities(self):
        return {x.city for x in self.postcodes.all()}

    def get_postcodes(self):
        return {x.postcode for x in self.postcodes.all()}

    #===========================================================================
    # @classmethod
    # def by_postcode(cls, postcode):
    #     return cls.objects.filter(postcode=postcode)
    #===========================================================================

    def get_delivery_times(self):
        return self.deliverytime_set.all()

    def get_weekdays(self):
        return {Weekday(dt.weekday) for dt in self.deliverytime_set.all()}

    def next_deliveries(self, num=10):
        weekdays = self.get_weekdays()
        if not weekdays:
            return
        blocked = list(GlobalBlocklist.get_dates()) + list(TourBlocklist.get_dates())
        date_offset = 1 if datetime.now().hour < 14 else 2
        deliveries = []
        while len(deliveries) < num-1:
            date = datetime.now() + timedelta(days=date_offset)
            date = date.date()
            if date not in blocked and Weekday(date.isoweekday()) in weekdays:
                deliverytimes = self.get_delivery_times().filter(weekday=date.isoweekday())
                for deliverytime in deliverytimes:
                    delivery_kwargs = {'time': deliverytime, 'date': date}
                    try:
                        delivery = Delivery.objects.get(**delivery_kwargs)
                    except Delivery.DoesNotExist:
                        delivery = Delivery(**delivery_kwargs)

                    deliveries.append(delivery)
            date_offset += 1
        return deliveries

    def __str__(self):
        return '{} [{}]'.format(
                ', '.join(self.get_cities()),
                ', '.join((str(x.postcode) for x in self.postcodes.all())),
            )

    class Meta:
        verbose_name = _('Tour')
        verbose_name_plural = _('Tours')


class DeliveryTime(ModelMixin, models.Model):
    tour = models.ForeignKey('tour', on_delete=models.CASCADE)
    weekday = models.PositiveSmallIntegerField(_('Weekday'), choices=Weekday.choices)
    start = models.TimeField(_('Start'), null=True, blank=True)
    end = models.TimeField(_('End'), null=True, blank=True)

    def time(self):
        """ used in machine email template """
        return '{}-{}'.format(
            str(self.start).rsplit(':', 1)[0],
            str(self.end).rsplit(':', 1)[0]
        )

    def weekday_str(self):
        return Weekday(self.weekday).label

    def __str__(self):
        return '{}<{} - {}>'.format(
                self.weekday_str(),
                self.start,
                self.end,
            )

    class Meta:
        ordering = ['start', 'end']
        verbose_name = _('Delivery Time')
        verbose_name_plural = _('Delivery Times')
