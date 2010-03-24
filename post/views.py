from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from itertools import chain

from post.models import *
from project.models import *
from post.forms import *

@login_required
def main_stream(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			p.author_id = request.user.id;
			p.project_id = request.POST['project'];
			p.save()
	
	stream = list(chain(
		Post.objects.all(), Comment.objects.all(),
	))
	
	stream = sorted(
		list(chain(Post.objects.all(), Comment.objects.all())),
		key=lambda x: x.posted_date
	)
	stream.reverse();
	
	return render_to_response("stream/main.html", {
		'stream': stream,
		'projects':Project.objects.all(),
	}, context_instance=RequestContext(request))

@login_required
def edit_post(request, id):
	if request.method == 'POST' and request.POST['content']:
		p = Post.objects.get(id=id)
		p.content = request.POST['content']
		p.save()
	return redirect('/post/'+id)

@login_required
def post(request, id):
	post = Post.objects.get(id=id)
	
	if request.method == 'POST' and request.POST['comment']:
		Comment(comment=request.POST['comment'], post=post, author=request.user).save()
		
	return render_to_response("stream/post.html", {
		'post':post
	}, context_instance=RequestContext(request))
