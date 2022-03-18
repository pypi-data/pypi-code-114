# IMPORTS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def driver_create(PATH):
    global driver
    driver = webdriver.Chrome(PATH)
    driver.get("https://web.whatsapp.com/")

def locate_contact(contact_name):
    global driver
    x_arg = ' //span[contains(@title, ' + contact_name +')]'
    target = WebDriverWait(driver,600).until(EC.presence_of_element_located((By.XPATH, x_arg)))
    target.click()

def message(message,iter=1):
    global driver
    inp_xpath_search = "//div[@title='Type a message']"
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    for i in range(iter):
        input_box_search.send_keys(message)
        input_box_search.send_keys(Keys.RETURN)