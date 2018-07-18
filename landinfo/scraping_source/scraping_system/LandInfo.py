"""
DBで扱う土地情報の項目と値を扱う
"""


# 土地情報の項目名を扱うクラス
# LandColumns_at1, LandColumns_at2, LandColumns_su
class LandColumns_at1:
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


class LandColumns_at2:
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


class LandColumns_su:
    def __init__(self):
        self.title = "title"
        self.url = "url"
        self.scheduled_sales = "販売スケジュール"
        self.event_info = "イベント情報"
        self.location = "所在地"
        self.traffic = "交通"
        self.sales_divisions = "販売区画数"
        self.total_blocks = "総区画数"
        self.price = "価格"
        self.most_popular_price_range = "最多価格帯"
        self.private_road_burden = "私道負担・道路"
        self.other_expenses = "諸費用"
        self.land_area = "土地面積"
        self.build_cov_area_ratio = "建ぺい率・容積率"
        self.current_status = "土地状況"
        self.estab_completion_time = "造成完了時期"
        self.land_rights = "土地の権利形態"
        self.conditions_etc = "建築条件"
        self.delivery = "引き渡し時期"
        self.geography = "地目"
        self.usage_area = "用途地域"
        self.other_restrictions = "その他制限事項"
        self.notices = "その他概要・特記事項"
        self.company_profile = "会社概要"
        self.contact_infomation = "問い合わせ先"
        self.info_release_date = "情報提供日"
        self.next_info_update_date = "次回更新日"


class LandColumns_ya:
    def __init__(self):
        self.title = "title"
        self.url = "url"
        self.price = "価格"
        self.location = "所在地"
        self.traffic = "交通"
        self.conditions_etc = "建築条件"
        self.land_area = "土地面積"
        self.build_cov_area_ratio = "建ぺい率/容積率"
        self.private_road_burden = "私道負担"
        self.estab_completion_time = "完成時期"
        self.delivery = "引渡し時期"
        self.current_status = "土地状況"
        self.geography = "地目"
        self.optimal_use = "最適用途"
        self.usage_area = "用途地域"
        self.land_rights = "土地権利形態"


# 土地情報の値を扱うクラス
# LandInfo_at1, LandInfo_at2, LandInfo_su, LandInfo_ya
class LandInfo_at1:
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
        self.land_info = []


class LandInfo_at2:
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
        self.land_info = []


class LandInfo_su:
    def __init__(self, info_list):
        self.title = info_list[0]
        self.url = info_list[1]
        self.scheduled_sales = info_list[2]
        self.event_info = info_list[3]
        self.location = info_list[4]
        self.traffic = info_list[5]
        self.sales_divisions = info_list[6]
        self.total_blocks = info_list[7]
        self.price = info_list[8]
        self.most_popular_price_range = info_list[9]
        self.private_road_burden = info_list[10]
        self.other_expenses = info_list[11]
        self.land_area = info_list[12]
        self.build_cov_area_ratio = info_list[13]
        self.current_status = info_list[14]
        self.estab_completion_time = info_list[15]
        self.land_rights = info_list[16]
        self.conditions_etc = info_list[17]
        self.delivery = info_list[18]
        self.geography = info_list[19]
        self.usage_area = info_list[20]
        self.other_restrictions = info_list[21]
        self.notices = info_list[22]
        self.company_profile = info_list[23]
        self.contact_infomation = info_list[24]
        self.info_release_date = info_list[25]
        self.next_info_update_date = info_list[26]
        self.land_info = []


class LandInfo_ya:
    def __init__(self, info_list):
        self.title = info_list[0]
        self.url = info_list[1]
        self.price = info_list[2]
        self.location = info_list[3]
        self.traffic = info_list[4]
        self.conditions_etc = info_list[5]
        self.land_area = info_list[6]
        self.build_cov_area_ratio = info_list[7]
        self.private_road_burden = info_list[8]
        self.estab_completion_time = info_list[9]
        self.delivery = info_list[10]
        self.current_status = info_list[11]
        self.geography = info_list[12]
        self.optimal_use = info_list[13]
        self.usage_area = info_list[14]
        self.land_rights = info_list[15]
        self.land_info = []
