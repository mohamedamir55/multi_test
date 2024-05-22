from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def register (request):
    if request.method=='POST':
        email=request.POST.get('email')
        username=email.split('@')[0]
        password=request.POST.get('password1')
        confirm_password=request.POST.get('password2')
        if password == confirm_password:
                user=User.objects.create_user(username=username,email=email,password=password)
                send_mail(
                'Succes Signup',
                f'Your username is :{username}\n your password is: {password} \n ',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
                return redirect ('accounts:login')
        else:
                return HttpResponse('Invalid password')

    return render(request,'accounts/register.html')

def login_view (request):
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect ('home')

    return render(request,'accounts/login.html')

def logout_view(request):
        logout(request)
        return redirect('accounts:login')

def forget_password (request):
        email=request.POST.get('email') 
        new_password=User.objects.make_random_password()
        user=User.objects.filter(email=email).first()
        user.set_password(new_password)
        user.save
        send_mail(
                'reset password',
                f' your permnant password is: {new_password} \n ',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
        
        
       
        return render(request,'accounts/forget_password.html')

def reset_password(request):
        email=request.POST.get('email')
        old_password=request.POST.get('oldpassword')
        new_password1=request.POST.get('password1')
        new_password2=request.POST.get('password2')
        user=User.objects.filter(email=email)
        if new_password1==new_password2 and old_password is authenticate :
            user.set_password(new_password2)
            user.save
            send_mail(
                'reset password',
                f' your new password is: {new_password2} \n ',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

        return render (request,"accounts/reset_password.html")