import csv
import traceback
from time import sleep, time

from dbconnection import DbConnect
from selenium import webdriver
from selenium.webdriver.support.select import Select

from filedatadb import data_insert_db

#prefs = [
#    "北海道", "青森", "岩手", "秋田", "宮城", "山形", "福島",
#    "東京", "神奈川", "千葉", "群馬", "栃木", "茨城", 
#    "山梨", "長野", "新潟", "石川", "富山", "福井",
#    "愛知", "静岡", "岐阜", "三重", "大阪", "兵庫", "京都",
#    "滋賀", "奈良", "和歌山", "広島", "岡山", "鳥取", "島根",
#    "山口", "香川", "愛媛", "徳島", "高知", "福岡", "佐賀",
#    "長崎", "大分", "熊本", "宮崎", "鹿児島", "沖縄"
#]

#テスト用(島根27件,鳥取83件)
prefs = [
    "島根" 
]

# 全土地情報の辞書
lands_info1 = []
lands_info2 = []
# 各土地に割り振った番号
land_num = 0

flag1 = 0
flag2 = 0

csvpath1 = ".\\venvtest\\Sourse\\scraping\\land_info1.csv"
csvpath2 = ".\\venvtest\\Sourse\\scraping\\land_info2.csv"

# ブラウザの生成
driver = webdriver.Firefox()

# athomeサイトマップに遷移
driver.get("https://www.athome.co.jp/sitemap/")
sleep(1)

# 土地情報のページに遷移
driver.find_element_by_link_text("土地").click()
sleep(1)

# 各都道府県の全土地一覧ページ遷移
for pref in prefs:
    start = time()
    # 該当都道府県のページに遷移
    driver.find_element_by_id("prefLinks").find_element_by_link_text(pref).click()
    sleep(1)

    # 該当都道府県の全土地一覧を表示
    driver.find_element_by_class_name("allList").click()
    sleep(1)

    # 該当都道府県の土地情報件数
    lands_num = driver.find_element_by_css_selector(
    "dl.head-counter.pie").find_element_by_css_selector(
    "span.num").text.replace(",", "")

    # ページごとの土地件数
    find_lands = Select(driver.find_element_by_css_selector(
        "select.bukken-limit")).all_selected_options
    find_lands = find_lands[0].get_attribute("value")

    # ページ数
    page = int(lands_num) // int(find_lands)

    # 1ページのみの場合
    if page == 0:
        page = 2

    # 土地情報の取得
    while range(page - 1):
        # 土地のリスト
        item_list = []
        item_list = driver.find_elements_by_css_selector("p.heading.object-title")

        # 1ページの土地情報一覧から各土地のページに移り、土地情報を取得
        for item in item_list:
            title = item.find_element_by_css_selector("a.boxHoverLinkStop").text
            # 土地ページを新しいタブで開く
            item.find_element_by_css_selector("a.boxHoverLinkStop").click()
            sleep(2)

            # 開いたタブに制御を移動
            window_handles = driver.window_handles
            driver.switch_to_window(window_handles[1])
            sleep(2)

            # 建築条件の有無を判断
            condition = driver.find_element_by_css_selector(
                "form#bukken_detail_form").get_attribute("action")
            
            # 建築条件がある場合
            if condition == "https://www.athome.co.jp/inquiry/bukken/check/request/":
                # 物件概要のタブをクリック
                tabs = driver.find_element_by_css_selector(
                    "ul.clearfix.cm3_nav").find_elements_by_tag_name("li")
                tabs[3].find_element_by_tag_name("a").click()
                sleep(1)

                # 現在ページのurl取得
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
                land = driver.find_element_by_css_selector("section#item-detail_data")
                tables = land.find_element_by_class_name("left")
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
            next = driver.find_element_by_css_selector(
                "ul.paging.typeInline.right").find_element_by_link_text("次へ").click()
            sleep(1)
        except:
            #なければループを抜ける
            break
    end = time()
    
    # 1都道府県ごとに進捗を表示
    print("Progress : " + pref)
    print("-> Scraping is finish")

    # TODO ファイルに書き込み 
    # そのままcsvにしたいが、キーが異なる2種類土地データがある
    with open(csvpath1, "a", encoding="utf-8") as f:
        if flag1 == 0:
            keys = ""
            for k in lands_info1[0].keys():
                keys += k + ","
            f.write(keys.rstrip(",") + "\n")
            flag1 = 1

        for land in lands_info1:
            values = ""
            for k, v in land.items():
                # 有無が不確定な情報を除外
                if (k == "仲介手数料") or (k == "その他交通"):
                    pass 
                else:
                    values += (v.replace(",", "") + ",")
            f.write(values.replace("\n", " ").rstrip(",") + "\n")
        
    with open(csvpath2, "a", encoding="utf-8") as f:
        if flag2 == 0:
            keys = ""
            for k in lands_info2[0].keys():
                keys += (k + ",")
            f.write(keys.rstrip(",") + "\n")
            flag2 == 1

        for land in lands_info2:
            values = ""
            for k, v in land.items():
                # 有無が不確定な情報を除外
                if k == "販売代理":
                    pass 
                else:
                    values += (v.replace(",", "") + ",")
            f.write(values.replace("\n", " ").rstrip(",") + "\n")

    # 書き込みの終了を伝える旨
    print("-> Writing data is finish")

    try:
        # DB操作のオブジェクトを生成　
        connect = DbConnect()
        data_insert_db(csvpath1, csvpath2, connect)
    except:
        # エラーが発生した場合、rollbackを行う
        print("-> error")
        print("---------------------------")
        print(traceback.format_exc())
        print("---------------------------")
        connect.db_rollback()    
    finally:
        # 必ずcommitを行い、DBの接続を閉じる
        connect.db_commit()
        connect.db_close()

    # 書き込みの終了を伝える旨
    print("-> Insert data for db finish")
    # print("process time : " + str(int(end - start)) + " sec")

# ブラウザの破棄
driver.quit()
