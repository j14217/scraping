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
    return render(request, 'search/detail.html',{'columns':data,'name':name})

#インデックス画面 http://127.0.0.1:8000/search/
def index(request):
    return render(request,'search/index.html',{'all':'./all/','search': './searchforms/'})

#全件表示画面 http://127.0.0.1:8000/search/all
def all(request):
    data = sland.selectall()
    return render(request, 'search/all.html', {'columns':data})

#検索画面 http://127.0.0.1:8000/search/searchforms/
def searchforms(request):
    #検索ボタン押下時の処理
    #2018/08/16陳追加--------------------------------------------
    if request.method == 'POST':
        form = SearchForm(request.POST)
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
            searchpage = paginate(data, request)
            #sdata = searchpage.page.object_list
            return render(request, 'search/search.html', {
            'form': form,
            'contacts': searchpage.contacts,
            #'columns': False,
            })
    else:
        #入力が無ければ、検索画面初期表示(検索フォームだけ表示)
        form = SearchForm()
        return render(request, 'search/search.html', {
            'form': form,
            #'columns': False,
        })
    #------------------------------------------------------------
    '''
    元コード
    if request.method == "POST":
        form = SearchForm(request.POST)
        data = sland.selectsearch(request.POST)
        searchpage = paginate(data,request)
        request.session.clear()
        #セッションに検索フォームのデータを格納
        
        f = [
                form.data['title'],
                form.data['location'],
                form.data['traffic'],
                form.data['order'],
                form.data['min_price'],
                form.data['max_price'],
                form.data['min_area'],
                form.data['max_area'],
            ]
        
        request.session['search_form'] = f
        return render(request, 'search/search.html', {
            'form': form,
            'contacts': searchpage.contacts
        })
    #検索画面初期表示(検索フォームだけ表示)
    else:
        form = SearchForm()
        return render(request, 'search/search.html', {
            'form': form
        })
    '''

#検索結果(jqueryで検索ページ内で読み込む)
def result(request):
    '''
    元コード
    #セッションデータを参照し検索
    f = request.session['search_form']
    form_data = ({
        'title': f[0],
        'location': f[1],
        'traffic': f[2],
        'order':f[3],
        'min_price': f[4],
        'max_price': f[5],
        'min_area': f[6],
        'max_area': f[7],
    })
    '''
    #2018/08/16陳追加--------------------------------------------
    form = SearchForm(request.POST)
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

    #------------------------------------------------------------
    data = sland.selectsearch(form_data)
    searchpage = paginate(data, request)
    #該当ページで表示するレコード10件
    sdata = searchpage.page.object_list
    return render(request, 'search/result.html', {
        'columns': sdata,
    })

def ajax_search(request):
    '''ajaxとの通信用関数'''
    if request.method == 'POST':
        #セッション型をなるべく使わないよう、セッションから辞書型に変換
        form_data = {
            'title': request.POST.get('title', None),
            'location': request.POST.get('location', None),
            'traffic': request.POST.get('traffic', None),
            'order': request.POST.get('order', None),
            'min_price': request.POST.get('min_price', None),
            'max_price': request.POST.get('max_price', None),
            'min_area': request.POST.get('min_area', None),
            'max_area': request.POST.get('max_area', None),
        }
        data = sland.selectsearch(form_data)
        #dataが無ければNo result,dataがあれば、行数に戻ります
        if data:
            data = {"count": data.count()}
            return JsonResponse(data)
        else:
            data = {"count": "No result"}
            return JsonResponse(data)
