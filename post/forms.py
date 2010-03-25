from django import forms
from django.forms.models import inlineformset_factory
from post.models import *
 
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('author', 'assigned', 'posted_date', 'project')

