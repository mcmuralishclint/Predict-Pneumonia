from django import forms
from .models import Signup

class EmailSignupForm(forms.ModelForm):
	email = forms.EmailField(widget = forms.TextInput(attrs = {
		"class":"form-control flex-fill mr-0 mr-sm-2 mb-3 mb-sm-0",
		'name':"email",
		 'id':"inputEmail",
		 'placeholder':"Type your email address"
		}),label="")
	class Meta:
		model = Signup
		fields = ('email',)

		