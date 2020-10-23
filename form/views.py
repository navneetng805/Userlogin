from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    a = User.objects.all()
    return render(request,'index.html',{'a' : a})

def signup(request):
    return render(request,'signup.html')

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        mobile = request.POST['mobile']
        fname = request.POST['fname']
        lname = request.POST['lname']
        img = request.POST['img']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return redirect('index') 
    else:
        return HttpResponse('Not Found')

def signin(request):
    return render(request,'signin.html')

def handlesignin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username = loginusername, password = loginpass)
    
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('Invalid Credentials')
    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('index')