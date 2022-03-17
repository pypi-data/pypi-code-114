from unittest import TestCase

from property_price_register.models.sale import Sales, Sale


class SalesTest(TestCase):

    def test_sales_load(self):
        sales = Sales.load()
        self.assertGreater(len(sales), 450_000)

    def test_sales_average_price(self):
        sales = Sales.load()
        self.assertGreater(sales.average_price, 0)
        self.assertLess(sales.average_price, 1_000_000)


class SaleTest(TestCase):

    def test_serialize_clean(self):
        obj = Sale(
            date='01/01/2022',
            address='123 Something Lane',
            postal_code='',
            county='Dublin',
            price=123123.12,
            not_full_market_price='No',
            vat_exclusive='No',
            description_of_property='Second-Hand Dwelling house /Apartment',
            description_of_property_size='greater than or equal to 38 sq metres and less than 125 sq metres',
            lat=0.0,
            lon=0.0,
            full_address='123 Something Lane',
            match_score=1,
            eircode_display_name='123 Something Lane',
            eircode_unique_id='AAAA',
            eircode_routing_key='D11',
            eircode_address_source='ppr',
        )
        self.assertEqual(
            obj.serialize(),
            {
                'address': '123 Something Lane',
                'county': 'Dublin',
                'date': '01/01/2022',
                'description_of_property': 'Second-Hand Dwelling house /Apartment',
                'description_of_property_size': 'greater than or equal to 38 sq metres and less than 125 sq metres',
                'eircode_display_name': '123 Something Lane',
                'eircode_routing_key': 'D11',
                'eircode_unique_id': 'AAAA',
                'eircode_address_source': 'ppr',
                'full_address': '123 Something Lane',
                'lat': 0.0,
                'lon': 0.0,
                'match_score': 1,
                'not_full_market_price': 'No',
                'postal_code': '',
                'price': 123123.12,
                'vat_exclusive': 'No'
            }
        )

    def test_serialize_dirty(self):
        '''
        This is as we get the data from the property price register. Dirty headers in the csv
        '''
        data = {
            'Date of Sale (dd/mm/yyyy)': '01/01/2022',
            'Address': '123 Something Lane',
            'Postal Code': '',
            'County': 'Dublin',
            'Price (\x80)': '123123.12',
            'Not Full Market Price': 'No',
            'VAT Exclusive': 'No',
            'Description of Property': 'Second-Hand Dwelling house /Apartment',
            'Property Size Description': 'greater than or equal to 38 sq metres and less than 125 sq metres'
        }
        self.assertEqual(
            Sale(
                **data
            ).serialize(),
            {
                'address': '123 Something Lane',
                'county': 'Dublin',
                'date': '01/01/2022',
                'description_of_property': 'Second-Hand Dwelling house /Apartment',
                'description_of_property_size': 'greater than or equal to 38 sq metres and less than 125 sq metres',
                'eircode_display_name': None,
                'eircode_routing_key': None,
                'eircode_unique_id': None,
                'eircode_address_source': None,
                'full_address': None,
                'lat': None,
                'lon': None,
                'match_score': None,
                'not_full_market_price': 'No',
                'postal_code': '',
                'price': 123123.12,
                'vat_exclusive': 'No'
            }
        )

    def test_content_hash(self):
        first_data = {
            'Date of Sale (dd/mm/yyyy)': '01/01/2022',
            'Address': '123 Something Lane',
            'Postal Code': '',
            'County': 'Dublin',
            'Price (\x80)': '123123.12',
            'Not Full Market Price': 'No',
            'VAT Exclusive': 'No',
            'Description of Property': 'Second-Hand Dwelling house /Apartment',
            'Property Size Description': 'greater than or equal to 38 sq metres and less than 125 sq metres'
        }
        first_sale_one = Sale(
            **first_data
        )

        first_sale_two = Sale(
            **first_data
        )

        second_data = {
            'Date of Sale (dd/mm/yyyy)': '01/01/2021',
            'Address': '123 Something Lane',
            'Postal Code': '',
            'County': 'Dublin',
            'Price (\x80)': '123123.12',
            'Not Full Market Price': 'No',
            'VAT Exclusive': 'No',
            'Description of Property': 'Second-Hand Dwelling house /Apartment',
            'Property Size Description': 'greater than or equal to 38 sq metres and less than 125 sq metres'
        }
        second_sale = Sale(
            **second_data
        )

        self.assertEqual(
            first_sale_one.content_hash,
            first_sale_two.content_hash
        )

        self.assertNotEqual(
            first_sale_one.content_hash,
            second_sale.content_hash
        )

    def test_is_good_numbers(self):
        obj = Sale(
            date='01/01/2022',
            address='123 Something Lane',
            postal_code='',
            county='Dublin',
            price=123123.12,
            not_full_market_price='No',
            vat_exclusive='No',
            description_of_property='Second-Hand Dwelling house /Apartment',
            description_of_property_size='greater than or equal to 38 sq metres and less than 125 sq metres',
            lat=0.0,
            lon=0.0,
            full_address='123 Something Lane, Co. Dublin',
            match_score=1,
            eircode_display_name='123 Something Lane',
            eircode_unique_id='AAAA',
            eircode_routing_key='D11'
        )
        self.assertTrue(obj.is_good_mapbox_address)

    def test_is_good_county(self):
        obj = Sale(
            date='01/01/2022',
            address='123 Something Lane',
            postal_code='',
            county='Dublin',
            price=123123.12,
            not_full_market_price='No',
            vat_exclusive='No',
            description_of_property='Second-Hand Dwelling house /Apartment',
            description_of_property_size='greater than or equal to 38 sq metres and less than 125 sq metres',
            lat=0.0,
            lon=0.0,
            full_address='123 Something Lane, Co. Dublin',
            match_score=1,
            eircode_display_name='123 Something Lane',
            eircode_unique_id='AAAA',
            eircode_routing_key='D11'
        )
        self.assertTrue(obj.is_good_mapbox_address)

        obj = Sale(
            date='01/01/2022',
            address='123 Something Lane',
            postal_code='',
            county='Dublin',
            price=123123.12,
            not_full_market_price='No',
            vat_exclusive='No',
            description_of_property='Second-Hand Dwelling house /Apartment',
            description_of_property_size='greater than or equal to 38 sq metres and less than 125 sq metres',
            lat=0.0,
            lon=0.0,
            full_address='123 Something Lane, Co. Cork',
            match_score=1,
            eircode_display_name='123 Something Lane',
            eircode_unique_id='AAAA',
            eircode_routing_key='D11'
        )
        self.assertFalse(obj.is_good_mapbox_address)
