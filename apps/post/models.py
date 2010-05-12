from django.db import models
from django.contrib.auth.models import User
from project.models import Project

import datetime

class Post(models.Model):
	posted_date = models.DateTimeField(default=datetime.datetime.now)
	updated = models.DateTimeField(auto_now=True)
	content = models.TextField()
	title = models.TextField()
	author = models.ForeignKey(User, related_name="posts")
	assigned = models.ManyToManyField(User, related_name="assigned_tasks", null=True)
	
	is_completed = models.BooleanField(default=False)
	completed_by = models.ForeignKey(User, related_name="completed_posts", null=True)
	
	project = models.ForeignKey(Project, null=True)
	
	has_files = models.BooleanField(default=False)
	has_todos = models.BooleanField(default=False)
	
	def comment_count(self):
		count = self.comment_set.count()
		if count == 0: return "No Comments"
		if count == 1: return "%s Comment" % count
		else:  return "%s Comments" % count
		
	def last_comment(self):
		comments = self.comment_set.all()
		if len(comments) > 0:
			return self.comment_set.latest('posted_date')
		else: return None
	
	def __unicode__(self):
		return self.content
	
	class Meta:
		ordering = ['-updated']
		
class Comment(models.Model):
	posted_date = models.DateTimeField(default=datetime.datetime.now)
	post = models.ForeignKey(Post)
	comment = models.TextField()
	author = models.ForeignKey(User)
	
	class Meta:
		ordering = ['-posted_date']
	
class TodoItem(models.Model):
	posted_date = models.DateTimeField(default=datetime.datetime.now)
	post = models.ForeignKey(Post)
	content = models.TextField()
	is_completed = models.BooleanField()
	completed_by = models.ForeignKey(User, null=True)
	completed_date = models.DateTimeField(default=datetime.datetime.now)
	
	def __unicode__(self):
		return self.content
	
	class Meta:
		ordering = ['-posted_date']
	
class PostFile(models.Model):
	posted_date = models.DateTimeField(default=datetime.datetime.now)
	post = models.ForeignKey(Post)
	file = models.FileField(upload_to='post-files/%Y/%m/%d')
	
	def get_name(self):
		name = str(self.file).split('/')
		name.reverse()
		return name[0]
	
	class Meta:
		ordering = ['-posted_date']
		
class Filter(models.Model):
	owner = models.ForeignKey(User, related_name="filters")
	author_id = models.IntegerField(default=0)
	assigned_id = models.IntegerField(default=0)
	project_id= models.IntegerField(default=0)
	type = models.IntegerField(default=0)
	