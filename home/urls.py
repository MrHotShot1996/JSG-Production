from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('about/', views.about, name='about'),
	]
	
'''
path('test/<int:id>', views.test, name='test'),
path('test/<str:test_var>', views.testvar, name='testvar'),
path('test/errors', views.errortesting, name='errortesting'),
'''