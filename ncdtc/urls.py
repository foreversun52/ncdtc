import xadmin
xadmin.autodiscover()
# xversion模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

from django.contrib import admin
from django.urls import path, re_path
from main import views

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('bottom/', views.bottom, name='bottom'),
    path('logo/', views.logo, name='logo'),
    path('menu/', views.menu, name='menu'),
    path('browse/', views.browse, name='browse'),
    re_path('browse_result/(\w+)/', views.browse_result, name='browse_result'),
    re_path('browse_result_details/(\d+)', views.browse_result_details, name='browse_result_details'),
    path('download/', views.download, name='download'),
    path('help/', views.help, name='help'),
    path('search/', views.search, name='search'),
    path('search_by_ncrna/', views.search_by_ncrna, name='search_by_ncrna'),
    path('search_by_drug/', views.search_by_drug, name='search_by_drug'),
    path('search_by_cancer/', views.search_by_cancer, name='search_by_cancer'),
    re_path('search_result/(\w+)/', views.search_result, name='search_result'),
    re_path('search_result_details/(\d+)/', views.search_result_details, name='search_result_details'),
    path('submit/', views.submit, name='submit'),
]
