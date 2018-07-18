from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.template import loader
from django.urls import reverse

from search.pagination import paginate
from search.DBconnection import selectland
from search.LandInfotitle import landcolumns

from .forms import SearchForm
from .models import LandInfo

sland = selectland()
names = landcolumns()

def one(request, landinfo_id):
    data = sland.selectone(landinfo_id)
    name = names.landname
    return render(request, 'search/one.html',{'columns':data,'name':name})


def index(request):
    return render(request,'search/index.html',{'all':'./all/','search': './searchforms/'})


def all(request):
    data = sland.selectall()
    return render(request, 'search/all.html', {'columns':data})

def searchforms(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        data = sland.selectsearch(request.POST)
        searchpage = paginate(data,request)
        sdata = searchpage.page.object_list
        request.session.clear()
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
    else:
        form = SearchForm()
        return render(request, 'search/search.html', {
            'form': form
        })

def result(request):
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
    sdata = searchpage.page.object_list
    return render(request, 'search/result.html', {
        'columns': sdata,
    })