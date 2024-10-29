from django.db import models
from django.utils import timezone
# Create your models here.

# Qualquer coisa que mudar no model, executar o comando: python manage.py makemigrations
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True) # pode ficar em branco
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now())
    description = models.TextField(blank=True)

    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

