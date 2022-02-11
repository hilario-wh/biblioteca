from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^function/$', editor_list, name='function_list'),
    url(r'^function/create/$', editor_create, name='function_create'),
    url(r'^function/update/(?P<pk>\d+)/$', editor_update, name='function_update'),
    url(r'^function/delete/(?P<pk>\d+)/$', editor_delete, name='function_delete'),

    url(r'^class/$', EditorList.as_view(), name='class_list'),
    url(r'^class/create/$', EditorCreate.as_view(), name='class_create'),
    url(r'^class/update/(?P<pk>\d+)/$', EditorUpdate.as_view(), name='class_update'),
    url(r'^class/delete/(?P<pk>\d+)/$', EditorDelete.as_view(), name='class_delete'),
]