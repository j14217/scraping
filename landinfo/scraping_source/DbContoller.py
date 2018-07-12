"""
DBの操作を行う

pylintがある場合、以下のようなエラーが出力されるが、sqlalchemyに対応してない部分のため
E1120:No value for argument 'dml' in method call
"""

from sqlalchemy import create_engine, select, insert
from sqlalchemy import Table, Column, String, Integer, Numeric, Date, MetaData


# DBの操作クラス
class DbContoller:
    # DBの接続、トランザクション開始
    def __init__(self):
        self.url = 'postgresql+psycopg2://postgres:postgres'\
            '@192.168.0.159:5432/postgres'
        self.db_engine = create_engine(self.url)
        self.connection = self.db_engine.connect()
        self.trans = self.connection.begin()
        self.metadata = MetaData()
        self.land_table = Table('search_landinfo', self.metadata,
                                Column('id', Integer, primary_key=True),
                                Column('title', String(200)),
                                Column('location', String(200)),
                                Column('traffic', String(200)),
                                Column('build_cov_area_ratio', String(50)),
                                Column('building_coverage', String(50)),
                                Column('usage_area', String(50)),
                                Column('conditions_etc', String(200)),
                                Column('contact_infomation', String(200)),
                                Column('url', String(250)),
                                Column('city_planning', String(50)),
                                Column('contact_info', String(50)),
                                Column('current_status', String(50)),
                                Column('delivery', String(50)),
                                Column('development_permission_number',
                                       String(50)),
                                Column('estab_completion_time', String(50)),
                                Column('facility', String(200)),
                                Column('floor_area_ratio', String(50)),
                                Column('floor_space', Numeric(10, 2)),
                                Column('geography', String(50)),
                                Column('info_provider', String(200)),
                                Column('info_release_date', Date),
                                Column('info_update_date', Date),
                                Column('land_area', Numeric(10, 2)),
                                Column('land_law_notification', String(50)),
                                Column('land_rights', String(50)),
                                Column('lease_period_rent', String(50)),
                                Column('maintenance_costs_etc', String(50)),
                                Column('most_popular_price_range', String(50)),
                                Column('next_info_update_date', String(200)),
                                Column('notices', String(200)),
                                Column('optimal_use', String(50)),
                                Column('other_expenses', String(50)),
                                Column('parking', String(200)),
                                Column('price', Numeric(8, 2)),
                                Column('private_road_burden', String(50)),
                                Column('property_no', Numeric(10)),
                                Column('property_type', String(50)),
                                Column('remarks', String(300)),
                                Column('right_money', String(50)),
                                Column('sales_divisions', String(50)),
                                Column('scheduled_sales', String(200)),
                                Column('security_deposit', String(50)),
                                Column('seller', String(200)),
                                Column('setback', String(50)),
                                Column('topography', String(50)),
                                Column('total_blocks', String(50)),
                                Column('tsubo_unit_price', Numeric(8, 2)),
                                Column('units_sold_total_units', String(50)),
                                Column('company_profile', String(200)),
                                Column('event_info', String(200)),
                                Column('other_restrictions', String(200)),
                                )

    # 全件表示
    def db_select_all(self, table):
        select_data = select([self.land_table])
        results = self.connection.execute(select_data)
        print(results.fetchall())

    # DBへの挿入at1
    def db_insert_at1(self, land_info):
        # pylint: disable=E1120
        sql = self.land_table.insert().values(
            title=land_info.title,
            url=land_info.url,
            traffic=land_info.traffic,
            location=land_info.location,
            property_type=land_info.property_type,
            price=land_info.price,
            tsubo_unit_price=land_info.tsubo_unit_price,
            lease_period_rent=land_info.lease_period_rent,
            right_money=land_info.right_money,
            security_deposit=land_info.security_deposit,
            maintenance_costs_etc=land_info.maintenance_costs_etc,
            other_expenses=land_info.other_expenses,
            facility=land_info.facility,
            notices=land_info.notices,
            remarks=land_info.remarks,
            land_area=land_info.land_area,
            floor_space=land_info.floor_space,
            optimal_use=land_info.optimal_use,
            private_road_burden=land_info.private_road_burden,
            land_rights=land_info.land_rights,
            city_planning=land_info.city_planning,
            usage_area=land_info.usage_area,
            topography=land_info.topography,
            building_coverage=land_info.building_coverage,
            floor_area_ratio=land_info.floor_area_ratio,
            contact_info=land_info.contact_info,
            geography=land_info.geography,
            land_law_notification=land_info.land_law_notification,
            setback=land_info.setback,
            conditions_etc=land_info.conditions_etc,
            current_status=land_info.current_status,
            delivery=land_info.delivery,
            property_no=land_info.property_no,
            info_release_date=land_info.info_release_date,
            next_info_update_date=land_info.next_info_update_date
        )
        self.connection.execute(sql)

    # DBへの挿入at2
    def db_insert_at2(self, land_info):
        # pylint: disable=E1120
        sql = self.land_table.insert().values(
            title=land_info.title,
            url=land_info.url,
            estab_completion_time=land_info.estab_completion_time,
            delivery=land_info.delivery,
            scheduled_sales=land_info.scheduled_sales,
            price=land_info.price,
            most_popular_price_range=land_info.most_popular_price_range,
            other_expenses=land_info.other_expenses,
            land_area=land_info.land_area,
            floor_space=land_info.floor_space,
            sales_divisions=land_info.sales_divisions,
            total_blocks=land_info.total_blocks,
            contact_infomation=land_info.contact_infomation,
            property_type=land_info.property_type,
            location=land_info.location,
            traffic=land_info.traffic,
            build_cov_area_ratio=land_info.build_cov_area_ratio,
            private_road_burden=land_info.private_road_burden,
            contact_info=land_info.contact_info,
            parking=land_info.parking,
            facility=land_info.facility,
            land_rights=land_info.land_rights,
            usage_area=land_info.usage_area,
            city_planning=land_info.city_planning,
            geography=land_info.geography,
            development_permission_number=land_info.
            development_permission_number,
            remarks=land_info.remarks,
            seller=land_info.seller,
            info_provider=land_info.info_provider,
            info_update_date=land_info.info_update_date,
            next_info_update_date=land_info.next_info_update_date,
            units_sold_total_units=land_info.units_sold_total_units
        )
        self.connection.execute(sql)

    def db_insert_su(self, land_info):
        # pylint: disable=E1120
        sql = self.land_table.insert().values(
            title=land_info.title,
            url=land_info.url,
            scheduled_sales=land_info.scheduled_sales,
            event_info=land_info.event_info,
            location=land_info.location,
            traffic=land_info.traffic,
            sales_divisions=land_info.sales_divisions,
            total_blocks=land_info.total_blocks,
            price=land_info.price,
            most_popular_price_range=land_info.most_popular_price_range,
            private_road_burden=land_info.private_road_burden,
            other_expenses=land_info.other_expenses,
            land_area=land_info.land_area,
            build_cov_area_ratio=land_info.build_cov_area_ratio,
            current_status=land_info.current_status,
            estab_completion_time=land_info.estab_completion_time,
            land_rights=land_info.land_rights,
            conditions_etc=land_info.conditions_etc,
            delivery=land_info.delivery,
            geography=land_info.geography,
            usage_area=land_info.usage_area,
            other_restrictions=land_info.other_restrictions,
            notices=land_info.notices,
            company_profile=land_info.company_profile,
            contact_infomation=land_info.contact_infomation,
            info_release_date=land_info.info_release_date,
            next_info_update_date=land_info.next_info_update_date
        )
        self.connection.execute(sql)

    # DBのロールバック
    def db_rollback(self):
        print("-> Rollback db")
        self.trans.rollback()

    # DBへのコミット
    def db_commit(self):
        print("-> Commit for db")
        self.trans.commit()

    # DBの接続を閉じる
    def db_close(self):
        print("-> Db connection is close")
        self.connection.close()
