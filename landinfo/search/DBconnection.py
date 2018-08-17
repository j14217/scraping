from sqlalchemy import create_engine
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData,and_, or_, not_
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from .models import LandInfo
from django.db import connection

class selectland():
    #DB接続部分
    #url = 'postgresql://postgres:postgres@192.168.0.159:5432/postgres'
    #localhostに変換
    url = 'postgresql://postgres:postgres@127.0.0.1:5432/postgres'
    engine = create_engine(url)
    conn = engine.connect()
    #Session = sessionmaker(bind = engine)
    #session = Session()
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
        Column('land_area', String),
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
        Column('price', Integer),
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

    #カラム内のNoneデータを文字列「-」に変更する機能
    #※実装しているのはselectallのみ
    def None_delete(self,data):
        dictdata = dict(data)
        for colum in dictdata:
            if dictdata[colum] == None:
                dictdata[colum] = '-'
        return dictdata
    #DBの全レコードを受け取る
    def selectall(self):
        ds =[]
        s = select([self.land_info])
        result = self.conn.execute(s)
        data = result.fetchall()
        for colum in data:
            dictd = self.None_delete(colum) 
            ds.append(dictd)
        return ds
    #IDに紐づいたレコード一件の表示(詳細画面用)
    def selectone(self,landinfo_id):
        s = select([self.land_info], self.land_info.c.id == landinfo_id)
        result = self.conn.execute(s)
        data = result.fetchone()
        return data
    #検索フォームの条件を基に絞り込む機能
    #keywords:POSTリクエストで受け取った辞書データ
    def selectsearch(self,keywords):
        
        #DjangoのオブジェクトでQuerySetを生成
        data = LandInfo.objects.all()

        #filterに使用できる各メソッドの参考：https://codelab.website/django-queryset-filter/
        #価格上限(入力フォームが空の場合、処理を飛ばす)
        if keywords['max_price']:
            data = data.filter(price__lte = keywords['max_price'])
        #価格下限
        if keywords['min_price']:
            data = data.filter(price__gte = keywords['min_price'])
        #面積上限
        if keywords['max_area']:
            data = data.filter(land_area__lte = keywords['max_area'])
        #面積下限
        if keywords['min_area']:
            data = data.filter(land_area__gte = keywords['min_area'])
        #タイトル検索(部分一致大文字小文字区別なし)
        if keywords['title']:
            data = data.filter(title__icontains = keywords['title'])
        #所在地検索(部分一致大文字小文字区別なし)
        if keywords['location']:
            data = data.filter(location__icontains = keywords['location'])
        #交通検索
        if keywords['traffic']:
            data = data.filter(traffic__icontains = keywords['traffic'])
        #価格の順番
        if keywords['order'] == '1':
            data = data.order_by('price')
        elif keywords['order'] == '2':
            data = data.order_by('-price')
        elif keywords['order'] == '3':
            data = data.order_by('tsubo_unit_price')
        elif keywords['order'] == '4':
            data = data.order_by('-tsubo_unit_price')
        elif keywords['order'] == '5':
            data = data.order_by('land_area')
        elif keywords['order'] == '6':
            data = data.order_by('-land_area')
        #ソート実行
        data = data.all()
        '''
        元コード

        jouken = {}
        data = self.session.query(self.land_info)

        #価格上限(入力フォームが空の場合、処理を飛ばす)
        if keywords['max_price'] !='':
            data = data.filter(self.land_info.c.price <= keywords['max_price'])
        #価格下限
        if keywords['min_price'] !='':
            data = data.filter(self.land_info.c.price >= keywords['min_price'])
        
        #面積上限
        if keywords['max_area'] !='':
            data = data.filter(self.land_info.c.land_area <= keywords['max_area'])
        #面積下限
        if keywords['min_area'] !='':
            data = data.filter(self.land_info.c.land_area >= keywords['min_area'])

        #タイトル検索
        if keywords['title'] != '':
            jouken['title'] = self.land_info.c.title.like('%\\' + keywords['title'] + '%', escape='\\')
        #所在地検索
        if keywords['location'] !='':
            jouken['location']= self.land_info.c.location.like('%\\' + keywords['location'] + '%', escape='\\')
        #交通検索
        if keywords['traffic'] !='':
            jouken['traffic']= self.land_info.c.traffic.like('%\\' + keywords['traffic'] + '%', escape='\\')

        #各検索ワードで絞込み
        for filter_land in jouken.values():
            data = data.filter(filter_land)

        #価格の順番
        if keywords['order'] == '1':
            data = data.order_by(self.land_info.c.price)
        elif keywords['order'] == '2':
            data = data.order_by(self.land_info.c.price.desc())
        elif keywords['order'] == '3':
            data = data.order_by(self.land_info.c.tsubo_unit_price.desc())
        elif keywords['order'] == '4':
            data = data.order_by(self.land_info.c.tsubo_unit_price)
        elif keywords['order'] == '5':
            data = data.order_by(self.land_info.c.land_area.desc())
        elif keywords['order'] == '6':
            data = data.order_by(self.land_info.c.land_area)
        
        #ソート実行
        data = data.all()
        '''
        
        return data


