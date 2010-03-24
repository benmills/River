from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput)
	class Meta:
		model = User
		fields = ["username", "email", "first_name", "last_name"]