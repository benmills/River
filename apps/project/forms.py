from django import forms
from project.models import *

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		exclude = ('team')