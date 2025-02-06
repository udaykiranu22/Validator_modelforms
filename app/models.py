from django.db import models
from django.core import validators
# Create your models here.

class Student(models.Model):
    sid = models.CharField(primary_key=True, max_length=10,validators=[validators.MaxLengthValidator(10)])
    sname = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, validators=[validators.RegexValidator(r'[6-9]\d{9}')])
    email = models.EmailField()
    def __str__(self):
        return self.sname
