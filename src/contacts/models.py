from django.db import models
from src.users.models import User

class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    contact_image = models.URLField(null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    country_code = models.IntegerField(max_length=10)
    phone_number = models.IntegerField(max_length=30)
    is_favorite = models.BooleanField(default=True)
        
    
    def __str__(self):
        return self.first_name
        