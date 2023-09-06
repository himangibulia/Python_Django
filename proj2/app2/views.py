from django.shortcuts import render, HttpResponse
from .models import student_detail

# Create your views here.

def index(request):
    return render(request,'index.html')

def stat(request):
    return render(request,'stat.html')

def form(request):
    return render(request,'form.html')

def contact(request):
    return render(request,'contact.html')

def stud(request):
    data=student_detail.objects.all()
    context={'d':data}
    return render(request,'stud.html',context)