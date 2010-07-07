from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.models import User

from post.models import *
from userprofile.models import *
 
class PostForm(forms.ModelForm):
	assigned = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False)
	class Meta:
		model = Post
		fields = ('content', 'title', 'assigned')
		
class TodoForm(forms.ModelForm):
	content = forms.CharField()
	class Meta:
		model = TodoItem
		fields = ('post', 'content')

class PostFileForm(forms.ModelForm):
	class Meta:
		model = PostFile
		exclude = ('posted_date')

class FilterForm(forms.ModelForm):
	assigned = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False)
	class Meta:
		model = Filter
		
PostFileFormSet = inlineformset_factory(Post, PostFile, extra=1, form=PostFileForm, can_delete=False)
EditPostFileFormSet = inlineformset_factory(Post, PostFile, extra=1, form=PostFileForm)
TodoFormSet = inlineformset_factory(Post, TodoItem, extra=1, form=TodoForm, can_delete=False)
EditTodoFormSet = inlineformset_factory(Post, TodoItem, extra=1, form=TodoForm)