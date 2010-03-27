from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
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
			u.get_profile()
			u.message_set.create(message="Profile Updated!")
			return redirect('/')
	else:
		form = UserForm(instance=request.user)
		
	return render_to_response('user/profile.html', {
		'form':form
	}, context_instance=RequestContext(request))
	
@login_required
def board(request):
	return render_to_response('user/board.html', {
		'board':request.user.get_profile().board.all(),
		'request':request,
	}, context_instance=RequestContext(request))
	
@login_required
def tasks(request):
	return render_to_response('user/tasks.html', {
		'tasks':request.user.task_set.all(),
		'request':request,
	}, context_instance=RequestContext(request))
	
# @login_required
# def clear_notifications(request):
# 	request.user.get_profile()

@user_passes_test(lambda u: u.is_superuser, login_url='/')	
def user_admin(request):
	return render_to_response('admin/users.html', {
		'users':User.objects.all()
	}, context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser, login_url='/')
def user_admin_edit(request, id):
	user = User.objects.get(id=id)
	if request.method == "POST":
		form = UserFormAdmin(request.POST, instance=user)
		if form.is_valid():
			form.save()
	else:
		form = UserFormAdmin(instance=user)
		
	return render_to_response('admin/user.html', {
		'edit_user': user,
		'form':form,
	}, context_instance=RequestContext(request))
