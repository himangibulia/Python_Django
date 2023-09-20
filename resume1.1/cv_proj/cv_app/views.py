from django.shortcuts import render, HttpResponse,redirect

from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login , logout

from .models import cv
from .forms import cv_form

# Create your views here.

# cv.html output page
def my_cv(request):
    data=cv.objects.filter(user=request.user)
    print(data)
    for i in data:
        print(i)
    Language=[]
    Skill=[]
    In_percent=[]
    Interest=[]
    
    for i in data[0].language.split(','):
        Language.append(i)
        
    for i in data[0].skill.split(','):
        Skill.append(i)
        
    for i in data[0].in_percent.split(','):
        In_percent.append(i)
    
    for i in data[0].interest.split(','):
        Interest.append(i)
        
    context={
        'data':data,
        'language':Language,
        'skill':Skill,
        'interest':Interest,
    }
    return render(request,'cv.html',context)

# cv_forms.html form page
def cv_forms(request):
    if request.method=="POST":
        a=cv_form(request.POST, request.FILES)
        print(a)
        if a.is_valid():
            user = request.user
            name=a.cleaned_data['name']      
            image=a.cleaned_data['image']
            ability=a.cleaned_data['ability']
            dob=a.cleaned_data['dob']
            mobile=a.cleaned_data['mobile']
            email=a.cleaned_data['email']
            github_id=a.cleaned_data['github_id']
            linkedin_id=a.cleaned_data['linkedin_id']
            address=a.cleaned_data['address']
            years_degree=a.cleaned_data['years_degree']
            name_degree=a.cleaned_data['name_degree']
            clg_name=a.cleaned_data['clg_name']
            year12th=a.cleaned_data['year12th']
            class_name12th=a.cleaned_data['class_name12th']
            school_name12th=a.cleaned_data['school_name12th']
            year10th=a.cleaned_data['year10th']
            class_name10th=a.cleaned_data['class_name10th']
            school_name10th=a.cleaned_data['school_name10th']
            language=a.cleaned_data['language']
            about_para=a.cleaned_data['about_para']
            working_years_1=a.cleaned_data['working_years_1']
            company_name_1=a.cleaned_data['company_name_1']
            designation_1=a.cleaned_data['designation_1']
            about_1=a.cleaned_data['about_1']
            working_years_2=a.cleaned_data['working_years_2']
            company_name_2=a.cleaned_data['company_name_2']
            designation_2=a.cleaned_data['designation_2']
            about_2=a.cleaned_data['about_2']
            skill=a.cleaned_data['skill']
            in_percent=a.cleaned_data['in_percent']
            interest=a.cleaned_data['interest']
            
            cv(user=user,name=name,image=image,ability=ability,dob=dob,mobile=mobile,email=email,github_id=github_id,linkedin_id=linkedin_id,address=address,years_degree=years_degree,name_degree=name_degree,clg_name=clg_name,year12th=year12th,class_name12th=class_name12th,school_name12th=school_name12th,year10th=year10th,class_name10th=class_name10th,school_name10th=school_name10th,language=language,about_para=about_para,working_years_1=working_years_1,company_name_1=company_name_1,designation_1=designation_1,about_1=about_1,working_years_2=working_years_2,company_name_2=company_name_2,designation_2=designation_2,about_2=about_2,skill=skill,in_percent=in_percent,interest=interest).save()
            return redirect('/cv/')
        
    a=cv_form()
    context={
            'a':a
    }
    return render(request,'cv_forms.html',context) 

## CREATE ACCOUNT PAGE
def Create_Account(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        email=request.POST.get('email')
        passw=request.POST.get('password')
        print(uname,email,passw)
        
        if User.objects.filter(username=uname).first():
            messages.success(request,'username is taken')
            
        if User.objects.filter(email=email).first():
            messages.success(request,'email is taken')
            
        else:
            user = User(username=uname,email=email)
            user.set_password(passw)
            user.save()
            messages.success(request,'account create !!')
    
    return render(request,'create_account.html')

## LOGIN PAGE 
def login_page(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password =request.POST.get('password')
            print(username,password)
           
            if not username or not password:
                messages.success(request,'Boths fields are required !')

            user_obj = User.objects.filter(username=username).first()
            user = authenticate(username=username,password=password)

            if user_obj is None:
                messages.success(request,'User Not found !')
            print(user_obj)

            if user is not None:
                login(request,user)
                return redirect('/cv_forms/')
            
            if user is None:
                messages.success(request,'Wrong Password !!')

    return render(request,'login.html')