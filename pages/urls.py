from django.urls import path,include 
from . import views 

app_name = 'pages'

urlpatterns = [
    path('', views.Home, name='home'),
]
