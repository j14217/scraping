from django.db import models
from django.core import validators
# Create your models here.

#モデル部分(DBの定義)
class LandInfo(models.Model):
    title = models.CharField(max_length=200)  # title
    url = models.URLField(max_length=250)  # url
    traffic = models.CharField(max_length=200, null=True)  # 交通
    location = models.CharField(max_length=200)  # 所在地
    property_type = models.CharField(max_length=50, null=True)  # 物件種目
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 価格(単位：万円)
    most_popular_price_range = models.CharField(
        max_length=50, null=True)  # 最多価格帯
    tsubo_unit_price = models.DecimalField(max_digits=8, decimal_places=2,null=True)  # 坪単価
    lease_period_rent = models.CharField(
        max_length=50, null=True)  # 借地期間・地代（月額）
    right_money = models.CharField(max_length=50, null=True)  # 権利金
    security_deposit = models.CharField(max_length=50, null=True)  # 敷金/保証金
    maintenance_costs_etc = models.CharField(max_length=50, null=True)  # 維持費等
    other_expenses = models.CharField(max_length=50, null=True)  # その他費用
    facility = models.CharField(max_length=200, null=True)  # 設備
    parking = models.CharField(max_length=200, null=True)  # 駐車場
    notices = models.CharField(max_length=200, null=True)  # 特記事項
    remarks = models.CharField(max_length=300, null=True)  # 備考
    land_area = models.DecimalField(max_digits=10, decimal_places=2)  # 土地面積
    floor_space = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # 坪数
    sales_divisions = models.CharField(max_length=50, null=True)  # 販売区画数
    total_blocks = models.CharField(max_length=50, null=True)  # 総区画数
    units_sold_total_units = models.CharField(
        max_length=50, null=True)  # 販売戸数/総戸数
    optimal_use = models.CharField(max_length=200, null=True)  # 最適用途
    private_road_burden = models.CharField(max_length=50, null=True)  # 私道負担
    land_rights = models.CharField(max_length=50, null=True)  # 土地権利
    city_planning = models.CharField(max_length=50, null=True)  # 都市計画
    usage_area = models.CharField(max_length=50, null=True)  # 用途地域
    topography = models.CharField(max_length=50, null=True)  # 地勢
    building_coverage = models.CharField(max_length=50, null=True)  # 建蔽率
    floor_area_ratio = models.CharField(max_length=50, null=True)  # 容積率
    build_cov_area_ratio = models.CharField(
        max_length=50, null=True)  # 建蔽率/容積率
    contact_info = models.CharField(max_length=50, null=True)  # 接道状況
    geography = models.CharField(max_length=50, null=True)  # 地目
    land_law_notification = models.CharField(max_length=50, null=True)  # 国土法届出
    development_permission_number = models.CharField(
        max_length=50, null=True)  # 開発許可等番号
    setback = models.CharField(max_length=50, null=True)  # セットバック
    conditions_etc = models.CharField(max_length=200, null=True)  # 条件等
    current_status = models.CharField(max_length=50, null=True)  # 現況
    estab_completion_time = models.CharField(max_length=50, null=True)  # 造成完成時期
    delivery = models.CharField(max_length=50, null=True)  # 引渡し（時期/方法）
    scheduled_sales = models.CharField(max_length=200, null=True)  # 販売スケジュール
    property_no = models.DecimalField(max_digits=10, decimal_places=0, null=True)  # 物件番号
    contact_infomation = models.CharField(max_length=200, null=True)  # お問い合わせ先
    seller = models.CharField(max_length=200, null=True)  # 売主
    info_provider = models.CharField(max_length=200, null=True)  # 情報提供元
    info_release_date = models.DateField(null=True)  # 情報公開日
    info_update_date = models.DateField(null=True)  # 情報更新日
    next_info_update_date = models.CharField(max_length=200, null=True)  # 次回更新予定日
    event_info = models.CharField(max_length=200, null=True) #"イベント情報"
    other_restrictions = models.CharField(max_length=200, null=True) #"その他制限事項"
    company_profile = models.CharField(max_length=200, null=True) #"会社概要"
