from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import generic

from .forms import CreateUserForm, LoginForm

# Create your views here.
def registerPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('users:login')
			else:
				print("fallo")
		else:
			context = {'form':form}
			return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect("main:home")
	else:
		form = LoginForm
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect("main:home")
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {'form': form}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('users:login')

def profile(request):
	profile = request.user
	return render(request, 'profile.html', {'profile': profile})