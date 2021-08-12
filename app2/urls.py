from django.urls import path
from app2.views import *
app1_name='application2'
urlpatterns=[
    path('app2_fun/',app2_fun,name='app2_fun'),
]