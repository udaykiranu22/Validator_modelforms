from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def studentv(request):
    ESFO = StudentForm()
    d = {'ESFO': ESFO}
    if request.method == 'POST':
        SFO = StudentForm(request.POST)
        if SFO.is_valid():
            SFO.save()
            return HttpResponse('Data Inserted Successfully')
        else:
            return HttpResponse('Error Form Invalid')
    return render(request, 'student.html', d)