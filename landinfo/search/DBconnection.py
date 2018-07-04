from sqlalchemy import create_engine
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData,and_, or_, not_
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from .models import LandInfo

class landinfo:
    __tablename__ = 'search_landinfo'
    id = Column('id', Integer, primary_key=True)
    title =Column('title', String)
    location = Column('location', String)
    traffic= Column('traffic', String)
    build_cov_area_ratio= Column('build_cov_area_ratio', String)
    building_coverage= Column('building_coverage', String)
    usage_area= Column('usage_area', String)
    conditions_etc= Column('conditions_etc', String)
    contact_infomation= Column('contact_infomation', String)
    url= Column('url', String)
    city_planning= Column('city_planning', String)
    contact_info= Column('contact_info', String)
    current_status= Column('current_status', String)
    delivery= Column('delivery', String)
    development_permission_number= Column('development_permission_number', String)
    estab_completion_time= Column('estab_completion_time', String)
    facility= Column('facility', String)
    floor_area_ratio= Column('floor_area_ratio', String)
    floor_space= Column('floor_space', String)
    geography= Column('geography', String)
    info_release_date= Column('info_release_date', String)
    info_update_date= Column('info_update_date', String)
    land_area= Column('land_area', Integer)
    land_law_notification= Column('land_law_notification', String)
    land_rights= Column('land_rights', String)
    lease_period_rent= Column('lease_period_rent', String)
    maintenance_costs_etc= Column('maintenance_costs_etc', String)
    most_popular_price_range= Column('most_popular_price_range', String)
    next_info_update_date= Column('next_info_update_date', String)
    notices= Column('notices', String)
    optimal_use= Column('optimal_use', String)
    other_expenses= Column('other_expenses', String)
    parking= Column('parking', String)
    price= Column('price', String)
    private_road_burden= Column('private_road_burden', String)
    property_no= Column('property_no', String)
    property_type= Column('property_type', String)
    remarks= Column('remarks', String)
    right_money= Column('right_money', String)
    sales_divisions= Column('sales_divisions', String)
    scheduled_sales= Column('scheduled_sales', String)
    security_deposit= Column('security_deposit', String)
    seller= Column('seller', String)
    setback= Column('setback', String)
    topography= Column('topography', String)
    total_blocks= Column('total_blocks', String)
    tsubo_unit_price= Column('tsubo_unit_price', String)
    units_sold_total_units= Column('units_sold_total_units', String)

class selectland():
    url = 'postgresql://postgres:scrapingland@192.168.0.109:5432/postgres'
    engine = create_engine(url)
    conn = engine.connect()
    Session = sessionmaker(bind = engine)
    session = Session()
    metadata = MetaData()
    land_info = Table('search_landinfo', metadata,
        Column('id', Integer, primary_key=True),
        Column('title', String),
        Column('location', String),
        Column('traffic', String),
        Column('build_cov_area_ratio', String),
        Column('building_coverage', String),
        Column('usage_area', String),
        Column('conditions_etc', String),
        Column('contact_infomation', String),
        Column('url', String),
        Column('city_planning', String),
        Column('contact_info', String),
        Column('current_status', String),
        Column('delivery', String),
        Column('development_permission_number', String),
        Column('estab_completion_time', String),
        Column('facility', String),
        Column('floor_area_ratio', String),
        Column('floor_space', String),
        Column('geography', String),
        Column('info_release_date', String),
        Column('info_update_date', String),
        Column('land_area', Integer),
        Column('land_law_notification', String),
        Column('land_rights', String),
        Column('lease_period_rent', String),
        Column('maintenance_costs_etc', String),
        Column('most_popular_price_range', String),
        Column('next_info_update_date', String),
        Column('notices', String),
        Column('optimal_use', String),
        Column('other_expenses', String),
        Column('parking', String),
        Column('price', String),
        Column('private_road_burden', String),
        Column('property_no', String),
        Column('property_type', String),
        Column('remarks', String),
        Column('right_money', String),
        Column('sales_divisions', String),
        Column('scheduled_sales', String),
        Column('security_deposit', String),
        Column('seller', String),
        Column('setback', String),
        Column('topography', String),
        Column('total_blocks', String),
        Column('tsubo_unit_price', String),
        Column('units_sold_total_units', String),
    )
    def selectall(self):
        s = select([self.land_info.c.id,self.land_info.c.title])
        result = self.conn.execute(s)
        data = result.fetchall()
        return data
    def selectone(self,landinfo_id):
        s = select([self.land_info], self.land_info.c.id == landinfo_id)
        result = self.conn.execute(s)
        data = result.fetchone()
        return data
    def selectsearch(self,keywords):
        jouken ={}
        data = self.session.query(self.land_info.c.id,self.land_info.c.title)
        if keywords['title'] != '':
            jouken['title'] = self.land_info.c.title.like('%\\' + keywords['title'] + '%', escape='\\')
        if keywords['location'] !='':
            jouken['location']= self.land_info.c.location.like('%\\' + keywords['location'] + '%', escape='\\')
        for filter_land in jouken.values(): 
            data = data.filter(filter_land)
        data = data.all()
        return data
        

