from django.db import models

class Country(models.Model):
    id = models.BigAutoField(primary_key=True, default=None)
    country_name = models.CharField(max_length=255)
    
    class Meta:
      db_table = 'country'

