from django.urls import path

from . import views
#コントロール側(views.py)とURLを紐付け
app_name = 'search'
urlpatterns = [
    path('<int:landinfo_id>/detail/', views.detail, name='detail'),
    path('', views.index, name='index'),
    path('all/', views.all, name='all'),
    path('searchforms/', views.searchforms, name='searchforms'),
    path('result/', views.result, name='result')
]

