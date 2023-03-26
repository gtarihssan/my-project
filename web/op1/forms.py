from django.forms import ModelForm
from .models import municipality ,decribe , client
from django import forms


governess= [
('tunis' , 'tunis'),
("ariana",'ariana'),
('nabeul','nabeul'),
('souse','souse'),
('mounastir','mounastir'),
('touzeur','touzeur'),
('beja','beja'),
('jandouba','jandouba'),
('zaghouan','zaghouan'),
]


class municipalityForm(forms.Form):

    name=forms.CharField(max_length=100 , required=False, widget=forms.TextInput(attrs={'class':'name' , 'placeholder' : 'name'}))
    zone=forms.ChoiceField(choices=governess , required=True , widget=forms.Select(attrs={'class':'zone', 'placeholder' : 'zone'}))
    pic=forms.ImageField(required=False ,widget=forms.FileInput(attrs={'class':'photo', 'placeholder' : 'description'}) )
    decrisption=forms.CharField( widget=forms.Textarea(attrs={'class':'dec', 'placeholder' : 'description'}))



class clientForm(forms.Form):
    first_name=forms.CharField(max_length=100 , required=True , widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'first name'}))
    last_name=forms.CharField(max_length=100 , required=True ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'last name'}))
    mail=forms.EmailField( required=True ,widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'email'}))
    pic=forms.ImageField(required=False)
    username=forms.CharField(max_length=100, required=True ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'username'}))
    password=forms.CharField(required=True , widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder' : 'password'}))
    passwordv=forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder' : 'password-confirm'}))
    code=forms.CharField(max_length=100 , required=False ,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'put the admin code'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        passwordv = cleaned_data.get('passwordv')

        if password != passwordv:
            raise forms.ValidationError("Passwords do not match")
        

class loginForm(forms.Form):
    username=forms.CharField(max_length=100 , required=True , widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'username'}))
    password=forms.CharField(max_length=100 , required=True , widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder' : 'password'}))

class decribeForm(forms.Form):
    titre=forms.CharField(max_length=100 , required=True , widget=forms.TextInput(attrs={'class':'describe_titre', 'placeholder' : 'titre'}))    
    text=forms.CharField(max_length=1500 , required=True , widget=forms.Textarea(attrs={'class':'describe_text', 'placeholder' : 'your description'}))  
    pic=forms.ImageField(required=False)


tach={
    ('gouvernance','gouvernance'),
    ('financement','financement'),
    ('planification','planification'),
}

class formumForm(forms.Form):
    tach=forms.ChoiceField(choices=tach , required=True ,widget=forms.Select(attrs={'class':'form-control', 'placeholder' : 'zone'}))
    dic=forms.CharField(max_length=1500 , required=True , widget=forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'decribe for the decribe posted'})) 


class projectForm(forms.Form):
    titre=forms.CharField(max_length= 2000 , required=True , widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder':'titre'}))
    decription=forms.CharField(max_length= 2000 , required=True , widget=forms.Textarea(attrs={'class':'form-control' , 'placeholder':'decription'}))
    image=forms.ImageField(required=True)
    

class commentForm(forms.Form):
    comment=forms.CharField(max_length=100 , required=True , widget=forms.Textarea(attrs={'class':'form-control', 'placeholder' : 'comment'}))