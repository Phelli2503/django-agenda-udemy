from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
    

# Qualquer coisa que mudar no model, executar o comando: python manage.py makemigrations
class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="NOME")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="SOBRENOME") # pode ficar em branco
    phone = models.CharField(max_length=50, verbose_name="TELEFONE")
    email = models.EmailField(max_length=254 , verbose_name="E-MAIL")
    created_date = models.DateTimeField(default=timezone.now())
    description = models.TextField(blank=True, verbose_name="DESCRIÇÃO")
    
    show = models.BooleanField(default=True) # Se precisa mostrar
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,)

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

