from difflib import restore
from django.shortcuts import render,HttpResponse
from django.views import View
from .models import Blog
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import  login_required,user_passes_test
from django.contrib import messages
# Create your views here.

class ListBlogsView(View):

    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'blog_listing.html', {'blogs': blogs})
    
class ViewBlogView(View):
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        data = {
            'blog':blog
        }
        return render(request, 'view_blog.html', data)

def see_request(request):
    text = f"""
        Some attributes of the HttpRequest object:

        scheme: {request.scheme}
        path:   {request.path}
        method: {request.method}
        GET:    {request.GET}
        user:   {request.user}
    """

    return HttpResponse(text, content_type="text/plain")


def user_info(request):
    text = f"""
        Selected HttpRequest.user attributes:

        username:     {request.user.username}
        is_anonymous: {request.user.is_anonymous}
        is_staff:     {request.user.is_staff}
        is_superuser: {request.user.is_superuser}
        is_active:    {request.user.is_active}
    """

    return HttpResponse(text, content_type="text/plain")


@login_required
def private_place(request):
    return HttpResponse('Authorized members only', content_type="text/plain")

@user_passes_test(lambda user:user.is_staff)
def staff_place(request):
    return HttpResponse("Employees must wash hands", content_type="text/plain")



@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello {username}")
    messages.add_message(request, messages.WARNING, "DANGER WILL ROBINSON")

    return HttpResponse("Messages added", content_type="text/plain")


class UserVeriferView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self,request,pk=0):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
            
        if user is not None:
            return HttpResponse(f"<center><h1> User {username} Exist In User DB</h1></center>")
        else:
            return HttpResponse(f"<center><h1> User {username} Not Exist In User DB Or Password Is Incorrect!!</h1></center>")
