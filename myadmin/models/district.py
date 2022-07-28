from django.db import models
from myadmin.models import country
from myadmin.models import state

class District(models.Model):
    id = models.BigAutoField(primary_key=True, default=None)
    district_name = models.CharField(max_length=255)
    country_id = models.ForeignKey(country.Country,on_delete=models.SET_NULL,null=True,db_column='country_id')
    state_id = models.ForeignKey(state.State,on_delete=models.SET_NULL,null=True,db_column='state_id')
    
    class Meta:
      db_table = 'district'
