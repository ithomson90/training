from django.urls import path
from AppOne import views

#TEMPLATE URLS
app_name = 'AppOne'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
