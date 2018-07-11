from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options


class SiteScraping:
    def __init__(self, url):
        self.url = url
        self.switch_flag = False
        self.header_flag = True
        self.exclusion_list = [
            " ",
            "仲介手数料",
            "その他交通",
            "販売代理",
            "物件名",
        ]

    def create_browser(self, headless_flag):
        if headless_flag:
            self.option = Options()
            self.option.set_headless()
            self.driver = webdriver.Firefox(options=self.option)
        else:
            self.driver = webdriver.Firefox()

    def get_url(self):
        return self.driver.current_url

    def window_switch(self):
        if not self.switch_flag:
            window_handles = self.driver.window_handles
            self.driver.switch_to_window(window_handles[1])
            self.switch_flag = True
        else:
            self.driver.switch_to_window(window_handles[0])
            self.switch_flag = False

    def scraping_data(self):
        pass

    def csv_write(self, filepath, lands_info):
        with open(filepath, "a", encoding="utf-8") as f:
            if self.header_flag:
                keys = ""
                for k in lands_info[0].keys():
                    if k in self.exclusion_list:
                        pass
                    else:
                        keys += (k + ",")
                f.write(keys.rstrip(",") + "\n")
                self.header_flag = False

            for land in lands_info:
                values = ""
                for key, value in land.items():
                    if key in self.exclusion_list:
                        pass
                    else:
                        values += (
                            value.replace("\n", " ").replace(",", "") + ",")
                f.write(values.rstrip(",") + "\n")

        # 書き込みの終了を伝える旨
        print("-> Writing data is finish")
