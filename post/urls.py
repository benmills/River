from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'post.views.main_stream', name="main_stream"),
	url(r'^post/edit/(?P<id>[0-9]+)/$', 'post.views.edit_post', name="edit_post"),
	url(r'^post/(?P<id>[0-9]+)/$', 'post.views.post', name="post"),
	url(r'^pin/(?P<id>[0-9]+)/$', 'post.views.pin', name="pin"),
	url(r'^unpin/(?P<id>[0-9]+)/$', 'post.views.unpin', name="unpin"),
)
