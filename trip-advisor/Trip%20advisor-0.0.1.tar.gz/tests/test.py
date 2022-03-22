import unittest
import sys
import os 
sys.path.append('/home/misha/Documents/AiCore/Trip_advisor/Scraper')
#sys.path.append(os.path.join(sys.path[0],'Scraper'))
print(sys.path)
from TA_scraper import Scraper


class TestScraper(unittest.TestCase):
    def setUp(self):
        self.bot = Scraper()

    def test_accept_cookies(self):
        test_accept = self.bot.accept_cookies()
        self.assertTrue(test_accept)

    def test_search_bar(self):
        Bar = self.bot.search_bar('London')
        self.assertIsInstance(Bar,str)

    def test_find_hotel_container(self):
        hotel_container = self.bot.find_hotel_container()
        self.assertTrue(hotel_container)

    #def test_Hotels_Href(self):
    #    Href = self.bot.Hotels_Href()
    #    self.assertIsInstance(Href)

    #def test_iterate_all_pages(self):
    #    iterate = self.bot.iterate_all_pages()
    #    self.assertIsInstance(iterate)

    #def test_all_info(self):
     #   info = self.bot.all_info()
      #  self.assertIsInstance(info)

    #def test_create_df(self):
     #   df = self.bot.create_df()
      #  self.assertIsInstance(df)

    def tearDown(self):
        self.bot.driver.quit()

if __name__ == '__main__':
    unittest.main(argv=[''],verbosity=2,exit=False)

