from django import http
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views import View
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordResetForm
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.db.models.query_utils import Q







class RegistrationView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')  

        return render(request, 'registration/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'registration/login.html',{'form':form})

    def post(self,request,pk=0):
        print("POST METHOD")
        form  = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            if user is not None:
                login(request,user)
                return HttpResponse("Authentication was Successful")
            else:
                return HttpResponse("Authentication was not Successful")
            


class DashBoardView(View):
    def get(self,request,pk=0):
        context = {'user':request.user}
        return render(request,'registration/dashboard.html',context)


class LogoutView(View):
    def get(self,request,pk=0):
        logout(request)
        return render(request,'registration/logout_page.html')