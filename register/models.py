from django.db import models
from django.utils import timezone

# Quote variables for the success page
sentence1 = "You say you’re ‘depressed’ – all I see is resilience.\
You are allowed to feel messed up and inside out. \
It doesn’t mean you’re defective – it just means you’re human."
author1 = "David Mitchell"

sentence2 = "I found that with depression, \
one of the most important things you can \
realize is that you’re not alone. You’re not \
the first to go through it, \
you’re not gonna be the last to go through it."
author2 = "Dwayne “The Rock” Johnson"

sentence3 = "Self-care is never a selfish act—it is \
simply good stewardship of the only gift I have, \
the gift I was put on earth to offer to others."
author3 = "Parker Palmer"

quotes = {
	'quote1':[sentence1,author1],
	'quote2':[sentence2,author2],
	'quote3':[sentence3,author3]
	
}

# Create your models here.
class Users(models.Model):
	first_name = models.CharField(max_length=20)
	last_name  = models.CharField(max_length=20)
	email      = models.TextField()
	phone      = models.CharField(max_length=10)
	join_date  = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.first_name + self.last_name