from django.conf.urls.defaults import *
import settings

urlpatterns = patterns('',
	(r'^', include('post.urls')),
	(r'^user/', include('userprofile.urls')),
	(r'^project/', include('project.urls')),
)

if settings.LOCAL_DEVELOPMENT:
	urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)
