import csv
import json
import traceback
import re
from datetime import datetime

from LandInfo import LandInfoTest, LandInfo1, LandInfo2
from dbconnection import DbConnect

csvpath1 = ".\\venvtest\\Sourse\\scraping\\land_info1.csv"
csvpath2 = ".\\venvtest\\Sourse\\scraping\\land_info2.csv"
csvpathtest = ".\\venvtest\\Sourse\\scraping\\test.csv"

try:
    # columns_test = LandInfoTest()
    columns1 = LandInfo1()
    columns2 = LandInfo2()
    connect = DbConnect()

    # with open(csvpathtest, newline="", encoding="utf-8") as f:
    #     reader = csv.DictReader(f)
    #     for row in reader:
    #         info_list = []
    #         for k, v in row.items():
    #             for column in columns_test.column_list:
    #                 if k == column:
    #                     info_list.append(v)
    #                 else:
    #                     pass
    #         info_tuple = (
    #             info_list[0], info_list[1], info_list[2], info_list[3]
    #         )
    #         columns_test.info_tuple_format(info_tuple)
    #         connect.db_insert_test("search_landinfo", columns_test.columns, columns_test.tuple)

    # TODO ファイルを読み込み、辞書にして、キーで選別
    # TODO 仲介手数料の要素があったりなかったりするので要素数が合わないことの修正
    # title,url,交通,所在地,物件種目,価格,坪単価,借地期間・地代（月額）,
    # 権利金,敷金 / 保証金,維持費等,その他一時金,設備,特記事項,備考,
    # 土地面積,坪数,最適用途,私道負担面積,土地権利,都市計画,用途地域,
    # 地勢,建ぺい率,容積率,接道状況,地目,国土法届出,セットバック,条件等,
    # 現況,引渡し（時期/方法）,物件番号,情報公開日,次回更新予定日 35
    with open(csvpath1, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            info_list = []
            for k, v in row.items():
                if k in columns1.column_list:
                    if v == '－':
                        info_list.append(None)
                    else:
                        if (k == columns1.price) or (k == columns1.land_area) or (k == columns1.floor_space):
                            num = re.match("[0-9]+(.[0-9]+)$", v.replace(",", ""))
                            if num:
                                info_list.append(float(num.group(0)))
                            else:
                                info_list.append(None)
                        elif (k == columns1.info_release_date) or (k == columns1.next_info_update_date):                        
                            info_list.append(datetime.strptime(v, "%Y年%m月%d日"))
                        else:
                            info_list.append(v)
            info_tuple = (
                info_list[0], info_list[1], info_list[2], info_list[3], info_list[4],
                info_list[5], info_list[6], info_list[7], info_list[8], info_list[9],
                info_list[10], info_list[11], info_list[12], info_list[13], info_list[14],
                info_list[15], info_list[16], info_list[17], info_list[18], info_list[19],
                info_list[20], info_list[21], info_list[22], info_list[23], info_list[24],
                info_list[25], info_list[26], info_list[27], info_list[28], info_list[29],
                info_list[30], info_list[31], info_list[32], info_list[33], info_list[34]
            )
            print(info_tuple)
            connect.db_insert1("search_landinfo", columns1.columns, info_tuple)

    # TODO info_tubleの要素数が2つ多いのが不明なので要検証
    # title,url,造成完成時期,引渡し時期,販売スケジュール,価格,最多価格帯,その他費用,
    # 土地面積,坪数,販売区画数,総区画数,お問い合わせ先,物件種目,所在地,交通,建蔽率/容積率,
    # 私道負担,接道情報,駐車場,設備,権利,用途地域,都市計画,地目,開発許可等番号,
    # 備考,売主,情報提供元,情報更新日,次回更新予定日,販売戸数/総戸数 32
    with open(csvpath2, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            info_list = []
            for k, v in row.items():
                if k in columns2.column_list:
                    if v == '－':
                        info_list.append(None)
                    else:
                        if (k == columns2.price) or (k == columns2.land_area) or (k == columns2.floor_space):
                            num = re.match("[0-9]+(.[0-9]+)$", v.replace(",", ""))
                            if num:
                                info_list.append(float(num.group(0)))
                            else:
                                info_list.append(None)
                        elif (k == columns2.info_update_date) or (k == columns2.next_info_update_date):                        
                            info_list.append(datetime.strptime(v, "%Y年%m月%d日"))
                        else:
                            info_list.append(v)
            info_tuple = (
                info_list[0], info_list[1], info_list[2], info_list[3], info_list[4],
                info_list[5], info_list[6], info_list[7], info_list[8], info_list[9],
                info_list[10], info_list[11], info_list[12], info_list[13], info_list[14],
                info_list[15], info_list[16], info_list[17], info_list[18], info_list[19],
                info_list[20], info_list[21], info_list[22], info_list[23], info_list[24],
                info_list[25], info_list[26], info_list[27], info_list[28], info_list[29],
                info_list[30], info_list[31]
            )
            connect.db_insert2("search_landinfo", columns2.columns, info_tuple)

except:
    print("error")
    print(traceback.format_exc())
    connect.db_rollback()
finally:
    connect.db_commit()
    connect.db_close()
#    pass