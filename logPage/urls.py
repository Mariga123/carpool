from django.urls import path 
from django.conf.urls import url
from . import views

app_name = 'logPage'

urlpatterns = [
	path('' , views.index , name = "index"),
	path('register.html' , views.register , name = "register"),
	path('forgot-password.html' , views.forget , name = "forget"),
	path('option/' , views.drive_or_ride , name = "option"),
	path('registerUser/' , views.addUser , name = "registerUser"),
	path('verifyUser/' , views.verifyUser , name = "authenticate"),
]

