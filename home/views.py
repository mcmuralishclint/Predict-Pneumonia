from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .forms import LoginForm, SignUpForm,ImageForm
from django.contrib import messages
from django.contrib.auth.models import User
from marketing.forms import EmailSignupForm
from .models import UploadImage
from PIL import Image

def home_view(request):
	images=None
	email_form = EmailSignupForm()
	image_form = ImageForm(request.POST, request.FILES)
	if request.method == "POST":
		if email_form.is_valid():
			email = request.POST["email"]
			new_signup = Signup()
			new_signup.email = email
			new_signup.save()
		else:
			if image_form.is_valid():

				#images = request.FILES['image']
				new_image = UploadImage(image = request.FILES['image'])
				new_image.save()

				images = UploadImage.objects.all()
				images = images[len(images)-1]

	context = {
	'page':'home',
	'form_marketing':email_form,
	'imageform': image_form,
	'images':images
	}
	return render(request,"index.html",context)

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
	loginform = LoginForm(request.POST or None)
	if loginform.is_valid():
		username = loginform.cleaned_data['username']
		password = loginform.cleaned_data['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('/')
		else:
			loginform = LoginForm()
			messages.warning(request, 'Wrong username or password') 
			#return redirect('#login')
	context = {
	"form":loginform,
	'page':'login'
	}
	return render(request,"login.html",context)

def signup_view(request):
	signupform = SignUpForm(request.POST or None)
	if signupform.is_valid():
		username = signupform.cleaned_data['username']
		password = signupform.cleaned_data['orig_password']
		firstname = signupform.cleaned_data['firstname']
		user = User.objects.create_user(firstname,username,password)
		user.save()
		return redirect('/login')
		messages.success(request, 'User Created') 
	context = {
	"form":signupform,
	'page':'signup'
	}
	return render(request,"signup.html",context)

