from django.conf.urls import url
from . import views
from django.contrib import admin

app_name = 'gem'
urlpatterns = [
    #example: /gem
    url(r'^$', views.IndexView.as_view(), name='index'),

    #example: /gem/5
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]