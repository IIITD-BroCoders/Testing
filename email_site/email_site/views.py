from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import user
import random

def index(request):
    return render(request,'login_page.html')

# def check_username(request):
#     return True

@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', 'default')
        pass_word = request.POST.get('password', 'default')
        print(user_name)
        print(pass_word)
        return render(request, 'home_screen.html')
    

@csrf_exempt
def sign_up(request):
    if request.method =='POST':
        first_name = request.POST.get('first_name','default')
        middle_name = request.POST.get('middle_name','default')
        last_name = request.POST.get('last_name','default')
        user_name = request.POST.get('username',None)
        pass_word = request.POST.get('password', 'default')
        con_password = request.POST.get('con_password','default')

        User = user(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            user_name=user_name,
            password=pass_word,
            id=  random.randint(100000,999999)
        )
        User.save()
        
        return render(request, 'home_screen.html')
    else:
        return render(request,"sign_up.html")


        