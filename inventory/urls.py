from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'inventory'

urlpatterns = [
    path('list/items/', views.itemList, name='items_list'),
    path('list/drugs/', views.drugList, name='drugs_list'),
    path('item/', views.ItemPage, name='addItem'),
    path('drug/', views.DrugPage, name='addDrug'),
    url(r'^delete/(?P<id>[\w.@+-]+)/$', views.delete_item, name='deleteItem'),
    url(r'^delete_drug/(?P<id>[\w.@+-]+)/$', views.delete_drug, name='deleteDrug'),
    url(r'^edit/(?P<id>[\w.@+-]+)/$', views.edit_item, name='editItem'),
    url(r'^edit_drug/(?P<id>[\w.@+-]+)/$', views.edit_drug, name='editDrug'),

]
