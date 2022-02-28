from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout


# Create your views here.
def index(request):
    return render(request, "user/index.html")

def logout(request):
    auth_logout(request)
    return redirect('index')