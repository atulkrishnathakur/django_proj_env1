from django.urls import path
from myadmin.views import views
from myadmin.views import list

urlpatterns = [
  path('home', views.home, name='home'),
  path('about', views.about, name='about'),
  path('shop', views.shop, name='shop'),
  path('contact', views.contact, name='contact'),
  path('shop-single', views.shopSingle, name='shopSingle'),
]
