from django.shortcuts import render


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


def apps_dashboard(request):
        if request.user.is_authenticated:
                return render(request, 'authentication/apps_dashboard.html')
        else:
                return HttpResponseRedirect(reverse("login"))

def logout_view(request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
        if request.method == "POST":
                username = request.POST['floatingInput_name']
                password = request.POST['floatingPassword_name']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                        login(request, user)
                        return HttpResponseRedirect(reverse("apps_dashboard"))
                else:
                        return render(request, "authentication/login.html", {
                                "login_message": "invalid credentials"
                        })
        else:
                return render(request, 'authentication/login.html')

def register_view(request):
        if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                        user = form.save()
                        login(request, user)
                        return HttpResponseRedirect(reverse("apps_dashboard"))
                else:
                        return render(request, "authentication/register.html", {
                                "form": form
                        })
        else:
                form = UserCreationForm()
                return render(request, "authentication/register.html", {
                        "form": form
                })
