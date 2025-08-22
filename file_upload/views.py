from django.shortcuts import render

from . signal_generator import generate_random_signal_plot

from django.contrib.auth import authenticate, login, logout


from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from .forms import csv_upload_form

def file_upload_home(request):
        # # print()
        if not request.user.is_authenticated:
                return HttpResponseRedirect(reverse("login"))
        else:
                try:
                        plot_for_front = generate_random_signal_plot()
                        # form = csv_upload_form()
                        return render(request, 'file_upload/index.html', {
                        'var1': 'var_from_front',
                        'form': csv_upload_form,
                        'plot': plot_for_front,
                        })
                except:
                        print('--->- def index exception')
                        return render(request, 'file_upload/index.html',
                                      {
                        'var1': 'var_from_front',
                        'form': csv_upload_form,
                        })