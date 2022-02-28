
from django.contrib import admin
from django.urls import path, include
# from crudApp import views
from signalApp import views as signal_views
from cbv_app import views as cbv_views
from django.contrib.auth import views as auth_views 
from rest_framework_simplejwt import views as jwt_views
# from myapp import views as myapp_views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/', include('crudApp.urls')),
    
    path('home/', signal_views.home, name='home'),
    path('custom_signal/', signal_views.customSignal, name='custom_signal'),

    path('school/', cbv_views.SchoolView.as_view(), name='school'),
    path('student_registration/', cbv_views.StudentRegView.as_view(), name='student_registration'),
    
    path('product/', include('cbv_app.urls')),
    path('blog/', include('blogappAuthExample.urls')),
    
    # path("accounts/", include("django.contrib.auth.urls")),

    # path('allauth/',include('socialLoginAllAuth.urls')),
    # path('accounts/', include('allauth.urls')),

    path('loginApp/',include('loginApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('article_api/', include('djangoRestFulApp.urls')),

    path("employee_crud/", include("ajaxCrudApp.urls")),\
    
    path('drf_apis/',include('djangoRestFrameWorkApp.urls')),
    
    # path('crud/',include('myapp.urls')),

    

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # path('',myapp_views.index,name='index'),
    # path('products/', myapp_views.product_list, name='product_list'),
    # path('create/', myapp_views.product_create, name='product_create'),
    # path('products/<int:pk>/update/', myapp_views.product_update, name='product_update'),
    # path('products/<int:pk>/delete/', myapp_views.product_delete, name='product_delete'),


   
   
   
# Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)

    # path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
    #  name='password_reset_done'),

    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
    #  name='password_reset_complete'),
  


]
