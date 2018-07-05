"""
DBで扱う土地情報の項目と値を扱う
"""


# 土地情報の項目名を扱うクラス
# LandColumns1, LandColumns2
class LandColumns1:
    def __init__(self):
        self.title = "title"
        self.url = "url"
        self.traffic = "交通"
        self.location = "所在地"
        self.property_type = "物件種目"
        self.price = "価格"
        self.tsubo_unit_price = "坪単価"
        self.lease_period_rent = "借地期間・地代（月額）"
        self.right_money = "権利金"
        self.security_deposit = "敷金 / 保証金"
        self.maintenance_costs_etc = "維持費等"
        self.other_expenses = "その他一時金"
        self.facility = "設備"
        self.notices = "特記事項"
        self.remarks = "備考"
        self.land_area = "土地面積"
        self.floor_space = "坪数"
        self.optimal_use = "最適用途"
        self.private_road_burden = "私道負担面積"
        self.land_rights = "土地権利"
        self.city_planning = "都市計画"
        self.usage_area = "用途地域"
        self.topography = "地勢"
        self.building_coverage = "建ぺい率"
        self.floor_area_ratio = "容積率"
        self.contact_info = "接道状況"
        self.geography = "地目"
        self.land_law_notification = "国土法届出"
        self.setback = "セットバック"
        self.conditions_etc = "条件等"
        self.current_status = "現況"
        self.delivery = "引渡し（時期/方法）"
        self.property_no = "物件番号"
        self.info_release_date = "情報公開日"
        self.next_info_update_date = "次回更新予定日"

        self.column_list = [
            self.title, self.url, self.traffic, self.location,
            self.property_type, self.price, self.tsubo_unit_price,
            self.lease_period_rent, self.right_money, self.security_deposit,
            self.maintenance_costs_etc, self.other_expenses, self.facility,
            self.notices, self.remarks, self.land_area, self.floor_space,
            self.optimal_use, self.private_road_burden, self.land_rights,
            self.city_planning, self.usage_area, self.topography,
            self.building_coverage, self.floor_area_ratio, self.contact_info,
            self.geography, self.land_law_notification, self.setback,
            self.conditions_etc, self.current_status, self.delivery,
            self.property_no, self.info_release_date,
            self.next_info_update_date
        ]


class LandColumns2:
    def __init__(self):
        self.title = "title"
        self.url = "url"
        self.estab_completion_time = "造成完成時期"
        self.delivery = "引渡し時期"
        self.scheduled_sales = "販売スケジュール"
        self.price = "価格"
        self.most_popular_price_range = "最多価格帯"
        self.other_expenses = "その他費用"
        self.land_area = "土地面積"
        self.floor_space = "坪数"
        self.sales_divisions = "販売区画数"
        self.total_blocks = "総区画数"
        self.contact_infomation = "お問い合わせ先"
        self.property_type = "物件種目"
        self.location = "所在地"
        self.traffic = "交通"
        self.build_cov_area_ratio = "建蔽率/容積率"
        self.private_road_burden = "私道負担"
        self.contact_info = "接道情報"
        self.parking = "駐車場"
        self.facility = "設備"
        self.land_rights = "権利"
        self.usage_area = "用途地域"
        self.city_planning = "都市計画"
        self.geography = "地目"
        self.development_permission_number = "開発許可等番号"
        self.remarks = "備考"
        self.seller = "売主"
        self.info_provider = "情報提供元"
        self.info_update_date = "情報更新日"
        self.next_info_update_date = "次回更新予定日"
        self.units_sold_total_units = "販売戸数/総戸数"

        self.column_list = [
            self.title, self.url, self.estab_completion_time, self.delivery,
            self.scheduled_sales, self.price, self.most_popular_price_range,
            self.other_expenses, self.land_area, self.floor_space,
            self.sales_divisions, self.total_blocks, self.contact_infomation,
            self.property_type, self.location, self.traffic,
            self.build_cov_area_ratio, self.private_road_burden,
            self.contact_info, self.parking, self.facility, self.land_rights,
            self.usage_area, self.city_planning, self.geography,
            self.development_permission_number, self.remarks, self.seller,
            self.info_provider, self.info_update_date,
            self.next_info_update_date, self.units_sold_total_units
        ]


# 土地情報の値を扱うクラス
# LandInfo1, LandInfo2
class LandInfo1:
    def __init__(self, info_list):
        self.title = info_list[0]
        self.url = info_list[1]
        self.traffic = info_list[2]
        self.location = info_list[3]
        self.property_type = info_list[4]
        self.price = info_list[5]
        self.tsubo_unit_price = info_list[6]
        self.lease_period_rent = info_list[7]
        self.right_money = info_list[8]
        self.security_deposit = info_list[9]
        self.maintenance_costs_etc = info_list[10]
        self.other_expenses = info_list[11]
        self.facility = info_list[12]
        self.notices = info_list[13]
        self.remarks = info_list[14]
        self.land_area = info_list[15]
        self.floor_space = info_list[16]
        self.optimal_use = info_list[17]
        self.private_road_burden = info_list[18]
        self.land_rights = info_list[19]
        self.city_planning = info_list[20]
        self.usage_area = info_list[21]
        self.topography = info_list[22]
        self.building_coverage = info_list[23]
        self.floor_area_ratio = info_list[24]
        self.contact_info = info_list[25]
        self.geography = info_list[26]
        self.land_law_notification = info_list[27]
        self.setback = info_list[28]
        self.conditions_etc = info_list[29]
        self.current_status = info_list[30]
        self.delivery = info_list[31]
        self.property_no = info_list[32]
        self.info_release_date = info_list[33]
        self.next_info_update_date = info_list[34]


class LandInfo2:
    def __init__(self, info_list):
        self.title = info_list[0]
        self.url = info_list[1]
        self.estab_completion_time = info_list[2]
        self.delivery = info_list[3]
        self.scheduled_sales = info_list[4]
        self.price = info_list[5]
        self.most_popular_price_range = info_list[6]
        self.other_expenses = info_list[7]
        self.land_area = info_list[8]
        self.floor_space = info_list[9]
        self.sales_divisions = info_list[10]
        self.total_blocks = info_list[11]
        self.contact_infomation = info_list[12]
        self.property_type = info_list[13]
        self.location = info_list[14]
        self.traffic = info_list[15]
        self.build_cov_area_ratio = info_list[16]
        self.private_road_burden = info_list[17]
        self.contact_info = info_list[18]
        self.parking = info_list[19]
        self.facility = info_list[20]
        self.land_rights = info_list[21]
        self.usage_area = info_list[22]
        self.city_planning = info_list[23]
        self.geography = info_list[24]
        self.development_permission_number = info_list[25]
        self.remarks = info_list[26]
        self.seller = info_list[27]
        self.info_provider = info_list[28]
        self.info_update_date = info_list[29]
        self.next_info_update_date = info_list[30]
        self.units_sold_total_units = info_list[31]
