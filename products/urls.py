from django.urls import path
from .views import (CreateProductView, ReadProductView,
                     UpdateProductView, DeleteProductView)

urlpatterns = [
    path('create/', CreateProductView.as_view(), name='create-Product'),
    path('read/', ReadProductView.as_view(), name='read-Product'),
    path('update/<int:pk>/', UpdateProductView.as_view(), name='update-Product'),
    path('delete/<int:pk>/', DeleteProductView.as_view(), name='delete-Product'),
]
