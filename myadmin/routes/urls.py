from django.urls import path
from myadmin.views import views
from myadmin.views import country

urlpatterns = [
  path('home', views.home, name='home'),
  path('about', views.about, name='about'),
  path('shop', views.shop, name='shop'),
  path('contact', views.contact, name='contact'),
  path('shop-single', views.shopSingle, name='shopSingle'),
  path('add-country', country.addCountry, name='addCountry'),
  path('save-country', country.saveCountry, name='saveCountry'),
  path('country-list', country.countryList, name='countryList'),
  path('edit-country/<int:id>', country.editCountry, name='editCountry'),
]
