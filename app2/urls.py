from django.urls import path
from app2.views import *

app_name='app2'

urlpatterns=[
    path('sample3/',sample3,name='sample3'),
    path('sample4/',sample4,name='sample4'),
]