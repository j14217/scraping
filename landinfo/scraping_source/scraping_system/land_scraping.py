"""
Webスクレイピングを行う
"""

from time import sleep

from CsvIO import CsvInput, CsvOutput
from SiteScraping import SiteScraping
from DbContoller import DbContoller

# 最終的に収集する都道府県は引数としてリストで渡す

# prefs = [
#    "北海道", "青森県", "岩手県", "秋田県", "宮城県", "山形県", "福島県",
#    "東京都", "神奈川県", "千葉県", "群馬県", "栃木県", "茨城県",
#    "山梨県", "長野県", "新潟県", "石川県", "富山県", "福井県",
#    "愛知県", "静岡県", "岐阜県", "三重県", "大阪府", "兵庫県", "京都府",
#    "滋賀県", "奈良県", "和歌山県", "広島県", "岡山県", "鳥取県", "島根県",
#    "山口県", "香川県", "愛媛県", "徳島県", "高知県", "福岡県", "佐賀県",
#    "長崎県", "大分県", "熊本県", "宮崎県", "鹿児島県", "沖縄県"
# ]

# suumoテスト用(沖縄県60件)
prefs = [
    "沖縄県"
]

config = {}
config_path = ".\\venvtest\\Sourse\\scraping\\csv\\config.csv"

csv_input = CsvInput()

config = csv_input.config_reader("suumo", config_path)

scraping = SiteScraping(config, prefs)

scraping.open_browser(False)
scraping.lands_page()

for pref in scraping.prefs:
    scraping.land_pref_page(pref)
    scraping.land_all_page()
    scraping.driver.get(scraping.land_top)
    sleep(1)
    scraping.driver.find_element_by_css_selector(
        "ol.breadcrumb-list"
        ).find_element_by_link_text("土地").click()
    sleep(1)

scraping.close_browser()
