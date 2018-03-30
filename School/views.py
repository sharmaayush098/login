from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import View

from django.shortcuts import render, redirect
from django.template import loader

from School.forms import UserForm
from School.models import Subject


def index(request):
    return render(request, "frontpage.html")


def admin(request):
    return render(request, "login_page_admin.html")


def admin_content(request):
    return render(request, "admin_content.html")


def teachers(request):

    return render(request, "login_page_teacher.html")


def parents(request):
    return render(request, "login_page_parents.html")


def about(request):
    return render(request, "About.html")



@csrf_exempt
def store(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        username = User.objects.get(email=email).username

        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
            return HttpResponse("ayush")
        else:
            return HttpResponse("authentication failed")
    else:
        email = request.GET.get("email")
        try:
            username = User.objects.get(email=email).username
            return HttpResponse("User Exist: "+str(username))

        except User.DoesNotExist:
            return HttpResponse("User does not exist")

@csrf_exempt
def registration(request):
    if request.method == "GET":
        return render(request, 'password_validation.html')
    elif request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)

        except:
            user = None
        if user:
            return HttpResponse("already exists")
        else:
            User.objects.create_user(email=email, username=username, first_name=firstname, last_name=lastname,
                                     password=password)
            return HttpResponse("Done")

    else:
        return HttpResponse("Invalid user")

@csrf_exempt
def signup(request):
    if request.method == "GET":
        return render(request, 'login_page_admin.html')
    elif request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse("done")
            else:
                return HttpResponse("No user found")
        except:
            return HttpResponse("none")





