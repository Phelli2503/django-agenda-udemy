from django.urls import path
from contact import views

app_name = 'contacts' # Adicionar o nome do app

urlpatterns = [
    path('', views.index, name='index'), # adicionar a view na url
]
