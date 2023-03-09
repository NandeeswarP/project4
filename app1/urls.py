from django.urls import path
from app1.views import *

app_name='num'

urlpatterns = [
    path('sample/',sample,name='sample'),
    path('sam/',sam,name='sample1'),
    
]
