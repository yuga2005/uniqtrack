from django.conf.urls import url
from django.contrib import admin
from pro import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^login/', views.logins),
    url(r'^logout/', views.logouts),
    url(r'^pro/', views.welcomes),
    url(r'^epi/', views.episodes),
    url(r'^asse/', views.assets),
    url(r'^getlogep/(?P<shot_details>\w+)/',views.getlogep),
    url(r'^getassetlog/(?P<shot_details>\w+)/',views.getassetlog),
    url(r'^updatewin/(?P<shot_details>\w+)/',views.updatewin),
    url(r'^updateassetwin/(?P<shot_details>\w+)/',views.updateassetwin),
    url(r'^update/(?P<shot_details>\w+)/',views.update),
    url(r'^updateasset/(?P<shot_details>\w+)/',views.updateasset),
    url(r'^add/', views.add),
    url(r'attendance/', views.attendance),
]