from django.conf.urls import url
from django.urls import path, re_path
from .import views


app_name = 'articles' # namespaced URLs below for articles app

urlpatterns = [
    url(r'^$', views.article_list, name='list1'),       # Home page
    path('titles/', views.article_titles, name='titles'),
    re_path(r'^(?P<slug>[a-z0-9-]+)/$', views.article_details, name="details"),
    #re_path(r'^(?P<year>[0-9]{4})/$', views.article_year),



    #url(r'^(?P<year>[0-9]{4})/$', views.article_year, name="year"),
    #path('2020/', views.article_year, name="year"),
    #path('<int:year>/', views.article_year, name="articleyear"),
]




