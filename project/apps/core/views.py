from rest_framework import permissions
from rest_framework import viewsets

from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
