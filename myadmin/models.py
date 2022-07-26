from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    
    class Meta:
      db_table = 'person'
      
class Boys(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    
    class Meta:
      db_table = 'boys'
      app_label = 'myadmin'      
      
