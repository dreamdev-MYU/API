from django.urls import path
from .views import (CreateStudentView, ReadStudentView,
                     UpdateStudentView, DeleteStudentView)

urlpatterns = [
    path('create/', CreateStudentView.as_view(), name='create-student'),
    path('read/', ReadStudentView.as_view(), name='read-student'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update-student'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete-student'),
]
