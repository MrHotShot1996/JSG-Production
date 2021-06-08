from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from register.views import register, success
# Create your tests here.

class TestUrls(SimpleTestCase):

	def test_register_is_resolved(self):
		url = reverse('register')
		print(resolve(url))
		# Makes sure the function matches
		self.assertEquals(resolve(url).func, register) 

	def test_success_is_resolved(self):
		url = reverse('success')
		print(resolve(url))
		# Makes sure the function matches
		self.assertEquals(resolve(url).func, success) 

