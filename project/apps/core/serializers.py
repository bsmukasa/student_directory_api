from rest_framework import serializers
from .models import University, Student


class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    students = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='student-detail',
        queryset=Student.objects.all()
    )

    class Meta:
        model = University
        fields = ('pk', 'url', 'name', 'state', 'students')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    university = serializers.HyperlinkedRelatedField(
        view_name='university-detail',
        read_only=True
    )

    class Meta:
        model = Student
        fields = ('pk', 'url', 'first_name', 'last_name', 'university')
