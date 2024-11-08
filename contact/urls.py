from django.urls import path
from contact import views

app_name = 'contact' # Adicionar o nome do app

urlpatterns = [
    path('', views.index, name='index'), # adicionar a view na url
    path('search/', views.search, name='search'),
    
    # Contact (CRUD)
    path('contato/<int:contact_id>/detalhes/', views.contact, name='contact'),
    path('contato/<int:contact_id>/atualizar/', views.update, name='update'),
    path('contato/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contato/create/', views.create, name='create'),
    
    # USER 
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user_update'),
]
