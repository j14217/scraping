class LandInfoTest:
    def __init__(self):
        self.title = "title"
        self.location = "所在地"
        self.traffic = "交通"
        self.url = "url"

        self.column_list = [
            self.title, self.location, self.traffic, self.url
        ]

        self.columns = "title, location, traffic, url"

    def info_tuple_format(self, info):
        self.tuple = info

class LandInfo1:
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
        self.info_update_date = "情報公開日"
        self.next_info_update_date = "次回更新予定日"

        self.column_list = [
            self.title, self.url, self.traffic, self.location,
            self.property_type, self.price, self.tsubo_unit_price,
            self.lease_period_rent, self.right_money, self.security_deposit,
            self.maintenance_costs_etc, self.other_expenses, self.facility,
            self.notices, self.remarks,self.land_area, self.floor_space,
            self.optimal_use, self.private_road_burden,self.land_rights,
            self.city_planning, self.usage_area, self.topography,
            self.building_coverage, self.floor_area_ratio, self.contact_info,
            self.geography,self.land_law_notification, self.setback,
            self.conditions_etc, self.current_status,self.delivery,
            self.property_no, self.info_update_date,
            self.next_info_update_date
        ]

        self.columns = "title, url, traffic, location, property_type, price, "\
            "tsubo_unit_price, lease_period_rent, right_money, security_deposit, "\
            "maintenance_costs_etc, other_expenses, facility, notices, remarks, "\
            "land_area, floor_space, optimal_use, private_road_burden, "\
            "land_rights, city_planning, usage_area, topography, "\
            "building_coverage, floor_area_ratio, contact_info, geography, "\
            "land_law_notification, setback, conditions_etc, current_status, "\
            "delivery, property_no, info_update_date, next_info_update_date"

    def info_tuple_format(self, info):
        self.tuple = info


class LandInfo2:
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
        self.building_coverage_floor_area_ratio = "建蔽率/容積率"
        self.contact_info = "接道状況"
        self.geography = "地目"
        self.development_permission_number = "開発許可等番号"
        self.establishment_completion_time = "造成完成時期"
        self.delivery = "引渡し時期"
        self.scheduled_sales = "販売スケジュール"
        self.contact_infomation = "お問い合わせ先"
        self.seller = "売主"
        self.info_provider = "情報提供元"
        self.info_update_date = "情報更新日"
        self.next_info_update_date = "次回更新予定日"

        self.column_list = [
            self.title, self.url, self.traffic, self.location,
            self.property_type, self.price,self.most_popular_price_range,
            self.other_expenses, self.facility, self.remarks,self.land_area,
            self.floor_space, self.sales_divisions, self.total_blocks,
            self.units_sold_total_units, self.private_road_burden,
            self.land_rights,self.city_planning, self.usage_area,
            self.building_coverage_floor_area_ratio, self.contact_info, self.geography,
            self.development_permission_number,
            self.establishment_completion_time, self.delivery,
            self.scheduled_sales, self.contact_infomation, self.seller,
            self.info_provider, self.info_update_date,
            self.next_info_update_date
        ]

        self.columns = "title, url, traffic, location, property_type, price, "\
            "most_popular_price_range, other_expenses, facility, remarks, "\
            "land_area, floor_space, sales_divisions, total_blocks, "\
            "units_sold_total_units, private_road_burden, land_rights, "\
            "city_planning, usage_area, building_floor_area_ratio, "\
            "contact_info, geography, development_permission_number, "\
            "establishment_completion_time, delivery, scheduled_sales, "\
            "contact_infomation, seller, info_provider, info_update_date, "\
            "next_info_update_date"

    def info_tuple_format(self, info):
        self.tuple = info
