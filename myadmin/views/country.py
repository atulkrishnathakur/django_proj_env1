from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from myadmin.add_country_form import CountryForm
from myadmin.add_country_form import CountryEditForm
from myadmin.models.country import Country


def addCountry(request):
  if(request.method != 'POST'):
     form = CountryForm()
     return render(request, 'add_country.html', {'form': form})
def saveCountry(request):
    context ={}
    form = CountryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
     form.save()
     context['form'] = form,
    
    ##return render(request,'add_country.html',context )
     return redirect('countryList')  
    else:
     return redirect('addCountry')
    
def countryList(request):
  if(request.method != 'POST'):
    template = loader.get_template('country_list.html')
    all_countries = Country.objects.all()
    context = {
    'all_countries': all_countries,
    }
    
    return HttpResponse(template.render(context, request))

def editCountry(request, id):
   if(request.method != 'POST'):
    form = CountryEditForm()
    template = loader.get_template('edit_country.html')
    countryObj = Country.objects.get(id=id)
    context = {
    'countryObj': countryObj,
    'form': form
    }
   return HttpResponse(template.render(context, request))
  

