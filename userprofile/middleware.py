from django.contrib.auth.models import *
from userprofile.models import UserProfile

class UserProfileMiddleware(object):
	def process_request(self, request):
		if request.user.is_authenticated():
			try: request.user.get_profile().update_active()
			except: 
					UserProfile(user=request.user).save()
			