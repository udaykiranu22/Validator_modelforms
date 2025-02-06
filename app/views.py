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

# we need to create templatetags package ===================================================

def strings(request):
    data = 'udaY Kiran how are YOU'
    import datetime
    dt = datetime.datetime.now()
    kiss = [0,1,2]
    d = {'data' : data,'dt':dt, 'kiss':kiss}
    return render(request, 'demo.html', d)
