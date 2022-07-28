from django.db import models

class Person(models.Model):
    p_id = models.BigAutoField(primary_key=True, default=None)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    class Meta:
      db_table = 'person'

