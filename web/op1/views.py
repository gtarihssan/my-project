from django.shortcuts import render , HttpResponse , redirect 
from django.http import HttpResponseRedirect , JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .generateur import verif , getcode
from django.contrib.auth.models import User
from .models import client ,municipality , comment , decribe ,decribe_to_check , projects
from django.contrib.auth import login , logout , authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import municipalityForm ,loginForm , clientForm ,decribeForm,formumForm , commentForm
from random import randrange
from django.db.models import Q
from django.http import HttpResponseRedirect #!!!!! to know(1) 
from django.core.mail import send_mail

from datetime import date
#================================ to fix ====================================================
def news(request):
    dec=decribe.objects.all().order_by('-date')
    if len(dec)>10 and len(dec)%2==0:
        dec=dec[:len(dec)/2]
    elif len(dec)>10 and len(dec)%2==1:
        dec=dec[:len(dec)-1/2]
    if request.method =='POST':
        req=request.POST['btn']
        print(req)
    else:    
        req='no'
    context={
        'req':req,
        'decs':dec
    }

    return render(request , 'op1/news.html' , context)





#============================= for update =============================================

def visit_deccheck(request):
    slugy=request.GET.get('dec_slugy')
    dec=decribe_to_check.objects.get(slugy=slugy)
    print((dec.client.user.username))
    print(dec.text)
    data={
        'titre': dec.titre ,
        'date' : str(dec.date)[:10],
        'mun' : dec.municipality.name,
        'text' : dec.text,
        'username' : dec.client.user.username,
        
    }

    return JsonResponse(data)

def check_decribes(request):
    decs=decribe_to_check.objects.all()
    return render(request , 'op1/decribe_to_check.html' , {'decs':decs})


def add_comment(request):
    if request.user.is_authenticated:
        texte=request.POST.get('text_data')
        slugy=request.POST.get('dec_slugy')
        dsecribe=decribe.objects.get(slugy=slugy)
        comments_number=comment.objects.filter(Decribe=dsecribe).count()
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            clientname=request.user.username
            cli=client.objects.get(user=request.user)
            
            new_commnet=comment.objects.create(text=texte , client=cli , Decribe=dsecribe)
            new_commnet.save()
            data={'clientname' : clientname ,
            'comment' : texte ,
            'comments_number':comments_number ,
            'clientpic' : cli.pic.url,
            'active' : True}
            return JsonResponse(data)
    else : 


        return JsonResponse({'active' : False})
    
def dec_info(request , slugy):
    dec=decribe.objects.get(slugy=slugy)
    mun=municipality.objects.get(id=dec.municipality_id)
    cli=client.objects.get(id=dec.client.id)
    com=comment.objects.filter(Decribe=dec).order_by("date")
    context={
        'dec':dec,
        'mun':mun,
        'cli':cli,
        'com':com[:6],
        'verif': len(com)!=0
    }
    return render(request , 'op1/description_info.html' , context)    
    







#=========================================================================================

def index(request):
    return render(request , 'op1/index.html')


def profile(request , id):
    usr=User.objects.get(id=id)

    cli=client.objects.get(user=usr)
    context={
        'cli':cli,
        'user':usr
    }
    return render(request , 'op1/profile.html' , context)

def municilitys(request):
    muns=municipality.objects.all()
    for i in muns:
        i.decrisption=i.decrisption[:500]
    muns=muns
    context={
        'muns':muns[:6]
    }
    return render (request ,'op1/municipality.html' , context)




def map(request):
    return render (request , 'op1/map.html')

def project(request):
    pros=projects.objects.all()
    context={
        'pros':pros
    }
    return render (request , 'op1/projects.html' , context)

def municiplity_info(request , slugy):
    mun=municipality.objects.get(slugy=slugy)
    decs=decribe.objects.filter(municipality=mun)
    context={
        'mun':mun,
        'decs':decs
    }
    return render(request , 'op1/municiplity_info.html' , context)




def munstatic(request , slugy):
    mun=municipality.objects.get(slugy=slugy)   
    data =[decribe.objects.filter(Q(tach='planification') & Q(municipality=mun)).count(),
    decribe.objects.filter(Q(municipality=mun) & Q(tach='gouvernance')).count(),
    decribe.objects.filter(Q(municipality=mun) & Q(tach='financement')).count()]    

    context= {
        'data':data
    }

    return render(request , 'op1/stat.html' , context)

#==========================================================================
def register(request):
    
    form= clientForm()
    if request.method =='POST':
        form=clientForm(request.POST , request.FILES)
        if form.is_valid():
            fname=form.cleaned_data['first_name']
            lname=form.cleaned_data['last_name']
            mail=form.cleaned_data['mail']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            password=form.cleaned_data['passwordv']
            code=form.cleaned_data['code']
            if request.POST.get('pic')!=None:
                pic='no.jpg'
            if code=='1234':
                user=User.objects.create_superuser(username=username , password=password , first_name=fname , last_name=lname)
                user.save()
                cli=client.objects.create(user=user , mail=mail , pic=pic)
                cli.save()
                login(request,user)
                return index(request)
            elif code=='':
                user=User.objects.create_user(username=username , password=password , first_name=fname , last_name=lname)
                user.save()
                cli=client.objects.create(user=user , mail=mail , pic=pic)
                cli.save()
                login(request,user)
                return index(request)
            else : 
                messages.error(request , 'admin code invalid')
                return register(request)
    return render(request , "op1/register.html" , {'form':form} )
    

def login_user(request):
    form=loginForm()
    if request.method=='POST':
        form=loginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request , username=username , password=password)
            if user is not None : 
                login(request , user)
                messages.error(request , 'connected succesfully')
                return index(request)
            else : 
                messages.error(request , 'sorry we can\'t find you in our data base')
                return render(request , 'op1/login.html' , {'form':form})
    else :
        return render(request , 'op1/login.html' , {'form':form})




def logout_user(request):
    logout(request)
    return index(request)



def create_municipality(request):
    munForm=municipalityForm()
    if request.method=='POST':
        munForm=municipalityForm(request.POST , request.FILES)
        if munForm.is_valid():
            name=munForm.cleaned_data['name']
            zone=munForm.cleaned_data['zone']
            print(zone)
            pic=munForm.cleaned_data['pic']
            decrisption=munForm.cleaned_data['decrisption']
            mun=municipality.objects.create(name=name , zone=zone ,  decrisption=decrisption,pic=pic )
            mun.save()
            return index(request)
    
    return render(request , 'op1/createmun.html' , {'munForm':munForm})


    


@login_required(login_url='login')
def add_decribe(request , slugy):
    mun=municipality.objects.get(slugy=slugy)
    pform=decribeForm()
    if request.method=='POST':
        pform=decribeForm(request.POST , request.FILES)
        if pform.is_valid():
            titre=pform.cleaned_data['titre']
            text=pform.cleaned_data['text']
            pic=pform.cleaned_data['pic']
            user=request.user   
            cli=client.objects.get(user=user)
            dec=decribe_to_check.objects.create(titre=titre , text=text , client=cli , municipality=mun , pic=pic)
            dec.save()
            messages.error(request,'thank you for your information but we should check it first ')
            return municiplity_info(request , slugy)
    else :
        context={
            'form':pform,
            'mun':mun
        }

        return render (request , 'op1/add_dec.html', context)
    

def delete_comment(request , id):
    com=comment.objects.get(id=id)
    mun=municipality.objects.get(decribe=decribe.objects.get(comment=com))
    com.delete()
    messages.error(request ,'are you sure to delete this Post sir ?')
    return municiplity_info(request , mun.slugy)

def delete_decribe(request ,slugy):
    dec=decribe.objects.get(slugy=slugy)
    mun=municipality.objects.get(decribe=dec)
    dec.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))   


def delete_municiplty(request , slugy):
    mun=municipality.objects.get(slugy=slugy)
    mun.delete()
    return index(request)


    


def into_decribe(request , slugy):
    dec=decribe_to_check.objects.get(slugy=slugy)
    return render(request , 'op1/into_decribe.html' , {'dec':dec})

def delete_decribe_checked(request , slugy):
    decribe_to_check.objects.get(slugy=slugy).delete()
    return check_decribes(request)




def formulaire(request , slugy):
    form=formumForm()
    dec=decribe.objects.get(slugy=slugy)
    context={
        'form':form,
        'dec':dec
    }
    if request.method=='POST':
        form=formumForm(request.POST)
        if form.is_valid():
            t=form.cleaned_data['tach']
            dec.tach=t
            dec.save()
            return check_decribes(request)
    else:
        return render(request , 'op1/formulaire.html' ,context)




def post_decribe(request , slugy):
    dec=decribe_to_check.objects.get(slugy=slugy)
    decs=decribe.objects.create(titre=dec.titre , text=dec.text , client=dec.client , municipality=dec.municipality , slugy=slugy , pic=dec.pic)
    decs.save()
    dec.delete()
    return formulaire(request , slugy )  


def profile(request , id):
    user=User.objects.get(id=id)
    cli=client.objects.get(user=user)
    dec=decribe.objects.filter(client=cli)
    com=comment.objects.filter(client=cli)
    context ={
        'client':cli,
        'decs':dec,
        'coms':com,   
    }
    return render(request , "op1/profile.html" , context)

