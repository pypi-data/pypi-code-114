import os

import click
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
WEBDRIVER_PATH=os.getenv('WEBDRIVER_PATH')

class Band:
  def __init__(self, band, tour_page_url, selenium_driver):
    self.band = band
    self.tour_page_url = tour_page_url
    self.concerts = []

    self._load_concerts(selenium_driver)

  def __str__(self):
    return str(f"Band: {self.band}\n\n") + "\n".join([str(c) for c in self.concerts])

  def _load_concerts(self, selenium_driver):
    selenium_driver.get(self.tour_page_url)
    dates = selenium_driver.find_elements(by=By.CSS_SELECTOR, value=".bit-event .bit-date")
    locations = selenium_driver.find_elements(by=By.CSS_SELECTOR, value=".bit-event .bit-location")

    locations = [location.text for location in locations if location and location.text]
    dates = [date.text for date in dates if date and date.text]
    for i in range(len(dates)):
      concert = Concert(locations[i], dates[i])
      self.add_concert(concert)

  def add_concert(self, concert):
    self.concerts.append(concert)

  def add_concerts(self, concerts):
    self.concerts.extend(concerts)

  def find_concert(self, state):
    for concert in self.concerts:
      if state in concert.location:
        return concert
    
    return None

class Concert:
  @staticmethod
  def sanitize_location(raw_location):
    return raw_location

  @staticmethod
  def sanitize_date(raw_date):
    return raw_date

  def __init__(self, raw_location, raw_date):
    self.location = Concert.sanitize_location(raw_location)
    self.date = Concert.sanitize_date(raw_date)

  def __str__(self):
    return f"Location: {self.location}, Date: {self.date}"

def find_concerts(band, state):
  return band.find_concert(state)

@click.command()
@click.option('--state', default='WA', help='US state to search for concerts in')
def main(state):
  print(f"Searching for concerts in state: {state}")

  driver = webdriver.Chrome(WEBDRIVER_PATH) 

  jinjer = Band("Jinjer", "http://jinjer-metal.com/tour", driver)
  print(str(jinjer))

  driver.quit()

  print()

  concert = jinjer.find_concert(state)
  if concert:
    print(f"Found concert in {state}: {concert}")
  else:
    print(f"No concert found in: {state}")


if __name__ == "__main__":
  main()
