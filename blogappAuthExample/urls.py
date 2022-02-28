from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.ListBlogsView.as_view(), name='blog_listing'),
    path('view_blog/<int:blog_id>/', views.ViewBlogView.as_view(), name='view_blog'),
    path('see_request',views.see_request,name = 'see_request'),
    path('see_userinfo',views.user_info, name='user_info'),
    path('private_place',views.private_place, name='private_place'),
    path('staff_place',views.staff_place, name='staff_place'),
    path("add_messages/", views.add_messages),
    path("user_verify/",views.UserVeriferView.as_view(), name='user_verify'),


    
]