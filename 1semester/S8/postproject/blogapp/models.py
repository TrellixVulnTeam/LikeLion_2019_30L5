from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	body = models.TextField()
	
	def __str__(self):
		return self.title
# Create your models here.
