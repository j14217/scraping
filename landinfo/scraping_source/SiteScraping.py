from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options


class SiteScraping:
    def __init__(self, headless, url):
        self.headless = headless
        self.url = url

    def create_browser(self):
        if self.headless:
            self.option = Options()
            self.option.set_headless()
            self.driver = webdriver.Firefox(options=self.option)
        else:
            self.driver = webdriver.Firefox()

    def get_url(self):
        return self.driver.current_url

    def window_switch(self, switching):
        if switching:
            window_handles = self.driver.window_handles
            self.driver.switch_to_window(window_handles[1])
        else:
            self.driver.switch_to_window(window_handles[0])

    def scraping_data(self):
        pass
