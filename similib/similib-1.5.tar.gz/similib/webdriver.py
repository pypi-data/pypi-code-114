from selenium import webdriver


class WebDriverHub():
    def __init__(self, ip):
        self.ip = ip
        self.cap = {
            "browserName": "chrome",

        }

    def get_driver(self, port):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Remote("http://{}:{}/wd/hub".format(self.ip, port), self.cap, options=options, )
        return driver
