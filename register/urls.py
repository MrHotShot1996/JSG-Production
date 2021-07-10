from django.urls import path

from . import views

urlpatterns = [
	path('', views.register, name='register'),
	path('success/', views.success, name='success'),
	path('terms/', views.terms, name='terms'),

	]