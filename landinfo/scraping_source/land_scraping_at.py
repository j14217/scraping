"""
Webスクレイピングを行う
"""

import csv
from time import sleep

from dbconnection import DbConnect
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options

# preflist
# prefs = [
#    "北海道", "青森", "岩手", "秋田", "宮城", "山形", "福島",
#    "東京", "神奈川", "千葉", "群馬", "栃木", "茨城",
#    "山梨", "長野", "新潟", "石川", "富山", "福井",
#    "愛知", "静岡", "岐阜", "三重", "大阪", "兵庫", "京都",
#    "滋賀", "奈良", "和歌山", "広島", "岡山", "鳥取", "島根",
#    "山口", "香川", "愛媛", "徳島", "高知", "福岡", "佐賀",
#    "長崎", "大分", "熊本", "宮崎", "鹿児島", "沖縄"
# ]

# テスト用(島根27件,鳥取83件)
prefs = [
    "島根"
]

# 全土地情報の辞書リスト dictlist
lands_info1 = []
lands_info2 = []

# csvファイルのヘッダ書き込みのフラグ xxx
flag1 = 0
flag2 = 0

# csvファイルのパス xxx
csvpath1 = ".\\venvtest\\Sourse\\scraping\\csv\\land_info_at1.csv"
csvpath2 = ".\\venvtest\\Sourse\\scraping\\csv\\land_info_at2.csv"

# headlessモードでブラウザの生成
option = Options()
option.set_headless()
driver = webdriver.Firefox(options=option)

# サイトマップに遷移 startpage
driver.get("https://www.athome.co.jp/sitemap/")
sleep(1)

# 土地情報のページに遷移 landtoppage
driver.find_element_by_link_text("土地").click()
sleep(1)

# 各都道府県の全土地一覧ページ遷移
for pref in prefs:
    # 該当都道府県のページに遷移 xxx
    driver.find_element_by_id(
        "prefLinks").find_element_by_link_text(pref).click()
    sleep(1)

    # 該当都道府県の全土地一覧を表示 xxx
    driver.find_element_by_class_name("allList").click()
    sleep(1)

    # 土地情報の取得
    while True:
        # 土地のリスト xxx
        item_list = []
        item_list = driver.find_elements_by_css_selector(
            "p.heading.object-title")

        # 1ページの土地情報一覧から各土地のページに移り、土地情報を取得
        for item in item_list:
            title = item.find_element_by_css_selector(
                "a.boxHoverLinkStop").text
            # 土地ページを新しいタブで開く xxx
            item.find_element_by_css_selector("a.boxHoverLinkStop").click()
            sleep(2)

            # 開いたタブに制御を移動
            window_handles = driver.window_handles
            driver.switch_to_window(window_handles[1])
            sleep(2)

            # 建築条件の有無を判断 xxx
            condition = driver.find_element_by_css_selector(
                "form#bukken_detail_form").get_attribute("action")
            sleep(1)

            # 建築条件がある場合
            if condition == "https://www.athome.co.jp/"\
                    "inquiry/bukken/check/request/":
                # 物件概要のタブをクリック
                tabs = driver.find_element_by_css_selector(
                    "ul.clearfix.cm3_nav").find_elements_by_tag_name("li")
                tabs[3].find_element_by_tag_name("a").click()

                # 現在ページのurl取得 xxx
                url = driver.current_url

                # 物件情報をテーブルから取得
                tables = driver.find_elements_by_class_name("btbl")
                land_info = {}
                land_info["title"] = title
                land_info["url"] = url
                for table in tables:
                    trs = table.find_elements_by_tag_name("tr")
                    for tr in trs:
                        th = tr.find_element_by_tag_name("th").text
                        td = tr.find_element_by_tag_name("td").text
                        land_info[th] = td
                lands_info2.append(land_info)

            # 建築条件がない場合
            else:
                # 現在ページのurl取得
                url = driver.current_url

                # 物件情報をテーブルから取得
                land = driver.find_element_by_css_selector(
                    "section#item-detail_data")
                ths = land.find_elements_by_tag_name("th")
                tds = land.find_elements_by_tag_name("td")
                land_info = {}
                land_info["title"] = title
                land_info["url"] = url
                for th, td in zip(ths, tds):
                    th = th.text
                    td = td.text
                    land_info[th] = td
                lands_info1.append(land_info)
            # タブを閉じる
            driver.close()

            # 土地一覧のタブに制御を移動
            driver.switch_to_window(window_handles[0])
            sleep(1)

        # 次のページがあるか判断
        try:
            # 次のページがあればそのページに遷移
            driver.find_element_by_xpath(
                '//*[@id="item-list"]/div[1]/div[2]/ul'
            ).find_element_by_link_text("次へ").click()
            sleep(1)
        except:
            # なければループを抜ける
            break

    # 1都道府県ごとに進捗を表示
    print("Progress : " + pref)
    print("-> Scraping is finish")

    # csvファイルで保存、上書きで書き込み
    # 項目が異なる2種類土地データがある
    with open(csvpath1, "a", encoding="utf-8") as f:
        if flag1 == 0:
            keys = ""
            for k in lands_info1[0].keys():
                # 有無が不確定、不必要な情報を除外
                if (k == "仲介手数料") or (k == "その他交通") or (k == " "):
                    pass
                else:
                    keys += k + ","
            f.write(keys.rstrip(",") + "\n")
            flag1 = 1

        for land in lands_info1:
            values = ""
            for k, v in land.items():
                # 有無が不確定、不必要な情報を除外
                if (k == "仲介手数料") or (k == "その他交通") or (k == " "):
                    pass
                else:
                    values += (v.replace(",", "") + ",")
            f.write(values.replace("\n", " ").rstrip(",") + "\n")

    with open(csvpath2, "a", encoding="utf-8") as f:
        if flag2 == 0:
            keys = ""
            for k in lands_info2[0].keys():
                # 有無が不確定な情報を除外
                if (k == "販売代理") or (k == " "):
                    pass
                else:
                    keys += (k + ",")
            f.write(keys.rstrip(",") + "\n")
            flag2 = 1

        for land in lands_info2:
            values = ""
            for k, v in land.items():
                # 有無が不確定な情報を除外
                if (k == "販売代理") or (k == " "):
                    pass
                else:
                    values += (v.replace(",", "") + ",")
            f.write(values.replace("\n", " ").rstrip(",") + "\n")

    # 書き込みの終了を伝える旨
    print("-> Writing data is finish")

# ブラウザの破棄
driver.quit()
