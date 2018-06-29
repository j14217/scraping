from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    # ex: /search/
    path('', views.index, name='index'),

    path('<int:landinfo_id>/', views.detail, name='detail'),

    #path('<int:landinfo_id>/one/', views.one, name='one'),
    path('<int:landinfo_id>/one/', views.one, name='one'),

    path('all/', views.all, name='all'),

#    path('<int:landinfo>/retrieval', views),
]

