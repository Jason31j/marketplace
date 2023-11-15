from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from .forms import CreateUserForm, LoginForm, ProfileForm
from .models import UserProfile

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
                messages.error(request, 'Error creating account')
                return render(request, 'register.html', {'form': form})
        else:
            context = {'form': form}
            return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        form = LoginForm
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

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


class profileView(LoginRequiredMixin ,generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['profile'] = UserProfile.objects.get(user=user)
        return context


class profileUpdateView(LoginRequiredMixin ,generic.UpdateView):
    model = UserProfile
    form_class = ProfileForm
    template_name = 'profile_update.html'

    def get_object(self):
        return UserProfile.objects.get(user=self.request.user)
    
    def form_valid(self, form):
        # Update user email
        new_email = form.cleaned_data['email']
        user = self.request.user
        user.email = new_email
        user.save()

        # Update user profile
        form.save()

        messages.success(self.request, 'Profile updated successfully')
        return redirect('users:profile')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Set email placeholder
        form.fields['email'].initial = self.request.user.email
        return form

    def get_success_url(self):
        return reverse('users:profile')