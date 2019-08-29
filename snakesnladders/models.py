from django.db import models
from django.contrib.postgres.fields import JSONField 
from django.contrib.auth.models import User 

# Create your models here.
class savedGames(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE) 
	date_saved = models.DateTimeField()
	position = models.IntegerField()
	greenDict = JSONField()
	redDict = JSONField()

	def _str_(self):
		return self.user 