from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .custom_permissions import IsAdminOrReadOnly


class StudentApiListView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def  get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class CreateStudentView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateStudentView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ReadStudentView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class DeleteStudentView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer