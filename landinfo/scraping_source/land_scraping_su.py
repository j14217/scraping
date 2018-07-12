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

# テスト用(沖縄県60件)
prefs = [
    "沖縄県"
]

# 全土地情報の辞書リスト dictlist
lands_info = []

# csvファイルのヘッダ書き込みのフラグ xxx
flag = False

# csvファイルのパス
csvpath = ".\\venvtest\\Sourse\\scraping\\csv\\land_info_su.csv"

# headlessモードでブラウザの生成
# option = Options()
# option.set_headless()
# driver = webdriver.Firefox(options=option)
driver = webdriver.Firefox()

# サイトマップに遷移 startpage
driver.get("https://suumo.jp/sitemap/")
sleep(1)

# 土地情報のページに遷移 landtoppage
driver.find_element_by_css_selector(
    'div.main'
    ).find_element_by_link_text('土地購入').click()
land_top_url = driver.current_url
sleep(1)

# 各都道府県の全土地一覧ページ遷移
for pref in prefs:
    # 該当都道府県のページに遷移 xxx
    driver.find_element_by_xpath(
        "/html/body/div[3]/div/div/div/div[2]/div/div[1]/div[8]/div[2]"
        ).find_element_by_link_text(pref).click()
    sleep(1)

    # 該当都道府県の全土地一覧を表示 xxx
    driver.find_element_by_css_selector(
        "div.kr_kentop.kr_kentop--btnsearch02"
        ).click()
    sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="js-shiborikomiPanel"]/div[2]/a'
    ).click()
    sleep(1)

    while True:
        # 土地のリスト xxx
        item_list = []
        item_list = driver.find_element_by_xpath(
            '//*[@id="bukken_ichiran_JJ012FC001ActionForm"]'
        ).find_elements_by_css_selector("div.property_unit")

        for item in item_list:
            # 土地ページを新しいタブで開く xxx
            item.find_element_by_css_selector('a').click()
            sleep(2)

            # 開いたタブに制御を移動
            window_handles = driver.window_handles
            driver.switch_to_window(window_handles[1])
            sleep(2)

            if 'エラー' in driver.find_element_by_xpath(
                '/html/head/title'
            ).text:
                pass
            else:
                title = driver.find_element_by_css_selector(
                    'h1.fl.w420').text
                sleep(1)

                # 物件概要のタブが選択されたページに遷移
                tab_url = driver.find_element_by_link_text(
                    '物件概要'
                ).get_attribute("href")
                driver.get(tab_url)
                sleep(1)

                # 現在ページのurl取得
                url = driver.current_url

                # 物件情報をテーブルから取得
                land_info = {}
                land_info["title"] = title
                land_info["url"] = url
                tables = driver.find_elements_by_css_selector("tbody.vat.tal")
                for table in tables:
                    trs = table.find_elements_by_tag_name("tr")
                    for tr in trs:
                        ths = tr.find_elements_by_tag_name("th")
                        tds = tr.find_elements_by_tag_name("td")
                        for th, td in zip(ths, tds):
                            th = th.text.replace("\nヒント", "")
                            td = td.text
                            land_info[th] = td
                lands_info.append(land_info)

            # タブを閉じる
            driver.close()

            # 土地一覧のタブに制御を移動
            driver.switch_to_window(window_handles[0])
            sleep(1)

        # 次のページがあるか判断
        try:
            # 次のページがあればそのページに遷移
            driver.find_element_by_xpath(
                '//*[@id="js-sectionBody-main"]/div[1]/div[2]'
            ).find_element_by_link_text("次へ").click()
            sleep(1)
        except:
            # なければループを抜けて,土地のトップに戻る
            driver.get(land_top_url)
            break

    # 1都道府県ごとに進捗を表示
    print("Progress : " + pref)
    print("-> Scraping is finish")

    # csvファイルで保存、上書きで書き込み
    with open(csvpath, "w", encoding="utf-8") as f:
        if not flag:
            keys = ""
            for k in lands_info[0].keys():
                # 有無が不確定な情報を除外
                if (k == "物件名") or (k == " "):
                    pass
                else:
                    keys += (k + ",")
            f.write(keys.rstrip(",") + "\n")
            flag = True

        for land in lands_info:
            values = ""
            for k, v in land.items():
                # 有無が不確定な情報を除外
                if (k == "物件名") or (k == " "):
                    pass
                else:
                    values += (v.replace(",", "") + ",")
            f.write(values.replace("\n", " ").rstrip(",") + "\n")

    # 書き込みの終了を伝える旨
    print("-> Writing data is finish")

# ブラウザの破棄
driver.close()
