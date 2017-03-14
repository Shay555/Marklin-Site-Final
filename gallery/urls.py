from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^gallery/$', views.image_list),
    url(r'^gallery/new/$', views.new_image, name='new_image'),
]