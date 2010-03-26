from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
	url('^login/$', login, {'template_name': 'user/login.html'}, name='log_in'),
	url('^logout/$', logout, {'next_page': '/'}, name='log_out'),
	url('^register/$', 'userprofile.views.register', name='register'),
	url('^profile/$', 'userprofile.views.profile', name='user_profile'),
	url('^board/$', 'userprofile.views.board', name='user_board'),
	url('^admin/$', 'userprofile.views.user_admin', name='user_admin'),
	url(r'^admin/(?P<id>[0-9]+)/$', 'userprofile.views.user_admin_edit', name='user_admin_edit'),
)
