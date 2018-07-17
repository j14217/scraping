from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options


class SiteScraping:
    def __init__(self, config, prefs):
        self.prefs = prefs
        self.switch_flag = False
        self.land_top = ""
        self.site = config["site"]
        if self.site == "athome":
            self.lands_info1 = []
            self.lands_info2 = []
            self.start_page = config["start_page"]
            self.land_page_go = config["land_page_go"]
            self.land_link_text = config["land_link_text"]
            self.pref_element = config["pref_element"]
            self.land_all_page1 = config["land_all_page1"]
            self.land_list = config["land_list"]
            self.next_page = config["next_page"]
            self.csv_path1 = config["csvpath1"]
            self.csv_path2 = config["csvpath2"]

        elif self.site == "suumo":
            self.lands_info = []
            self.start_page = config["start_page"]
            self.land_page_go = config["land_page_go"]
            self.land_page_back = config["land_page_back"]
            self.land_link_text = config["land_link_text"]
            self.pref_element = config["pref_element"]
            self.land_all_page1 = config["land_all_page1"]
            self.land_all_page2 = config["land_all_page2"]
            self.land_list = config["land_list"]
            self.next_page = config["next_page"]
            self.csv_path = config["csvpath1"]

        elif self.site == "yahoo":
            self.lands_info = []

    def open_browser(self, headless_flag):
        if headless_flag:
            self.option = Options()
            self.option.set_headless()
            self.driver = webdriver.Firefox(options=self.option)
            self.driver.set_page_load_timeout(10)
            self.driver.implicitly_wait(10)
            self.driver.get(self.start_page)
            sleep(1)

        else:
            self.driver = webdriver.Firefox()
            self.driver.get(self.start_page)
            sleep(1)

    def close_browser(self):
        self.driver.quit()

    def get_url(self):
        return self.driver.current_url

    def go_url(self, url):
        self.driver.get(url)
        sleep(1)

    # 土地情報のページに遷移
    def move_land_page(self, action):
        if action == "go":
            self.driver.find_element_by_css_selector(
                self.land_page_go
            ).find_element_by_link_text(
                self.land_link_text
            ).click()

        elif action == "back":
            if self.site == "athome":
                pass
            elif self.site == "suumo":
                self.go_url(self.land_top)
                self.driver.find_element_by_css_selector(
                    self.land_page_back
                ).find_element_by_link_text(
                    self.land_link_text
                ).click()
            elif self.site == "yahoo":
                pass
        sleep(1)

    # 該当都道府県のページに遷移
    def go_pref_page(self, pref):
        if self.site == "athome":
            self.driver.find_element_by_css_selector(
                self.pref_element
            ).find_element_by_link_text(pref).click()
            sleep(1)
        elif self.site == "suumo":
            self.driver.find_element_by_xpath(
                self.pref_element
            ).find_element_by_link_text(pref).click()
            sleep(1)
            self.land_top = self.get_url()

    # 該当都道府県の全土地一覧を表示
    def go_land_list_page(self):
        if self.site == "athome":
            self.driver.find_element_by_css_selector(
                self.land_all_page1
            ).click()

        elif self.site == "suumo":
            self.driver.find_element_by_css_selector(
                self.land_all_page1).click()
            sleep(1)

            self.driver.find_element_by_xpath(
                self.land_all_page2).click()

        elif self.site == "yahoo":
            pass
        sleep(1)

    # 土地のリスト
    def get_land_list(self):
        land_list = self.driver.find_elements_by_css_selector(
            self.land_list)
        return land_list

    def go_next_page(self):
        self.driver.find_element_by_css_selector(
            self.next_page
        ).find_element_by_link_text("次へ").click()
        sleep(1)

    # タブの制御切り替え
    def window_switch(self):
        if not self.switch_flag:
            self.window_handles = self.driver.window_handles
            self.driver.switch_to_window(self.window_handles[1])
            self.switch_flag = True

        else:
            self.driver.switch_to_window(self.window_handles[0])
            self.switch_flag = False
        sleep(2)

    # ここでクリックできていないので、ウィンドウが1つしかない
    def open_land_tab(self, land):
        land.find_element_by_tag_name("a").click()
        sleep(2)
        self.window_switch()

    def close_land_tab(self):
        self.driver.close()
        self.window_switch()

    def scraping_data(self):
        if self.site == "athome":
            # 建築条件の有無を判断 xxx
            condition = self.driver.find_element_by_css_selector(
                "form#bukken_detail_form").get_attribute("action")
            sleep(1)

            # 建築条件がある場合
            if "/inquiry/bukken/check/request/" in condition:
                # title抽出
                title = self.driver.find_element_by_css_selector("h1.h1").text

                # 物件概要のタブをクリック
                tabs = self.driver.find_element_by_css_selector(
                    "ul.clearfix.cm3_nav").find_elements_by_tag_name("li")
                tabs[3].find_element_by_tag_name("a").click()

                # 現在ページのurl取得 xxx
                url = self.get_url()

                # 物件情報をテーブルから取得
                tables = self.driver.find_elements_by_class_name("btbl")
                land_info = {}
                land_info["title"] = title
                land_info["url"] = url
                for table in tables:
                    trs = table.find_elements_by_tag_name("tr")
                    for tr in trs:
                        th = tr.find_element_by_tag_name("th").text
                        td = tr.find_element_by_tag_name("td").text
                        land_info[th] = td
                self.lands_info2.append(land_info)

            # 建築条件がない場合
            else:
                # title抽出
                title = self.driver.find_element_by_css_selector(
                    "span.name").text
                # 現在ページのurl取得
                url = self.get_url()

                # 物件情報をテーブルから取得
                table = self.driver.find_element_by_css_selector(
                    "section#item-detail_data")
                ths = table.find_elements_by_tag_name("th")
                tds = table.find_elements_by_tag_name("td")
                land_info = {}
                land_info["title"] = title
                land_info["url"] = url
                for th, td in zip(ths, tds):
                    th = th.text
                    td = td.text
                    land_info[th] = td
                self.lands_info1.append(land_info)

        elif self.site == "suumo":
            # 削除された物件ページか判断
            condition = self.driver.find_element_by_xpath(
                '/html/head/title').text
            sleep(1)

            if 'エラー' in condition:
                pass
            else:
                title = self.driver.find_element_by_css_selector(
                    'h1.fl.w420').text
                sleep(1)

                # 物件概要のタブが選択されたページに遷移
                tab_url = self.driver.find_element_by_link_text(
                    '物件概要'
                ).get_attribute("href")
                self.driver.get(tab_url)
                sleep(1)

                # 現在ページのurl取得
                url = self.get_url()

                # 物件情報をテーブルから取得
                land_info = {}
                land_info["title"] = title
                land_info["url"] = url
                tables = self.driver.find_elements_by_css_selector(
                    "tbody.vat.tal")
                for table in tables:
                    trs = table.find_elements_by_tag_name("tr")
                    for tr in trs:
                        ths = tr.find_elements_by_tag_name("th")
                        tds = tr.find_elements_by_tag_name("td")
                        for th, td in zip(ths, tds):
                            th = th.text.replace("\nヒント", "")
                            td = td.text
                            land_info[th] = td
                self.lands_info.append(land_info)

        elif self.site == "yahoo":
            pass
