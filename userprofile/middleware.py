from django.contrib.auth.models import *
from userprofile.models import UserProfile
from post.models import Filter

class UserProfileMiddleware(object):
	def process_request(self, request):
		if request.user.is_authenticated():
			try: request.user.get_profile().update_active()
			except: 
					UserProfile(user=request.user).save()
			try: user_filter = request.user.filters.all()[0]
			except: 
				Filter(owner=request.user).save()
			