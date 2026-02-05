from django.shortcuts import render


from django.contrib.auth import authenticate, login, logout


from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


def apps_dashboard(request):
        if request.user.is_authenticated:
                return render(request, 'authentication/apps_dashboard.html', {
                'var1': 'var_from_front'
                })
        else:
                return HttpResponseRedirect(reverse("login"))

def login_view(request):
        if request.method == "POST":
                # print('--> POST')
                # print('-->', request.POST, type(request.POST))
                username = request.POST['floatingInput_name']
                password = request.POST['floatingPassword_name']
                print(username, password)
                # print('-->', request.POST['floatingInput_name'])
                # print('-->', request.POST['floatingPassword_name'])
                user = authenticate(request, username = username, password=password)

                login(request, user)

                # print('--->',authenticate(request, username = username, password=password))
                print('----<user>',request.user, user)
                print("session key:", request.session.session_key)
                print("is_authenticated:", request.user.is_authenticated)
                print("cookies:", request.COOKIES.keys())
                if user is not None:
                        
                        print('----<>',request.user.is_authenticated)
                        # user = authenticate(request, username = usr_nm, password = usr_ps)
                        return render(request, 'authentication/apps_dashboard.html')
                else:
                        # print('---> wrong credintionals')
                        return render(request, "authentication/login.html", {
                        "login_message":"invalid credentials"
                })
        else:
                print('-->', request.method)
                return render(request, 'authentication/login.html')
