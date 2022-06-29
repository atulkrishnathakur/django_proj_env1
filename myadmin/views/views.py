from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def home(request):
  template = loader.get_template('myadmin/home.html')
  return HttpResponse(template.render())
def about(request):
  template = loader.get_template('myadmin/about.html')
  return HttpResponse(template.render())    
def shop(request):
  template = loader.get_template('myadmin/shop.html')
  return HttpResponse(template.render())
def contact(request):
  template = loader.get_template('myadmin/contact.html')
  return HttpResponse(template.render())  
def shopSingle(request):
  template = loader.get_template('myadmin/shop-single.html')
  return HttpResponse(template.render())  
