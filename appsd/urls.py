from django.conf.urls import url
from django.contrib import admin
from appsd import views
urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^hp$',views.homes, name = 'homes'),
    url(r'^hhp/([0-9])$',views.hyperl, name = 'hyperl'),
    url(r'^odiwali/([0-9])$', views.odiwali, name = "odiwali"),
    url(r'^occ/([A-Z])$', views.occs, name = "occs"),
]
