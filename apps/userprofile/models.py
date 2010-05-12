from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

from post.models import Post

class UserProfile(models.Model):
	user = models.ForeignKey(User)
	board = models.ManyToManyField(Post, related_name="pined_by")
	tasks = models.ManyToManyField(Post, related_name="tasked_by")
	last_active = models.DateTimeField(null=True)
	notifications = models.ManyToManyField(Post, related_name="notification_set")
	
	def get_name(self):
		if self.user.first_name and self.user.last_name:
			return self.user.get_full_name()
		else:
			return self.user.username
			
	def get_notifications(self):
		notifications = list(self.notifications.all())
		self.notifications.clear()
		return notifications
			
	def update_active(self):
		self.last_active = datetime.now()
		self.save()
		
	def get_filter(self):
		return self.user.filters.all()[0]

class Task(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	is_completed = models.BooleanField(default=False)
	assigned_by = models.ForeignKey(User, related_name="assigned_to_tasks", null=True)
