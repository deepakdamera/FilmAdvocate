from django.db import models
from datetime import datetime
# Create your models here.
class Review(models.Model):
	review_title = models.CharField(max_length=60)
	review_content = models.TextField()
	review_published = models.DateTimeField("Date Published",default=datetime.now)
	review_genre = models.CharField(max_length=60,default="Drama")
	review_rating = models.PositiveSmallIntegerField(default=8)

	def __str__(self):
		return self.review_title