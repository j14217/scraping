import csv
import json
import traceback

from LandInfo import LandInfo
from dbconnection import DbConnect

csvpath1 = ".\\venvtest\\Sourse\\scraping\\land_info1.csv"
csvpath2 = ".\\venvtest\\Sourse\\scraping\\land_info2.csv"
csvpathtest = ".\\venvtest\\Sourse\\scraping\\test.csv"

try:
    columns = LandInfo()
    connect = DbConnect()
    """
    # TODO ファイルを読み込み、辞書にして、キーで選別
    # title,url,造成完成時期,引渡し時期,販売スケジュール,価格,最多価格帯,その他費用,
    # 土地面積,坪数,販売区画数,総区画数,お問い合わせ先,物件種目,所在地,交通,建蔽率/容積率,
    # 私道負担,接道情報,駐車場,設備,権利,用途地域,都市計画,地目,開発許可等番号,
    # 備考,売主,情報提供元,情報更新日,次回更新予定日,販売戸数/総戸数
    with open(csvpath1, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for k, v in row.items():
                if k == columns.title:
                    print(k, v)
                elif k == columns.url:
                    print(k, v)
                elif k == columns.location:
                    print(k, v)
                elif k == columns.price:
                    print(k, v)
                elif k == columns.traffic:
                    print(k, v)
                else:
                    pass

    # title,url,交通,所在地,物件種目,価格,坪単価,借地期間・地代（月額）,
    # 権利金,敷金 / 保証金,維持費等,その他一時金, ,設備,特記事項,備考,
    # 土地面積,坪数,最適用途,私道負担面積,土地権利,都市計画,用途地域,
    # 地勢,建ぺい率,容積率,接道状況,地目,国土法届出,セットバック,条件等,
    # 現況,引渡し（時期/方法）,物件番号,情報公開日,次回更新予定日
    with open(csvpath2, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for k, v in row.items():
                if k == columns.title:
                    print(k, v)
                elif k == columns.url:
                    print(k, v)
                elif k == columns.location:
                    print(k, v)
                elif k == columns.price:
                    print(k, v)
                elif k == columns.traffic:
                    print(k, v)
                else:
                    pass
    """
    with open(csvpath1, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            columns.info_list_clear()
            for k, v in row.items():
                if k == columns.title:
                    columns.info_list_add(0, v)
                elif k == columns.location:
                    columns.info_list_add(1, v)
                elif k == columns.traffic:
                    columns.info_list_add(2, v)
                elif k == columns.url:
                    columns.info_list_add(3, v)
                else:
                    pass
            connect.db_insert("land_info",columns.list)
except:
    print("error")
    print(traceback.format_exc())
    connect.db_rollback()
finally:
    connect.db_commit()
    connect.db_close()
