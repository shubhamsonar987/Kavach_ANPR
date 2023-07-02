from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


#@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        # Retrieve uploaded file from POST request
        uploaded_file = request.FILES.get('my_video_file')
# Check if file was uploaded
                # Open file in binary write mode and write uploaded data to file
        if uploaded_file is not None:
            # Open file in binary write mode and write uploaded data to file
            with open('media/{}'.format(uploaded_file.name), 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # Redirect back to the index page
        return redirect('index')
    else:
           # Render the index template
        return render(request, 'index.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                   # messages.info(request, 'Email Taken')
                messages.info(request, 'User already present')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                # messages.info(request,'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()

                # login

                return redirect('signup')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def contact(request):
    return render(request, 'contact.html') 

def team(request):
    return render(request, 'team.html')

def feature(request):
    return render(request,'features.html')