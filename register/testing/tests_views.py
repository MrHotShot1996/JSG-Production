from django.test import TestCase, Client
from django.urls import reverse
from register.models import Users
# Create your tests here.
class TestViews(TestCase):
	
	# Setting up a custom test for the forms
	def setUp(self):
		Users.objects.create(first_name = "hasan",
		last_name="alboug",
		phone="0562020196",
		email="h@yahoo.com")
	
	# Testing Get Requests
	def test_register_GET(self):
		response = self.client.get(reverse('register'))

		# Tests if the view gives a 200
		self.assertEquals(response.status_code, 200)
		# Tests if the template works
		self.assertTemplateUsed(response, 'register/register.html')
		# Tests content in the templates if it matches
		self.assertContains(response, 'First Name')

	# def test_success_GET(self):
	# 	response = self.client.get(reverse('success'))

	# 	self.assertEquals(response.status_code, 200)
	# 	self.assertTemplateUsed(response, 'register/success.html')

	# Testing the Form
	
	def test_register_details(self):
		name = Users.objects.get(first_name='hasan')
		print(name)
