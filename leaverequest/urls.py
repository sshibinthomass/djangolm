from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('submit',views.leaverequest,name='leaverequest'),
    path('alldetails',views.alldetails,name='alldetails'),

]
