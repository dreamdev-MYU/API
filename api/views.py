
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer

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