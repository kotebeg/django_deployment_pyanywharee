from django.shortcuts import render


# from django.contrib.auth import authenticate, login, logout


from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect



def table_file_upload_index(request):
    if request.user.is_authenticated:
            return render(request, 'table_file_upload/home.html', {
            'var1': 'var_from_front'
            })
    else:
            return HttpResponseRedirect(reverse("login"))