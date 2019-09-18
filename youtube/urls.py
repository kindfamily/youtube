from django.urls import path
from .views import *

app_name = 'youtube'

urlpatterns = [
    
    path('', cattube, name='cattue'),    

]
