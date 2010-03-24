from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField()
	team = models.ManyToManyField(User)
