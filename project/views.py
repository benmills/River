from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from post.models import *
from project.models import *
from project.forms import *
from post.forms import *

@login_required
def create_project(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else: form = ProjectForm()
	return render_to_response("project/create.html", {
		'form':form
	}, context_instance=RequestContext(request))

@login_required
def project_stream(request, project_id):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			p = form.save(commit=False)
			p.author_id = request.user.id;
			p.project_id = request.POST['project'];
			p.save()
		
	return render_to_response("stream/project.html", {
		'project':Project.objects.get(id=project_id),
		'projects':Project.objects.all(),
	}, context_instance=RequestContext(request))
