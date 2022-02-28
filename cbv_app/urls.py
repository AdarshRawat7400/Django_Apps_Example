from django.urls import path, include
from . import views
urlpatterns = [

    path("list_products/<int:pk>/", views.ProductRetriveView.as_view(), name="list_products"),
    path("insert/", views.ProductInsertView.as_view(), name="product_insert"),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),

]