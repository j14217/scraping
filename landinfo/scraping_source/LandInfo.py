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
        self.traffic = "交通"
        self.location = "所在地"
        self.property_type = "物件種目"
        self.price = "価格"
        self.most_popular_price_range = "最多価格帯"
        self.other_expenses = "その他費用"
        self.facility = "設備"
        self.remarks = "備考"
        self.land_area = "土地面積"
        self.floor_space = "坪数"
        self.sales_divisions = "販売区画数"
        self.total_blocks = "総区画数"
        self.units_sold_total_units = "販売戸数/総戸数"
        self.private_road_burden = "私道負担"
        self.land_rights = "権利"
        self.city_planning = "都市計画"
        self.usage_area = "用途地域"
        self.build_cov_area_ratio = "建蔽率/容積率"
        self.contact_info = "接道情報"
        self.geography = "地目"
        self.development_permission_number = "開発許可等番号"
        self.estab_completion_time = "造成完成時期"
        self.delivery = "引渡し時期"
        self.scheduled_sales = "販売スケジュール"
        self.contact_infomation = "お問い合わせ先"
        self.parking = "駐車場"
        self.seller = "売主"
        self.info_provider = "情報提供元"
        self.info_update_date = "情報更新日"
        self.next_info_update_date = "次回更新予定日"

        self.column_list = [
            self.title, self.url, self.traffic, self.location,
            self.property_type, self.price, self.most_popular_price_range,
            self.other_expenses, self.facility, self.remarks, self.land_area,
            self.floor_space, self.sales_divisions, self.total_blocks,
            self.units_sold_total_units, self.private_road_burden,
            self.land_rights, self.city_planning, self.usage_area,
            self.build_cov_area_ratio, self.contact_info, self.geography,
            self.development_permission_number,
            self.estab_completion_time, self.delivery,
            self.scheduled_sales, self.contact_infomation, self.parking,
            self.seller, self.info_provider, self.info_update_date,
            self.next_info_update_date
        ]


# 土地情報の値を扱うクラス
# LandInfo1, LandInfo2
class LandInfo1:
    def __init__(self, title, location, traffic, building_coverage,
                 usage_area, conditions_etc, url, city_planning, contact_info,
                 current_status, delivery, facility, floor_area_ratio,
                 floor_space, geography, info_release_date, land_area,
                 land_law_notification, land_rights, lease_period_rent,
                 maintenance_costs_etc, next_info_update_date, notices,
                 optimal_use, other_expenses, price, private_road_burden,
                 property_no, property_type, remarks, right_money,
                 security_deposit, setback, topography, tsubo_unit_price):
        self.title = title
        self.url = url
        self.traffic = traffic
        self.location = location
        self.property_type = property_type
        self.price = price
        self.tsubo_unit_price = tsubo_unit_price
        self.lease_period_rent = lease_period_rent
        self.right_money = right_money
        self.security_deposit = security_deposit
        self.maintenance_costs_etc = maintenance_costs_etc
        self.other_expenses = other_expenses
        self.facility = facility
        self.notices = notices
        self.remarks = remarks
        self.land_area = land_area
        self.floor_space = floor_space
        self.optimal_use = optimal_use
        self.private_road_burden = private_road_burden
        self.land_rights = land_rights
        self.city_planning = city_planning
        self.usage_area = usage_area
        self.topography = topography
        self.building_coverage = building_coverage
        self.floor_area_ratio = floor_area_ratio
        self.contact_info = contact_info
        self.geography = geography
        self.land_law_notification = land_law_notification
        self.setback = setback
        self.conditions_etc = conditions_etc
        self.current_status = current_status
        self.delivery = delivery
        self.property_no = property_no
        self.info_release_date = info_release_date
        self.next_info_update_date = next_info_update_date


class LandInfo2:
    def __init__(self, title, location, traffic, build_cov_area_ratio,
                 usage_area, contact_infomation, url, city_planning,
                 contact_info, delivery, development_permission_number,
                 estab_completion_time, facility, floor_space, geography,
                 info_provider, info_update_date, land_area, land_rights,
                 most_popular_price_range, next_info_update_date,
                 other_expenses, parking, price, private_road_burden,
                 property_type, remarks, sales_divisions, scheduled_sales,
                 seller, total_blocks, units_sold_total_units):
        self.title = title
        self.url = url
        self.traffic = traffic
        self.location = location
        self.property_type = property_type
        self.price = price
        self.most_popular_price_range = most_popular_price_range
        self.other_expenses = other_expenses
        self.facility = facility
        self.remarks = remarks
        self.land_area = land_area
        self.floor_space = floor_space
        self.sales_divisions = sales_divisions
        self.total_blocks = total_blocks
        self.units_sold_total_units = units_sold_total_units
        self.private_road_burden = private_road_burden
        self.land_rights = land_rights
        self.city_planning = city_planning
        self.usage_area = usage_area
        self.build_cov_area_ratio = build_cov_area_ratio
        self.contact_info = contact_info
        self.geography = geography
        self.development_permission_number = development_permission_number
        self.estab_completion_time = estab_completion_time
        self.delivery = delivery
        self.scheduled_sales = scheduled_sales
        self.contact_infomation = contact_infomation
        self.parking = parking
        self.seller = seller
        self.info_provider = info_provider
        self.info_update_date = info_update_date
        self.next_info_update_date = next_info_update_date
