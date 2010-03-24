from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^(?P<project_id>[0-9]+)/$', 'project.views.project_stream', name="project"),
	url(r'^create/$', 'project.views.create_project', name="create_project"),
)
