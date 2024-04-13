from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializer, Student
from rest_framework.response import Response


class StudentApiView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"status": "success"})

class StudentDetailApiView(APIView):
    def get(self, request, student_id):
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student)

        return Response(serializer.data)

class StudentUpdateApiView(APIView):
    def put(self, request, id):
        student = get_object_or_404(Student, id=id)

        serializer = StudentSerializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

class StudentDeleteApiView(APIView):
    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()

        return Response({"Message":"Deleted"})


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


