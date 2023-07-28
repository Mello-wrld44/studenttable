from django import forms
from school.models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['Name','Admission','Course']