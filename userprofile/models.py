from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	
	def get_name(self):
		if self.user.first_name and self.user.last_name:
			return self.user.get_full_name()
		else:
			return self.user.username
