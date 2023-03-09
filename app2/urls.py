from django.urls import path
from app2.views import *

app_name='n'

urlpatterns = [
    path('a/',a,name='a'),
    path('hi/',b),
    path('myname/',h),
]