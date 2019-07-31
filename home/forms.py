from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(widget = forms.PasswordInput)

class SignUpForm(forms.Form):
	username = forms.CharField(max_length=20)
	firstname = forms.CharField(max_length=20)
	orig_password = forms.CharField(widget = forms.PasswordInput)
	confirm_pass = forms.CharField(widget = forms.PasswordInput)

	def clean_confirm_pass(self):
		if self.cleaned_data["orig_password"]!=self.cleaned_data["confirm_pass"]:
			raise forms.ValidationError("Password must match")

