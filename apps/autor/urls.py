from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^function/$', autor_list, name='function_list'),
    url(r'^function/create/$', autor_create, name='function_create'),
    url(r'^function/update/(?P<pk>\d+)/', autor_update, name='function_update'),
    url(r'^function/delete/(?P<pk>\d+)/', autor_delete, name='function_delete'),

    url(r'^class/$', AutorList.as_view(), name='class_list'),
    url(r'^class/create/$', AutorCreate.as_view(), name='class_create'),
    url(r'^class/update/(?P<pk>\d+)/', AutorUpdate.as_view(), name='class_update'),
    url(r'^class/delete/(?P<pk>\d+)/', AutorDelete.as_view(), name='class_delete'),
]