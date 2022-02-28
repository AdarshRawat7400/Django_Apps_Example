from django.http import JsonResponse
from django.shortcuts import render
from django import views
from .serializers import StudentSerializer,TeacherSerializer
from .models import Student,Teacher
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from operator import ge
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import status
# from rest_framework import generics
# from rest_framework import mixins
from rest_framework import viewsets


class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailAPIView(APIView):
    
    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student ,request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




##################ViewSet#############################

class TeacherViewSet(viewsets.ViewSet):
    def list(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request,pk = None):
        queryset = Teacher.objects.all()
        teacher  = get_object_or_404(queryset,pk=pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def update(self, request, pk = None):
        teacher = Student.objects.get(pk=pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors(status=status.HTTP_400_BAD_REQUEST))
    
    def destroy(self,request, pk = None):
        teacher = Teacher.objects.get(pk=pk)
        teacher.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)






















# # Create your views here.

# # Single Object
# class StudentInfoView(APIView):
#     def get(self, request):
#         student = Student.objects.get(id=2)
#         serializer = StudentSerializer(student)
#         if serializer.is_valid():
#             return JsonResponse(serializer.data)
#         else:
#             return JsonResponse(serializer.errors)
#         # instead of using Http Response we can use JsonResponse
#         # json_data = JSONRenderer().render(serializer.data) 
#         # return HttpResponse(json_data, content_type='application/json')

# # QuerySet
# class StudentListView(APIView):
#     def get(self,request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
        
#         # instead of using Http Response we can use JsonResponse
#         # json_data = JSONRenderer().render(serializer.data)
#         # return HttpResponse(json_data, content_type='application/json')
        
#         return JsonResponse(serializer.data,safe=False)


# @method_decorator(csrf_exempt, name='dispatch')
# class StudentCreateView(APIView):
#     def post(self,request,pk=None):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         else:
#             print("ERROR")
#             return JsonResponse(serializer.errors)





