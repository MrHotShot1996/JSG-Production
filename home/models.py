from django.db import models
from django.utils import timezone

class SiteVisits(models.Model):
	page_visits = models.IntegerField(default=0)


	def view_count(self):
		self.page_visits += 1 
		self.save()

	def __str__(self):
		return "Page Visit"

