from django import forms
from app.models import *

class StudentForm(forms.ModelForm):
    botcatch = forms.CharField(required=False,widget=forms.HiddenInput())
    class Meta:
        model = Student
        fields = '__all__'
