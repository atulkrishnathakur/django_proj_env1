from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from myadmin.add_country_form import CountryForm


def addCountry(request):

  if(request.method != 'POST'):

     form = CountryForm();
     return render(request,'add_country.html',{'form':form} )  
     
def saveCountry(request):
    context ={}
    form = CountryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
     form.save()
     context['form'] = form,
    
    return render(request,'add_country.html',context )
