from django.conf.urls.defaults import *

from post.models import Post
from post.views import delete_post

urlpatterns = patterns('',
	url(r'^$', 'post.views.main_stream', name="main_stream"),
		
	url(r'^post/(?P<id>[0-9]+)/$', 'post.views.post', name="post"),
		url(r'^post/edit/(?P<id>[0-9]+)/$', 'post.views.edit_post', name="edit_post"),
		url(r'^post/delete/(?P<object_id>[0-9]+)/$', delete_post, name='delete_post'),
	
	url(r'^pin/(?P<id>[0-9]+)/$', 'post.views.pin', name="pin"),
	url(r'^unpin/(?P<id>[0-9]+)/$', 'post.views.unpin', name="unpin"),
	
	url(r'^task/add/(?P<id>[0-9]+)/$', 'post.views.add_task', name="add_task"),
	url(r'^task/remove/(?P<id>[0-9]+)/$', 'post.views.remove_task', name="remove_task"),
	url(r'^task/complete/(?P<id>[0-9]+)/$', 'post.views.complete_task', name="complete_task"),
	
	url(r'^todo/complete/(?P<id>[0-9]+)/$', 'post.views.complete_todo', name="complete_todo"),
	
	url(r'^filter/save/$', 'post.views.save_filter', name="save_filter"),
)
