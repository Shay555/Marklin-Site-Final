from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products/$', views.all_products),
    url(r'^products/new/$', views.new_listing, name='new_listing')
]