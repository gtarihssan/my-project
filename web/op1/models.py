from django.db import models
from slugify import slugify
from django.contrib.auth.models import User
from random import randrange



governess= [
    ('tunis' , 'tunis'),
    ("ariana",'ariana'),
    ('nabeul','nabeul')
]

class client(models.Model):
    user=models.OneToOneField(User , on_delete=models.CASCADE)
    mail=models.EmailField(max_length=70 , null=True)
    pic=models.ImageField(null='True', blank='True', default='no.jpg')


    def __str__(self):
        return self.user.username
    



class municipality(models.Model):
    name=models.CharField(max_length=500 , null=None , default="municipalite x")
    zone=models.CharField(max_length=50)
    pic=models.ImageField(null=True , blank=True)
    slugy=models.SlugField(max_length=500 , blank=True , null=True)
    decrisption=models.TextField(max_length=2000, null=True)
    locali=models.CharField(max_length=20000 , blank=True , null=True)
    finance=models.PositiveIntegerField(blank=True , null=True)
    gouve=models.PositiveIntegerField(blank=True , null=True)
    plani=models.PositiveIntegerField(blank=True , null=True)

    def save(self ,*args , **kwargs):
        if self.slugy==None:
            ch=self.name+" "+self.zone+" "+str(randrange(1000,9999))
            self.slugy= slugify(ch)
        super().save(*args , **kwargs)

    def __str__(self):
        return self.name


class projects(models.Model):
    titre=models.CharField(max_length=2000)
    image=models.ImageField()
    decription=models.CharField(max_length=2000 , null=True , blank=True)
    municipilty=models.ForeignKey(municipality , on_delete=models.CASCADE)
    date_de_debut=models.DateField(auto_now=True)

    def __str__(self):
        return self.titre
    



class decribe(models.Model):
    titre=models.CharField(max_length=50 , null=False , blank=True)
    text=models.TextField(max_length=2000 , null=True , blank=True )
    pic=models.ImageField(null=True , blank=True)
    slugy=models.SlugField(max_length=500 , blank=True , null=True)
    client=models.ForeignKey(client , on_delete=models.CASCADE  , null=False , default="ananymous")
    date=models.DateTimeField(auto_now=True)
    municipality=models.ForeignKey(municipality , on_delete=models.CASCADE , default=None)
    tach=models.CharField(max_length=50 , null=True , blank=True)
    admin_decribe=models.CharField(max_length=2000 , null=True , blank=True)

    def save(self ,*args , **kwargs):
        if self.slugy==None:
            ch=self.titre+' '+str(randrange(1000,9999))
            self.slugy=slugify(ch)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.slugy
    

class decribe_to_check(models.Model):
    titre=models.CharField(max_length=50 , null=False , blank=True)
    text=models.TextField(max_length=2000 , null=True , blank=True )
    #image=
    slugy=models.SlugField(max_length=500 , blank=True , null=True)
    client=models.ForeignKey(client , on_delete=models.CASCADE  , null=False , default="ananymous")
    date=models.DateTimeField(auto_now=True)
    municipality=models.ForeignKey(municipality , on_delete=models.CASCADE , default=None)
    pic=models.ImageField(blank=True , null=True , default="no.jfif")

    def save(self ,*args , **kwargs):
        if self.slugy==None:
            ch=self.titre+' '+str(randrange(1000,9999))
            self.slugy=slugify(ch)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.slugy

class comment(models.Model):
    text=models.CharField(max_length=700)
    client=models.ForeignKey(client , on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    Decribe=models.ForeignKey(decribe , on_delete=models.CASCADE , default=None)
    

    def __str__(self):
        return self.text




    