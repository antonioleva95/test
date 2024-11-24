from django.shortcuts import render, redirect
from myapp.models import content
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "auth.html")

def main(request):

    if request.method=="POST":
        data=request.POST

        new=content(name=data['name'], description=data['description'], country=data['country'], cost=data['cost'], count=data['count'])
        new.save()

    return render(request, "main.html")


    
def kartochka(request):
    data=content.objects.all()
    return render(request, "kartochka.html", {'test':data})


def reg (request):
    if request.method=='POST':
        data=request.POST
        new=User.objects.create_user(data['lgn'],data['email'],data['pas'])
        new.save()
    return render(request, 'reg.html')

def auth(request):
    if request.method=='POST':
        data=request.POST
        user=authenticate(username=data['lgn'],password = data['pas'])
        if user is not None:
            request.session["is_auth"]=user.id
            return redirect(card)
        else:
            return redirect(auth)
    else:
        return render(request, 'auth.html')
    

def card(request):

    if request.session.get("is_auth",False):
        user=User.objects.filter(id=request.session.get("is_auth", False))

        data=content.objects.all()
        return render(request, "card.html", {'data':data})
    else:
        return HttpResponse("Не авторизован")


def card_name(request, card_name_id):
    data=content.objects.filter(id = card_name_id)
    return render(request, "card_name.html", {'data':data})
