from django.contrib.auth.models import User,Group
from django import forms

class LoginForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password',)