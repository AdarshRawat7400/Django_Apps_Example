from django.shortcuts import get_object_or_404, render,HttpResponse
from django.views import View
from .forms import ProductForm, StudentForm
from .models import Product, Student
# Create your views here.
#Class Based View

class SchoolView(View):
    def get(self, request):
        return render(request, "school/home.html")


class StudentRegView(View):
   def get(self, request):
       form = StudentForm()
       return render(request, "school/student_registration.html", {'form':form})

   def post(self, request):
         form = StudentForm(request.POST)
         if form.is_valid():
              form.save()
              return HttpResponse("<center><h1>Thank you student has been successfully registered<h1></center>")
         else:
            return HttpResponse("<center><h1>Sorry student has not been registered ,INVAILD DETAILS!!!!<h1></center>")



class ProductRetriveView(View):
   def get(self, request,pk):
       product = get_object_or_404(Product, pk=pk)
       form = ProductForm(instance=product)
       return render(request, "product/product_detail.html", {'form':form})

class ProductInsertView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, "product/product_insert.html", {'form':form})

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<center><h1>Thank you product has been successfully registered<h1></center>")
        else:
            return HttpResponse("<center><h1>Sorry product has not been registered ,INVAILD DETAILS!!!!<h1></center>")

class ProductUpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, "product/product_update.html", {'form':form})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse("<center><h1>Thank you product has been successfully updated<h1></center>")
        else:
            return HttpResponse("<center><h1>Sorry product has not been updated ,INVAILD DETAILS!!!!<h1></center>")


# class ProductDeleteView(View):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         form = ProductForm(instance=product)
#         return render(request, "product/product_detail.html", {'form':form})

#     def delete(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         product.delete()
#         return HttpResponse("<center><h1>Thank you product has been successfully deleted<h1></center>")
