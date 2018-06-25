from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("土地情報検索サイトです")

def detail(request, landinfo_id):
    return HttpResponse("土地情報 %s." % landinfo_id)