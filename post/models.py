from django.db import models
from django.contrib.auth.models import User
from project.models import Project

import datetime

class Post(models.Model):
	posted_date = models.DateTimeField(default=datetime.datetime.now)
	updated = models.DateTimeField(auto_now=True)
	content = models.TextField()
	author = models.ForeignKey(User, related_name="posts")
	assigned = models.ManyToManyField(User, related_name="assigned_tasks")
	project = models.ForeignKey(Project, null=True)
	
	def comment_count(self):
		count = self.comment_set.count()
		if count == 0: return "No Comments"
		if count == 1: return "%s Comment" % count
		else:  return "%s Comments" % count
		
	def last_comment(self):
		comments = self.comment_set.all()
		if len(comments) > 0:
			return comments[0]
		else: return None
		
	def get_title(self):
		lines = self.content.split('\n')
		for l in lines:
			words = l.split(' ')
			if len(words) >= 2:
				if words[0] == 'h1.':
					return words[1]
				return words[0]+" "+words[1]
		return self.content
	
	def __unicode__(self):
		return self.content
	
	class Meta:
		ordering = ['-updated']
		
class Comment(models.Model):
	posted_date = models.DateTimeField(default=datetime.datetime.now)
	post = models.ForeignKey(Post)
	comment = models.TextField()
	author = models.ForeignKey(User)
	
class TodoItem(models.Model):
	posted_date = models.DateTimeField(default=datetime.datetime.now)
	post = models.ForeignKey(Post)
	content = models.TextField()
	is_completed = models.BooleanField()
	completed_by = models.ForeignKey(User)
	completed_date = models.DateField(default=datetime.datetime.now)
	
	def __unicode__(self):
		return self.content
	
	class Meta:
		ordering = ['-posted_date']
	
class PostFile(models.Model):
	posted_date = models.DateTimeField(default=datetime.datetime.now)
	post = models.ForeignKey(Post)
	file = models.FileField(upload_to='post-files/%Y/%m/%d')
	
	def __unicode__(self):
		return self.file
	
	class Meta:
		ordering = ['-posted_date']