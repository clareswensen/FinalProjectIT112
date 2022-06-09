from importlib.resources import Resource
from django import forms
from .models import Course, Assignment

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'

class AssignmentForm(forms.ModelForm):
    class Meta:
        model=Assignment
        fields='__all__'