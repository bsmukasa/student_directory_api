from haystack import indexes
from .models import Student, University


class StudentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    university = indexes.CharField(model_attr='university')

    def get_model(self):
        return Student

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class UniversityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    state = indexes.CharField(model_attr='state')
    students = indexes.MultiValueField()

    def get_model(self):
        return University

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_students(self, obj):
        return [student.last_name for student in obj.students.all()]
