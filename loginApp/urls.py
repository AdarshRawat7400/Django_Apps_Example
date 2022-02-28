from loginApp import views
from django.urls import path
from django.contrib.auth.decorators import login_required
urlpatterns = [  
    path('', views.RegistrationView.as_view(), name = 'register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('dashboard', login_required(views.DashBoardView.as_view()), name='dashboard'),
    path('logout', views.LogoutView.as_view(), name='logout_page'),
]  