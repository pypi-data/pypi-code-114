from config.test_base import BaseTestCase
from .models import *


class DeliveryTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.postcodes = self.setup_postcodes()
        self.tours = self.setup_tours()
        self.delivery_times = self.setup_delivery_times()
        self.deliveries = self.setup_deliveries()
        self.global_blocklist = self.setup_global_blocklist()
        self.local_blocklist = self.setup_local_blocklist()

    def setup_postcodes(self):
        """ postcode, city """
        return [
            Postcode.objects.create(postcode=11111, city='Testcity1+2'),
            Postcode.objects.create(postcode=22222, city='Testcity1+2'),
            Postcode.objects.create(postcode=33333, city='Testcity3'),
            Postcode.objects.create(postcode=44444),
        ]

    def setup_tours(self):
        """ postcodes """
        tours = 4 * [Tour.objects.create()]
        tours[1].postcodes.set([self.postcodes[0]])
        tours[2].postcodes.set(self.postcodes)
        tours[3].postcodes.set(self.postcodes[3:4])
        return tours

    def setup_delivery_times(self):
        """ tour, weekday, start, end """
        return [
            DeliveryTime.objects.create(
                tour=self.tours[0], weekday=1, start='8:00', end='12:00'
            ),
            DeliveryTime.objects.create(
                tour=self.tours[0], weekday=1, start='12:00', end='18:00'
            ),
            DeliveryTime.objects.create(
                tour=self.tours[0], weekday=2, start='8:00', end='12:00'
            ),
            DeliveryTime.objects.create(
                tour=self.tours[0], weekday=3, start='8:00', end='12:00'
            ),
            DeliveryTime.objects.create(
                tour=self.tours[0], weekday=4, start='8:00', end='12:00'
            ),
            DeliveryTime.objects.create(
                tour=self.tours[0], weekday=5, start='8:00', end='12:00'
            ),
            DeliveryTime.objects.create(
                tour=self.tours[0], weekday=6, start='8:00', end='12:00'
            ),
            DeliveryTime.objects.create(
                tour=self.tours[0], weekday=7, start='8:00', end='12:00'
            ),
        ]

    def setup_deliveries(self):
        """ time (DateTime), date """
        return self.tours[0].next_deliveries()

    def setup_global_blocklist(self):
        return

    def setup_local_blocklist(self):
        return

    def test_weekday(self):
        pass

    def test_delivery(self):
        """ Test when the deliveryobject is saved """
        for delivery in self.tours[0].next_deliveries():
            self.assertIsNone(delivery.pk)

    def test_tour_blocklist(self):
        """ tour, date, name, enabled """
        pass

    def test_global_blocklist(self):
        """ date, name, enabled """
        pass

    def test_postcode(self):
        pass

    def test_tour(self):
        pass

    def test_delivery_time(self):
        pass
