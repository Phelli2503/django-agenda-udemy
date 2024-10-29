from django.urls import path
from contact import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
]
