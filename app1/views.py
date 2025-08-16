from django.shortcuts import render


from django.contrib.auth import authenticate, login, logout


from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


def index(request):
        try:
                return render(request, 'app1/index.html', {
                'var1': 'var_from_front'
                })
        except:
                print('--->- def index exception')
                return render(request, 'app1/index.html')


def home(request):
        if request.method == "POST":
                # print('--> POST')
                # print('-->', request.POST, type(request.POST))
                username = request.POST['floatingInput_name']
                password = request.POST['floatingPassword_name']
                print(username, password)
                # print('-->', request.POST['floatingInput_name'])
                # print('-->', request.POST['floatingPassword_name'])

                user = authenticate(request, username = username, password=password)


                if user is not None:

                    # user = authenticate(request, username = usr_nm, password = usr_ps)
                    return render(request, 'app1/home.html')
                else:
                    # print('---> wrong credintionals')
                    return render(request, "app1/index.html", {
                    "login_message":"invalid credentials"
            })
        else:
                print('-->', request.method)
                return render(request, 'app1/home.html')
