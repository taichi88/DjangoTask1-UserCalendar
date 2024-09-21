from django.db import models
from django.http import HttpResponse
from datetime import date

today = date.today()

# Create your models here.


class Person(models.Model):
    
    name = models.CharField(max_length=100)
    
    number = models.IntegerField()
    birthdate = models.DateField()


   
    

    
    def __str__(self):

        date_calculated = today.year - self.birthdate.year 
        
        return f'{self.name} was born in {self.birthdate}. Since {self.birthdate} it has past {date_calculated} years'

        
        
        
  
        
   
    