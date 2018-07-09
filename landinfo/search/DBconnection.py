from sqlalchemy import create_engine
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData,and_, or_, not_
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from .models import LandInfo

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

    #引数のdataにはレコードが存在するよう加工する必要あり(selectall参照)
    def None_delete(self,data):
        dictdata = dict(data)
        for colum in dictdata:
            if dictdata[colum] == None:
                dictdata[colum] = 'なし'
        return dictdata

    def selectall(self):
        ds =[]
        s = select([self.land_info])
        result = self.conn.execute(s)
        data = result.fetchall()
        for colum in data:
            dictd = self.None_delete(colum) 
            ds.append(dictd)
        return ds
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
        

