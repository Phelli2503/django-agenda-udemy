from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'last_name', 'phone', # titles
    ordering = '-id', # Order
    list_filter = 'created_date', # Filtrar
    search_fields = 'id','first_name','last_name', # Pesquisar
    list_per_page = 150 #paginação
    list_max_show_all = 100 # limite do mostrar tudo
    list_editable = 'phone', # editar sem abrir
    list_display_links = 'first_name', # links 
    
@admin.register(models.Category)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',

