from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
def Register(request):
    if request.method == 'POST':
        #messages.error(request, 'Testing error message')
        #Register user
        #return redirect('Register')
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check if passwords match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('Register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'You already have account')
                    return redirect('Register')
                else:
                    user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    #Login after Register
                    #auth.login(request,user)
                    #messages.success(request, 'You are not Logged in')
                    #return redirect('index')
                    user.save()
                    messages.success(request,'You are now Registered and can Login')
                    return redirect('Login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('Register')
    else:
        return render(request, 'accounts/register.html')



def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are now logged in')
            return redirect('Dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('Login')


    else:
        return render(request, 'accounts/login.html')

def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now Logged out')
        return redirect('index')
        #Register user
        return
    else:
        return redirect('index')

def Dashboard(request):
    if request.method == 'POST':
        #Register user
        return
    else:
        return render(request, 'accounts/dashboard.html')
