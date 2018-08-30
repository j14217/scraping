"""
DBへの挿入を行う
"""
import csv
import re
import traceback
from datetime import datetime

from CsvIO import CsvInput
from DbContoller import DbContoller
from LandInfo import LandColumns_at1, LandColumns_at2
from LandInfo import LandColumns_su, LandColumns_ya
from LandInfo import LandInfo_at1, LandInfo_at2, LandInfo_su, LandInfo_ya

def Insert_Db(web_site):
    # 各土地情報のオブジェクトを生成
    config_input = CsvInput()

    # 挿入するデータの抽出元サイト名を引数に渡す
    config = config_input.config_reader(web_site)

    try:
        # DB操作のオブジェクトを生成
        contoller = DbContoller()

        # csvファイルから情報を取り出して、DBに挿入
        # サイト名で分岐
        if config["site"] == "athome":
            columns_at1 = LandColumns_at1()
            columns_at2 = LandColumns_at2()

            # title,url,交通,所在地,物件種目,価格,坪単価,借地期間・地代（月額）,
            # 権利金,敷金 / 保証金,維持費等,その他一時金,設備,特記事項,備考,
            # 土地面積,坪数,最適用途,私道負担面積,土地権利,都市計画,用途地域,
            # 地勢,建ぺい率,容積率,接道状況,地目,国土法届出,セットバック,条件等,
            # 現況,引渡し（時期/方法）,物件番号,情報公開日,次回更新予定日 35
            with open(config["csvpath1"], newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    info_list = []
                    for k, v in row.items():
                        if v == '-':
                            info_list.append("－")
                        else:
                            if (k == columns_at1.price) or \
                                (k == columns_at1.land_area) or \
                                (k == columns_at1.floor_space) or \
                                    (k == columns_at1.tsubo_unit_price):
                                num = re.match("[0-9.]+", v.replace(",", ""))
                                if num:
                                    info_list.append(float(num.group(0)))
                                else:
                                    info_list.append(0)
                            elif k == columns_at1.info_release_date:
                                info_list.append(datetime.strptime(v, "%Y年%m月%d日"))
                            elif k == columns_at1.property_no:
                                info_list.append(int(v))
                            else:
                                info_list.append(v)
                    land_info = LandInfo_at1(info_list)
                    contoller.db_insert_at1(land_info)

            # title,url,造成完成時期,引渡し時期,販売スケジュール,価格,最多価格帯,その他費用,
            # 土地面積,坪数,販売区画数,総区画数,お問い合わせ先,物件種目,所在地,交通,建蔽率/容積率,
            # 私道負担,接道情報,駐車場,設備,権利,用途地域,都市計画,地目,開発許可等番号,
            # 備考,売主,情報提供元,情報更新日,次回更新予定日,販売戸数/総戸数 32
            with open(config["csvpath2"], newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    info_list = []
                    for k, v in row.items():
                        if (v == '-') or ("- / -" in v):
                            info_list.append(v.replace("-", "－"))
                        else:
                            if (k == columns_at2.price) or \
                                (k == columns_at2.land_area) or \
                                    (k == columns_at2.floor_space):
                                num = re.match("[0-9.]+", v.replace(",", ""))
                                if num:
                                    info_list.append(float(num.group(0)))
                                else:
                                    info_list.append(0)
                            elif k == columns_at2.info_update_date:
                                info_list.append(
                                    datetime.strptime(v, "%Y年%m月%d日"))
                            else:
                                info_list.append(v)
                    land_info = LandInfo_at2(info_list)
                    contoller.db_insert_at2(land_info)

        elif config["site"] == "suumo":
            columns_su = LandColumns_su()

            with open(config["csvpath1"], newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    info_list = []
                    for k, v in row.items():
                        if v == '-':
                            info_list.append("－")
                        else:
                            if (k == columns_su.price) or \
                                    (k == columns_su.land_area):
                                num = re.match("[0-9.億]+", v.replace(",", ""))
                                if num:
                                    num = num.group(0)
                                    if re.match("[0-9+]億$", num):
                                        info_list.append(
                                            float(num.replace("億", "0000")))
                                    else:
                                        info_list.append(
                                            float(num.replace("億", ""))
                                        )
                                else:
                                    info_list.append(0)
                            elif k == columns_su.info_release_date:
                                info_list.append(datetime.strptime(v, "%Y年%m月%d日"))
                            elif k == columns_su.traffic:
                                info_list.append(v.replace("-", "－"))
                            else:
                                info_list.append(v)
                    land_info = LandInfo_su(info_list)
                    contoller.db_insert_su(land_info)

        elif config["site"] == "yahoo":
            columns_ya = LandColumns_ya()

            with open(config["csvpath1"], newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    info_list = []
                    for k, v in row.items():
                        if v == '-':
                            info_list.append("－")
                        else:
                            if (k == columns_ya.price) or \
                                    (k == columns_ya.land_area):
                                num = re.match("[0-9.億]+", v.replace(",", ""))
                                if num:
                                    num = num.group(0)
                                    if re.match("[0-9+]億$", num):
                                        info_list.append(
                                            float(num.replace("億", "0000")))
                                    else:
                                        info_list.append(
                                            float(num.replace("億", ""))
                                        )
                                else:
                                    info_list.append(0)
                            elif k == columns_ya.build_cov_area_ratio:
                                info_list.append(v.replace("-", "－"))
                            elif k == columns_ya.location:
                                info_list.append(v.replace(" [地図を確認]", ""))
                            else:
                                info_list.append(v)
                    land_info = LandInfo_ya(info_list)
                    contoller.db_insert_ya(land_info)

        contoller.db_commit()

    except:
        # エラーが発生した場合、rollbackを行う
        print("-> error")
        print("---------------------------")
        print(traceback.format_exc())
        print("---------------------------")
        contoller.db_rollback()
    finally:
        #重複データの取り除く
        contoller.db_delete()
        # DBの接続を閉じる
        contoller.db_close()

    # DBへの挿入の完了を伝える旨
    print("-> Insert data for db finish")

if __name__ == '__main__':
    try:
        with open("./csv/setting.txt", encoding='utf-8') as fp:
            line = fp.readline()
        Insert_Db(line.replace('\n',''))
    except:
        traceback.print_exc()
    finally:
        input("任意のキーを押してください...")
