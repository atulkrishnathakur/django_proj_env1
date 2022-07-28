from django.db import models
from myadmin.models import country

class State(models.Model):
    id = models.BigAutoField(primary_key=True, default=None)
    state_name = models.CharField(max_length=255)
    country_id = models.ForeignKey(country.Country,null=True,on_delete=models.SET_NULL,db_column='country_id')
    
    class Meta:
      db_table = 'state'
