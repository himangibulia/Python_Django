from django import forms

class profile_form(forms.Form):
    name=forms.CharField()
    father_name=forms.CharField()
    mother_name=forms.CharField()
    email=forms.EmailField()
    roll_no=forms.IntegerField()
    mobile_no=forms.CharField()
    gender=forms.CharField()
    address=forms.CharField()
    state=forms.CharField()
    city=forms.CharField()
    pin_code=forms.CharField()
    image=forms.ImageField()
    stream=forms.CharField()
    description=forms.CharField()