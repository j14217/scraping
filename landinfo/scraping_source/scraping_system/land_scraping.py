"""
Webスクレイピングを行う
"""

from time import sleep, time

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

# athomeテスト用(島根27件,鳥取83件)
prefs = [
    "島根"
]

# suumoテスト用(沖縄県60件:約12分)
# prefs = [
#     "沖縄県"
# ]

config = {}
config_path = ".\\venvtest\\Sourse\\scraping\\csv\\config.csv"

csv_input = CsvInput()

config = csv_input.config_reader("athome", config_path)

scraping = SiteScraping(config, prefs)

start_time = time()

scraping.open_browser(False)
scraping.move_land_page("go")

for pref in scraping.prefs:
    scraping.go_pref_page(pref)
    scraping.go_land_list_page()
    while True:

        land_list = scraping.get_land_list()
        for land in land_list:
            scraping.open_land_tab(land)
            scraping.scraping_data()
            scraping.close_land_tab()

        # 次のページがあるか判断
        try:
            # 次のページがあればそのページに遷移
            scraping.go_next_page()
        except:
            # なければ土地のトップに戻る
            scraping.move_land_page("back")
            break

    # 進捗を表示
    print("Progress : " + pref)
    finish_time = time()
    progress_time = (finish_time - start_time)/60
    print("-> Scraping is finish : " + str(progress_time) + "min")

    if scraping.site == "athome":
        csv_output1 = CsvOutput(scraping.csv_path1, scraping.lands_info1)
        csv_output2 = CsvOutput(scraping.csv_path2, scraping.lands_info2)
        csv_output1.csv_writer()
        csv_output2.csv_writer()

    else:
        csv_output = CsvOutput(scraping.csv_path1, scraping.lands_info)
        csv_output.csv_writer()

scraping.close_browser()
