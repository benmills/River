from django.db import models
from django.contrib.auth.models import User

from post.models import Post

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	board = models.ManyToManyField(Post, related_name="pined_by")
	
	def get_name(self):
		if self.user.first_name and self.user.last_name:
			return self.user.get_full_name()
		else:
			return self.user.username
