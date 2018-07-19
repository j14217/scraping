from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.template import loader
from django.urls import reverse

from search.pagination import paginate
from search.DBconnection import selectland
from search.LandInfotitle import landcolumns

from .forms import SearchForm
from .models import LandInfo

#コントロール部分、view側(template)へ検索結果などデータを渡す

sland = selectland()
names = landcolumns()

#詳細画面 http://127.0.0.1:8000/search/(レコードのid)/detail
def detail(request, landinfo_id):
    data = sland.selectone(landinfo_id)
    name = names.landname
    return render(request, 'search/one.html',{'columns':data,'name':name})

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
    if request.method == "POST":
        form = SearchForm(request.POST)
        data = sland.selectsearch(request.POST)
        searchpage = paginate(data,request)
        sdata = searchpage.page.object_list
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
            'columns': sdata, 
            'contacts': searchpage.contacts
        })
    #検索画面初期表示(検索フォームだけ表示)
    else:
        form = SearchForm()
        return render(request, 'search/search.html', {
            'form': form
        })

#検索結果(jqueryで検索ページ内で読み込む)
def result(request):
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
    data = sland.selectsearch(form_data)
    searchpage = paginate(data,request)
    #該当ページで表示するレコード10件
    sdata = searchpage.page.object_list
    return render(request, 'search/result.html', {
        'columns': sdata,
    })