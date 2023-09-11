from django.shortcuts import render,HttpResponse
from .models import myprofile
from .forms import profile_form

# Create your views here.

def profile(request):
    if request.method == "POST":
        
        name= request.POST['name']
        f_name= request.POST['f_name']
        m_name= request.POST['m_name']
        email= request.POST['email']
        r_no= request.POST['roll_no']
        m_no= request.POST['mobile_no']
        g= request.POST['gender']
        ad= request.POST['address']
        state= request.POST['state']
        c= request.POST['city']
        p= request.POST['pin_code']
        i= request.POST['img']
        s= request.POST['stream']
        d= request.POST['description']
        
        myprofile(name=name, father_name=f_name, mother_name=m_name, email=email, roll_no=r_no, strem=s, address=ad, state=state, city=c, pin_code=p, gender=g, mobile_no=m_no, image=i, description=d).save()
        print(name,f_name,m_name,email,r_no,s,ad,state,c,p,g,m_no,i,d)
 
    return render(request,'profile.html')

def profile_forms(request):
    if request.method=="POST":
        a=profile_form(request.POST, request.FILES)
        print(a)
        if a.is_valid():
            name=a.cleaned_data['name']
            father_name=a.cleaned_data['father_name']
            mother_name=a.cleaned_data['mother_name']
            email=a.cleaned_data['email']
            roll_no=a.cleaned_data['roll_no']
            mobile_no=a.cleaned_data['mobile_no']
            gender=a.cleaned_data['gender']
            address=a.cleaned_data['address']
            state=a.cleaned_data['state']
            city=a.cleaned_data['city']
            pin_code=a.cleaned_data['pin_code']
            image=a.cleaned_data['image']
            stream=a.cleaned_data['stream']
            description=a.cleaned_data['description']
            
            myprofile(name=name,father_name=father_name,mother_name=mother_name,email=email,roll_no=roll_no,mobile_no=mobile_no,gender=gender,address=address,state=state,city=city,pin_code=pin_code,image=image,strem=stream,description=description).save()
            
            return HttpResponse('Data Saved !!!')
  
    a=profile_form()
    context={
            'a':a
    }
    return render(request,'pro_form.html',context)                                                

def get_data(request):
    data=myprofile.objects.all()
    print(data)