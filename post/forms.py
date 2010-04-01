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


class PostFileForm(forms.ModelForm):
	class Meta:
		model = PostFile
		exclude = ('posted_date')

def get_choices():
	choices = list()
	for u in User.objects.all():
		choices.append((u.id, u.get_profile().get_name()))
	return choices
	
class UserSelectionForm(forms.Form):
	#choices = list()
	user_id = forms.TypedChoiceField(choices=get_choices())

PostFileFormSet = inlineformset_factory(Post, PostFile, extra=1, form=PostFileForm, can_delete=False)
#AssignUserFormSet = inlineformset_factory(Post, UserProfile, extra=1, form=UserSelectionForm, can_delete=False, fk_name="assigned_tasks")