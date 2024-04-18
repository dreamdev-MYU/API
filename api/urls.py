from django.urls import path
from .views import (CreateStudentView, ReadStudentView,
                     UpdateStudentView, DeleteStudentView,StudentApiListView)

urlpatterns = [
    path('create/', CreateStudentView.as_view(), name='create-student'),
    path('read/', ReadStudentView.as_view(), name='read-student'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update-student'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete-student'),
    path('students/', StudentApiListView.as_view(), name='students-list'),
]
