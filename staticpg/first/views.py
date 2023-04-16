from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method =='POST':
        un = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=un,password=password)

        if user is not  None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('login')

    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        email_id = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['confirm password']

        if password == password1:

            if User.objects.filter(username=user_name).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request,"email id taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, email=email_id, password=password)
                user.save()
                return redirect('login')


        else:
            messages.info(request,"password and confirm password are not a match")
            return redirect('register')

        return redirect('/')
    return render(request,'registration.html')