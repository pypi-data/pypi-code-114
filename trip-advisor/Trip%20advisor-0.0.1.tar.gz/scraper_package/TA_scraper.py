from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import pandas as pd
import time

class Scraper:
    '''
    This class is a scaper that can be used for scrapping hotel information from trip advisor

    Parameters:
    url: str 
        Default url is is trip advisor homepage

    Attribute
    ----------
    driver:
        This is the webdriver object
    Hotel-dict:
        Dictionary stores all the hotel information

    '''

    def __init__(self, url: str = 'https://www.tripadvisor.co.uk/'):
        # let chromedriver install the correct version and open the we
        self.driver = Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        self.Hotel_dict = {
            'Name': [],
            'Href': [],
            'Price': [],
            'Review': [],
            'Bubbles': []
        }

    def accept_cookies(self, xpath: str = '//*[@id="onetrust-accept-btn-handler"]') -> None:
        '''
        This method looks for and clicks the accept cookies button 

        Parameters 
        -----------
        xpath : str
            The xpath for the accept button

        '''
        try:
            # wait for max of 10s
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
            self.driver.find_element(By.XPATH, xpath).click()

        except TimeoutError:
            print('no cookies button')

        return True

    def search_bar(self, text: str, xpath: str = "/html/body/div[1]/main/div[3]/div/div/div[2]/form/input[1]") -> None:
        '''
        Method looks for the search bar through the xpath and sends keys to the searchbar 

        Parameters 
        ------------
        xpath: str 
            The xpath for the serach bar 
        text: str 
            Name of the city/country
        '''

        try:
            button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
            button.send_keys(text)
            button.send_keys(Keys.ENTER)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, '//*[@class="ui_column is-12 card-wrap"]'))).click()
        except TimeoutException:
            print('No search bar found')

        return text
    
    def _find_hotel_container(self):
        '''
        This method looks clicks on the hotel option on the tripadvsor and switches tab to the window with hotel information
        '''
        
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//*[text()='Hotels']//ancestor::a").click()
        
        return True

    def _Hotels_Href(self, xpath: str = "//div[@class='meta_listing ui_columns large_thumbnail_mobile ']"):
        '''
        Method: Looks for the container with the list of all the hotel href on that page and appends all thr href to a list 

        Parameters
        ----------
        xpath: str
            The path to the Hotel list container 
        '''

        Container = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        self.driver.implicitly_wait(5)
        Href_Container = Container.find_elements_by_xpath(
            "//a[@class='property_title prominent ']")

        for hotel in Href_Container:
            try:
                self.Hotel_dict['Href'].append(hotel.get_attribute('href'))
            except NoSuchElementException:
                self.Hotel_dict['Href'].append('N/A')
        return(len(self.Hotel_dict['Href']))

    def _iterate_all_pages(self, xpath: str = "//div[@class='unified ui_pagination standard_pagination ui_section listFooter']") -> None:
        '''
        Method: Finds the number of pages for the search and iterates through all the pages to get Href of all the hotels

        Parameters 
        -----------
        xpath: str 
            Path to fnd the number of pages
        '''

        number_pages = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))).get_attribute('data-numpages')
        list_page_numbers = [i for i in range(2, int(number_pages))]

        first = list_page_numbers[1:2]

        for x in first:
            try:
                self.driver.implicitly_wait(5)
                self.Hotels_Href()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@class="nav next ui_button primary"]'))).click()

            except StaleElementReferenceException:
                continue
        return('There are {} pages'.format(list_page_numbers))

    def _all_info(self) -> None:
        '''
        Methods; Gets name, price, number of reviews, rating of all the hotel from the Href list

        Parameters
        ---------
        Takes the list of Href from the previous method
        '''

        for i in self.Hotel_dict['Href']:
            self.driver.get(i)

            try:
                Name_container = self.driver.find_element_by_xpath(
                    "//h1[@class='fkWsC b d Pn']")
                self.Hotel_dict['Name'].append(Name_container.text)
            except StaleElementReferenceException:
                self.Hotel_dict['Name'].append('N/A')
            except NoSuchElementException:
                self.Hotel_dict['Name'].append('N/A')

            try:
                Price_container = self.driver.find_element_by_xpath(
                    "//div[@class='fzleB b']")
                self.Hotel_dict['Price'].append(Price_container.text)
            except StaleElementReferenceException:
                self.Hotel_dict['Price'].append('N/A')
            except NoSuchElementException:
                self.Hotel_dict['Price'].append('N/A')

            try:
                Bubble_container = self.driver.find_element_by_xpath(
                    "//span[@class='bvcwU P']")
                self.Hotel_dict['Bubbles'].append(Bubble_container.text)
            except StaleElementReferenceException:
                self.Hotel_dict['Bubbles'].append('N/A')
            except NoSuchElementException:
                self.Hotel_dict['Bubbles'].append('N/A')

            try:
                Review_container = self.driver.find_element_by_xpath(
                    "//span[@class='btQSs q Wi z Wc']")
                self.Hotel_dict['Review'].append(Review_container.text)
            except StaleElementReferenceException:
                self.Hotel_dict['Review'].append('N/A')
            except NoSuchElementException:
                self.Hotel_dict['Review'].append('N/A')

        return len(self.Hotel_dict)

    def _create_df(self) -> None:
        '''
        Method creates a dataframe from the dictionary of hotel information
        '''

        Hotels = pd.DataFrame(self.Hotel_dict)
        Hotels.to_csv('Hotels.csv')


if __name__ == "__main__":
    bot = Scraper()
    bot.accept_cookies()
    bot.search_bar('London')
    bot.find_hotel_container()
    bot.Hotels_Href()
    bot.iterate_all_pages()
    bot.all_info()
    bot.create_df()
