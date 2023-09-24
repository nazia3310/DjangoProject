from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from app.models import File
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "login.html")
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            messages.success(request, "Welcome back "+user.first_name+"!!")
            login(request, user)
            return redirect("dashboard")

        else:
            messages.error(request, "Username or password is incorrect!!")
            return redirect("login")
        

class SignUpPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, "signup.html")
    
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get("fname")
        last_name = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re-enter-password")

        if password == re_password and not User.objects.filter(username=username, email=email, is_active=True):
            user = User()
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "User added successfully!!")
            return redirect("dashboard")
        
        else:
            messages.error(request, "Authentication failed!!")
            return redirect("signup")


class Dashboard(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            msg = kwargs.get("logout")
            if msg == "logout":
                logout(request)
                return redirect("login")
            
            return render(request, "dashboard.html", {
                'files': File.objects.filter(user=request.user)
            })
        else:
            return redirect("login")
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            file = request.FILES.get("file")
            f = File()
            f.file = file
            f.user = request.user
            f.save()
            messages.success(request, "File Uploaded Successfully!!")
            return redirect("dashboard")
        
        else:
            return redirect("login")
        
class FileDelete(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            file_id = kwargs.get("id")
            try:
                file = File.objects.get(id=file_id, user=request.user)
                file.delete()
                messages.success(request, "File Deleted Successfully!!")
                return redirect("dashboard")
            except:
                return redirect("dashboard")
        else:
            return redirect("login")