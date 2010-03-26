from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.views.generic.create_update import *

from post.models import *
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
			
# Views
		
@login_required
def main_stream(request):
	add_post(request)
	
	return render_to_response("stream/main.html", {
		'projects':Project.objects.all(),
	}, context_instance=RequestContext(request))

@login_required
def edit_post(request, id):
	if request.method == 'POST' and request.POST['content']:
		p = Post.objects.get(id=id)
		p.content = request.POST['content']
		p.save()
	return redirect('/post/'+id)
	
@user_passes_test(lambda u: u.is_superuser, login_url='/')
def delete_post(request, object_id):
    return delete_object(request, Post, '/', object_id=object_id, template_name='admin/delete_confirm.html')
	
@login_required
def pin(request, id):
	try:
		request.user.get_profile().board.add(id)
	except: pass
	return redirect('/')
	
@login_required
def unpin(request, id):
	#Post.objects.get(id=id)
	request.user.get_profile().board.remove(id)
	return redirect('/user/board')	

@login_required
def post(request, id):
	post = Post.objects.get(id=id)
	
	if request.method == 'POST' and request.POST['comment']:
		Comment(comment=request.POST['comment'], post=post, author=request.user).save()
		post.save()
		
	return render_to_response("stream/post.html", {
		'post':post
	}, context_instance=RequestContext(request))
