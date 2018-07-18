from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    path('<int:landinfo_id>/one/', views.one, name='one'),
    path('', views.index, name='index'),
    path('all/', views.all, name='all'),
    path('searchforms/', views.searchforms, name='searchforms'),
    path('result/', views.result, name='result')
]

