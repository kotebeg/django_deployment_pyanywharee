from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challange = {
    'january':'from january',
    'february':'from february',
    'march':'from march',
    'april':'from april',
    'may':'from may',
    'june':'from june',
    'july':'from july',
    'august': 'from august',
    'september':'from september',
    'octomber':'from octomber',
    'november': None,
    'december':'from december from december from december',
}

def index(request):
    list_items = ''
    month_list = list(monthly_challange.keys())
    # print(month_list)
    return render(request, 'app26/index.html', {
        'month_list': month_list
    })

def get_month_by_id(request, month):
        month_list = list(monthly_challange.keys())
        if 1 <= month <=12:
            choosen_month = month_list[month]
            redirect_path = reverse('month-challange', args = [choosen_month] )
            return HttpResponseRedirect(redirect_path)
        else:
            error_path = reverse('error-path')
            return HttpResponseRedirect(error_path)
            

def print_in_dtl():
    return 'print from function, throught DTL'


def get_month_by_name(request, month):
        try:
            challenge_text = monthly_challange[month]
            return render(request, 'app26/app26.html', {
                'text': challenge_text,
                'month_name': month,
                'py_funct': print_in_dtl()
            })
        except:
            raise Http404()


