from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.views.generic.create_update import delete_object
import datetime

from post.models import *
from userprofile.models import *
from project.models import *
from post.forms import *

# Methods

def add_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			p.author_id = request.user.id;
			p.project_id = request.POST['project']
			p.save()
			p.assigned = form.cleaned_data['assigned']
			p.save()
			
			for u in form.cleaned_data['assigned']:
				try: u.email_user('River - '+p.title, p.content)
				except: pass
				Task(post=p, user=u, assigned_by=request.user).save()
			
			# Save files
			files = PostFileFormSet(request.POST, request.FILES, instance=p, prefix='files')
			files.save()
			
			# Save todo items
			todo = TodoFormSet(request.POST, instance=p, prefix='todos')
			todo.save()
			
			if p.todoitem_set.count() > 0: p.has_todos = True
			if p.postfile_set.count() > 0: p.has_files = True
			p.save()
			
			request.user.message_set.create(message="Posted Added!")
			
			# Notify the right people 
			for u in UserProfile.objects.filter(last_active__lt=(p.posted_date - timedelta(minutes=3))):
				u.notifications.add(p)
		else:
			raise Exception
			
# Views
		
@login_required
def main_stream(request):
	add_post(request)
	return render_to_response("stream/main.html", {
		'projects':Project.objects.all(),
		'users':User.objects.all(),
		'request':request,
	}, context_instance=RequestContext(request))

@login_required
def edit_post(request, id):
	if request.method == 'POST' and request.POST['content'] and request.POST['title']:
		p = Post.objects.get(id=id)
		if request.user == p.author:
			p.content = request.POST['content']
			p.title = request.POST['title']
			p.save()
			request.user.message_set.create(message="Posted Edited!")
	return redirect('/post/'+id)
	
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def delete_post(request, object_id):
    return delete_object(request, Post, '/', object_id=object_id, template_name='admin/delete_confirm.html')

@login_required
def post(request, id):
	post = Post.objects.get(id=id)

	if request.method == 'POST' and request.POST['comment']:
		Comment(comment=request.POST['comment'], post=post, author=request.user).save()
		post.save()

	return render_to_response("stream/post.html", {
		'post':post,
		'request':request,
	}, context_instance=RequestContext(request))
	
# Quick Actions

@login_required
def save_filter(request):
	if request.method == "POST":
		form = FilterForm(request.POST)
		if form.is_valid():
			f = form.save(commit=False);
			f.id = request.user.get_profile().get_filter().id
			f.save()
		else:
			raise Exception
	return redirect('/') if not request.GET.__contains__('next') else redirect(request.GET['next'])

@login_required
def complete_todo(request, id):
	t = TodoItem.objects.get(id=id)
	if not t.is_completed:
		t.is_completed = True
		t.completed_by = request.user
		t.completed_date = datetime.now()
	else:
		t.is_completed = False
	t.save()
	return redirect('/') if not request.GET.__contains__('next') else redirect(request.GET['next'])
	
@login_required
def pin(request, id):
	try:
		request.user.get_profile().board.add(id)
		request.user.message_set.create(message="Post Pined!")
	except: pass
	return redirect('/') if not request.GET.__contains__('next') else redirect(request.GET['next'])
	
@login_required
def unpin(request, id):
	request.user.get_profile().board.remove(id)
	request.user.message_set.create(message="Posted Unpined!")
	return redirect('/user/board') if not request.GET.__contains__('next') else redirect(request.GET['next'])
	
@login_required
def add_task(request, id):
	p = Post.objects.get(id=id)
	Task(post=p, user=request.user).save()
	request.user.message_set.create(message="Task Added!")
	return redirect('/') if not request.GET.__contains__('next') else redirect(request.GET['next'])
	
@login_required
def remove_task(request, id):
	Task.objects.get(post=Post.objects.get(id=id), user=request.user).delete()
	request.user.message_set.create(message="Task Removed!")
	return redirect('/') if not request.GET.__contains__('next') else redirect(request.GET['next'])
	
@login_required
def complete_task(request, id):
	t = Task.objects.get(id=id)
	if t.is_completed: 
		t.is_completed = False
		if t.assigned_by:
			t.post.is_completed = False
			t.post.save()
	else: 
		t.is_completed = True
		if t.assigned_by:
			t.post.is_completed = True
			t.post.save()
	t.save()
	request.user.message_set.create(message="Task Completed!")
	return redirect('user_tasks') if not request.GET.__contains__('next') else redirect(request.GET['next'])