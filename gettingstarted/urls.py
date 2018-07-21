from django.conf.urls import include, url
from django.urls import path, re_path

from django.contrib import admin
admin.autodiscover()

import hello.views


urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^cars/(?P<pk>\d+)$', hello.views.car_detail, name='car_detail'),
    url(r'^cars/add', hello.views.car_add, name='car_add'),
    url(r'^cars/del', hello.views.cars_del, name='cars_del'),
    url(r'^cars.json', hello.views.cars_json, name='cars_json'),
    url(r'^cars', hello.views.car_list, name='car_list'),
    path('admin/', admin.site.urls),
]
