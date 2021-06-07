from django.db import models
from django.utils import timezone
# Create your models here.


# Create your models here.
class Users(models.Model):
	first_name = models.CharField(max_length=20)
	last_name  = models.CharField(max_length=20)
	email      = models.TextField()
	phone      = models.CharField(max_length=10)
	join_date  = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.first_name + self.last_name