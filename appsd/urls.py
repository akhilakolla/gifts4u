from django.conf.urls import url
from appsd import views
urlpatterns = [url(r'^$', views.index, name = 'home'),]

