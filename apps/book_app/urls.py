from django.conf.urls import url
from . import views     



urlpatterns = [
    url(r'^dashboard$', views.dashboard), 
    url(r'^new$', views.new), 
    url(r'^create$', views.create), 
    url(r'^show_book/(?P<id>\d+)$', views.show_book),
    url(r'^show_user/(?P<id>\d+)$', views.show_user),  
    url(r'^add/(?P<id>\d+)$', views.add), 
  ]