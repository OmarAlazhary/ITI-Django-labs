from django import forms
from .models import Trainee
from course_app.models import Course


class AddTraineeForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    email = forms.EmailField()
    course = forms.ChoiceField(choices=[(course.id, course.name) for course in Course.objects.all()])
