from django.shortcuts import render

# Create your views here.
def instaclone(request):
    return render(request,'instaclone.html')

def position(request):
    return render(request,'position.html')

def home(request):
    return render(request,'home.html')