from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options


class SiteScraping:
    def __init__(self, config, prefs):
        self.config = config
        self.initialize(self.config)
        self.prefs = prefs
        self.switch_flag = False

    def initialize(self, config):
        self.start_page = config["start_page"]

        if config["site"] == "athome":
            pass

        elif config["site"] == "suumo":
            self.land_page = config["land_page"]
            self.land_link_text = config["land_link_text"]
            self.pref_element = config["pref_element"]
            self.land_all_page1 = config["land_all_page1"]
            self.land_all_page2 = config["land_all_page2"]

        elif self.config["site"] == "yahoo":
            pass

    def open_browser(self, headless_flag):
        if headless_flag:
            self.option = Options()
            self.option.set_headless()
            self.driver = webdriver.Firefox(options=self.option)
            self.driver.set_page_load_timeout(10)
            self.driver.implicitly_wait(5)
            self.driver.get(self.start_page)
            sleep(1)

        else:
            self.driver = webdriver.Firefox()
            self.driver.get(self.start_page)
            sleep(1)

    def close_browser(self):
        self.driver.close()

    def get_url(self):
        return self.driver.current_url

    # 土地情報のページに遷移
    def lands_page(self):
        self.driver.find_element_by_css_selector(
            self.land_page
        ).find_element_by_link_text(self.land_link_text).click()
        self.land_top = self.get_url()
        sleep(1)

    # 該当都道府県のページに遷移
    def land_pref_page(self, pref):
        self.driver.find_element_by_xpath(
            self.pref_element
        ).find_element_by_link_text(pref).click()
        sleep(1)

    # 該当都道府県の全土地一覧を表示
    def land_all_page(self):
        if self.config["site"] == "athome":
            pass

        elif self.config["site"] == "suumo":
            self.driver.find_element_by_css_selector(
                self.land_all_page1).click()
            sleep(1)

            self.driver.find_element_by_xpath(
                self.land_all_page2).click()
            sleep(1)

        elif self.config["site"] == "yahoo":
            pass

    # タブの制御切り替え
    def window_switch(self):
        if not self.switch_flag:
            window_handles = self.driver.window_handles
            self.driver.switch_to_window(window_handles[1])
            self.switch_flag = True
            sleep(2)

        else:
            self.driver.switch_to_window(window_handles[0])
            self.switch_flag = False
            sleep(2)

    def scraping_data(self):
        if self.config["site"] == "athome":
            pass

        elif self.config["site"] == "suumo":
            pass

        elif self.config["site"] == "yahoo":
            pass
