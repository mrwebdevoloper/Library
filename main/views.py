from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from django.shortcuts import render, redirect
from .models import *

def Home(request):

    # category = Category.objects.all()

    context = {

        'category': Category.objects.all(),
        'products':Product.objects.all(),

    }

    return render(request, 'index.html', context)


def Categorys(request, id):
    products = Product.objects.filter(category_id=id)
    category = Category.objects.all()

    context = {
        'products': products,
        'category': category,

    }
    return render(request, 'shop.html', context)

def Sorov(request):

    return render(request, 'login/index.html')


def Login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user )
            return redirect('/yuklash/')
        else:
            return redirect('/yuklash/')
    else:

        return render(request, 'login/login.html')




def Register(request):

    if request.method == 'POST':
        r = request.POST
        username = r['username']
        password = r['password']
        ism = r['ism']
        fam = r['fam']
        phone = r['phone']
        birthday = r['birthday']
        address = r['address']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('/login/')
        else:
            user = Users.objects.create(username=username, password=password, first_name=ism, last_name=fam, phone=phone, birthday=birthday, address=address)
            login(request, user)
            return redirect('/yuklash/')

    else:
        return render(request, 'login/register.html')

def Yuklash(request):
    context = {
        'category': Category.objects.all()
    }
    if request.method == "POST":
        r = request.POST
        f = request.FILES

        category = r['category']
        rasm = f['rasm']
        name = r['name']
        muallif = r['muallif']
        file = f['file']

        Product.objects.create(category_id=category, name=name, photo=rasm, pdf=file,  muallif=muallif)

        return redirect('/kirish/')
    else:
        return render(request, 'login/yuklash.html', context)

def Logout(request):
    logout(request)
    return redirect('/login/')

def DeleteCart(request, id):

    item = Product.objects.get(id=id)
    item.delete()


    return redirect('/kirish/')