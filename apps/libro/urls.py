from django.conf.urls import url

from apps.libro.views import *


urlpatterns = [
    url(r'^$', index, name='function_index'),

    #FUNCIONES
    url(r'^libro/function/$', libro_list, name='function_list'),
    url(r'^libro/function/create/$', libro_create, name='function_create'),
    url(r'^libro/function/update/(?P<pk>\d+)/$', libro_update, name='function_update'),
    url(r'^libro/function/delete/(?P<pk>\d+)/$', libro_delete, name='function_delete'),

    #CLASES
    url(r'^libro/class/$', LibroList.as_view(), name='class_list'),
    url(r'^libro/class/create/$', LibroCreate.as_view(), name='class_create'),
    url(r'^libro/class/update/(?P<pk>\d+)/$', LibroUpdate.as_view(), name='class_update'),
    url(r'^libro/class/delete/(?P<pk>\d+)/$', LibroDelete.as_view(), name='class_delete'),
]