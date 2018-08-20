from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
#2018/08/15
from django.shortcuts import get_object_or_404, render,redirect
from django.template import loader
from django.urls import reverse

from search.pagination import paginate
from search.DBconnection import selectland
from search.LandInfotitle import landcolumns
from django.core.paginator import Paginator

from .forms import SearchForm
from .models import LandInfo

#コントロール部分、view側(template)へ検索結果などデータを渡す

sland = selectland()
names = landcolumns()

#詳細画面 http://127.0.0.1:8000/search/(レコードのid)/detail
def detail(request, landinfo_id):
    data = sland.selectone(landinfo_id)
    name = names.landname
    return render(request, 'search/detail.html', {'columns':data,'name':name})

#インデックス画面 http://127.0.0.1:8000/search/
def index(request):
    return render(request, 'search/index.html', {'all':'./all/', 'search': './searchforms/'})

#全件表示画面 http://127.0.0.1:8000/search/all
def all(request):
    data = sland.selectall()
    return render(request, 'search/all.html', {'columns':data})

#検索画面 http://127.0.0.1:8000/search/searchforms/
def searchforms(request):
    #検索ボタン押下時の処理
    #2018/08/16陳追加--------------------------------------------
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            #セッション型を使わずに、辞書型そのまま使用します
            form_data = {
                'title': form.cleaned_data.get('title'),
                'location': form.cleaned_data.get('location'),
                'traffic': form.cleaned_data.get('traffic'),
                'order': form.cleaned_data.get('order'),
                'min_price': form.cleaned_data.get('min_price'),
                'max_price': form.cleaned_data.get('max_price'),
                'min_area': form.cleaned_data.get('min_area'),
                'max_area': form.cleaned_data.get('max_area'),
            }
            data = sland.selectsearch(form_data)
            #searchpage = paginate(data, request)
            searchpage = Paginator(data, 10)
            page = request.GET.get('page')
            contacts = searchpage.get_page(page)

            #sdata = searchpage.page.object_list
            return render(request, 'search/search.html', {'form': form, 'contacts': contacts})
        else:
        #入力が無ければ、検索画面初期表示(検索フォームだけ表示)
            form = SearchForm()
            return render(request, 'search/search.html', {'form': form})
    #------------------------------------------------------------