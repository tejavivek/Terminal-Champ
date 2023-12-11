from django.shortcuts import redirect,render
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login,logout
from LinuxChamp import settings
from django.core.mail import send_mail
import mimetypes


def home(request):
    return render(request,"authentication/index.html")

def signup(request):

     if request.method == "POST":
        username = request.POST['username']
        fname =  request.POST['fname']
        lname =  request.POST['lname']
        email = request.POST['email']
        pass1=  request.POST['pass1']
        pass2=  request.POST['pass2']


        if User.objects.filter(username=username):
            messages.error(request, "Username already exists! Please try some other username")
            return redirect('home')

        if User.objects.filter(email=email):
             messages.error(request, "Email already registered! Please try other mail ")
             return redirect('home')

        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")

        if pass1 != pass2:
            messages.error(request,  "Passwords didn't match!")

        if not username.isalnum():
            messages.error(request, "username must be alpha-numeric!")
            return redirect

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname


        myuser.save()

        messages.success(request, "Your Account has been successfully created. We have sent you a confirmataion")


        # Welcome EMAIL

        subject = "Welcome to Terminal Champ!"
        message =  "Hello" + myuser.first_name + "!! \n" +"Welcome to termianl champ!! \n Thank you for visitng our website \n we have also sent you a confirmataion email, please confirm your email address inorder to activate your account. \n\n Thank you"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('signin')

     return render(request, "authentication/signup.html")

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        pass1=request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return render(request, "authentication/index.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials!")
            return redirect('home')

    return render(request,"authentication/signin.html")

def signout(request):
     logout(request)
     messages.success(request,"Logged Out Successfully")
     return redirect('home')

def blog(request):
    return render(request, 'authentication/blog.html')

def cloud(request):
    return render(request, 'authentication/cloud.html')

def  page2(request):
    return render(request,'authentication/page2.html')

# def listing(request):
#     users = User.objects.all