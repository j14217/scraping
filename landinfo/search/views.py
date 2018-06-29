from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
#from search.models import LandInfo
from scraping_source.land_info_scraping import land_info_scraping
from sqlalchemy import create_engine
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.sql import select

# Create your views here.
def index(request):
#    latest_landinfo_list = LandInfo[:5]
#    template = loader.get_template('search/index.html')
#   context = {
#        'latest_landinfo_list': latest_landinfo_list,
#    }
    return HttpResponse('ok')
#    return HttpResponse(template.render(context, request))


def detail(request, landinfo_id):
    try:
        landinfo = LandInfo.objects.get(pk=landinfo_id)
    except LandInfo.DoesNotExist:
        raise Http404("土地が見つかりません")
    return render(request, 'search/detail.html', {'landinfo': landinfo})


def one(request, landinfo_id):
#    land_info_scraping()
    url = 'postgresql://postgres:scrapingland@192.168.0.109:5432/postgres'
    engine = create_engine(url)
    conn = engine.connect()
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
    s = select([land_info], land_info.c.id == landinfo_id)
    result = conn.execute(s) 
    data = result.fetchone()
#    return HttpResponse(result)
    return render(request, 'search/one.html',{'app':'ひとつだけ','columns':data})
#    landinfo = get_object_or_404(LandInfo, pk=landinfo_id)
#    return render(request, 'search/results.html', {'landinfo': landinfo})

def all(request):
#    land_info_scraping()
    url = 'postgresql://postgres:scrapingland@192.168.0.109:5432/postgres'
    engine = create_engine(url)
    conn = engine.connect()
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
    s = select([land_info])
    result = conn.execute(s) 
    return HttpResponse(result)

def retrieval(request, landinfo_id):
    landinfo = get_object_or_404(LandInfo, pk=landinfo_id)
    try:
        selected_landinfo = landinfo.landinfo_set.get(pk=request.POST['landinfo'])
    except (KeyError, LandInfo.DoesNotExist):
        return render(request, 'search/detail.html', {
            'landinfo': landinfo,
            'error_message': "You didn't select a choice",
        })
    else:
        return HttpResponseRedirect(reverse('search:results', args=(landinfo.id,)))
