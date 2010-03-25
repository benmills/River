from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import login as auth_login, authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from userprofile.models import *
from userprofile.forms import *

def register(request):
	if request.method == "POST" and request.POST['username'] and request.POST['password']:
		username = str(request.POST['username']).lower()
		if len(User.objects.filter(username=username)) == 0:
			u = User(username=username)
			u.set_password(request.POST['password'])
			u.save()
			UserProfile(user=u).save()
			auth_login(request, authenticate(username=username, password=request.POST['password']))
			return redirect('/')
			
	return render_to_response('user/register.html')
	
@login_required
def profile(request):
	if request.method == 'POST':
		form = UserForm(request.POST, instance=request.user)
		if form.is_valid():
			u = form.save()
			try: u.get_profile()
			except:
				UserProfile(user=u).save()
			return redirect('/')
	else:
		form = UserForm(instance=request.user)
		
	return render_to_response('user/profile.html', {
		'form':form
	}, context_instance=RequestContext(request))
	
@login_required
def board(request):
	return render_to_response('user/board.html', {
		'board':request.user.get_profile().board.all()
	}, context_instance=RequestContext(request))
