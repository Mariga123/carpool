from django.urls import path 
from django.conf.urls import url
from . import views

app_name = 'rider'

urlpatterns = [
	path('' , views.index , name = "ride"),
	path('submit', views.rideInfo, name = "rideInfo"),
	path('processsing', views.statusUpdate, name = "statusUpdate"),
	path('success', views.rideSuccessful, name = "rideSuccessful"),
]

