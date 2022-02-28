from django.urls import path, include
from . import views
from .routers import router

urlpatterns = [

path('student/',views.StudentAPIView.as_view(),name='student'),
path('detail/<int:pk>/',views.StudentDetailAPIView.as_view(),name='student-detail'),
path('teacher_viewset/',include(router.urls),name='teacher_viewset'),
path('teacher_viewset/<int:pk>/',include(router.urls),name='teacher_viewset')










# path('studentinfo/',views.StudentInfoView.as_view(), name='student_info'),
# path('studentlist/',views.StudentListView.as_view(), name='student_list'),
# path('createstudent/',views.StudentCreateView.as_view(), name='create_student'),


]