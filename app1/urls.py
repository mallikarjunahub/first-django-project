from django.urls import path
from app1.views import *
app1_name='application1'
urlpatterns=[
    path('app1_fun/',app1_fun,name='app1_fun'),
]