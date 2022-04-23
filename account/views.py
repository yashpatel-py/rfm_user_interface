from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import SignupForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

class signUp(SuccessMessageMixin, generic.CreateView):
    form_class = SignupForm
    template_name = "main/register.html"
    success_url = reverse_lazy('login')
    success_message = "User has been created, please login with your username and password"
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please enter details properly")
        return redirect('home')

class logIn(generic.View):
    form_class = LoginUserForm
    template_name = "main/login.html"
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        if request.method == "POST":
            form = LoginUserForm(request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                
                user = authenticate(username = username, password=password)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, f"You are logged in as {username}")
                    return redirect('home')
                else:
                    messages.error(request, "Error")
            else:
                messages.error(request, "Username or password incorrect")
        form = LoginUserForm()
        return render(request, "main/login.html", {"form": form})

class logOut(generic.View):
    def get(self, request):
        logout(request)
        messages.success(request, "User logged out")
        return redirect('home')