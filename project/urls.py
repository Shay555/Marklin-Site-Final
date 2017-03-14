"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
from .settings import MEDIA_ROOT
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from marklin import views as  marklin_views
from accounts import views as accounts_views
from blog import urls as blog_urls
from marklin import views

urlpatterns = [
    url(r'^$', views.get_home, name='home'),
   url(r'^home/$', views.get_home, name='home'),
    url(r'^buy/$', views.get_Buy, name='buy'),
    url(r'', include(blog_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls),
    # url(r'^$', marklin_views.get_index, name='index'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^contact/$',views.get_Contact, name='contact'),
    url(r'^policy/$',views.get_Privacy, name='privacy'),
    url(r'', include('gallery.urls')),
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
    url(r'', include('products.urls'))
]
