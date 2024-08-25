from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:month>', views.get_month_by_id),
    path('<str:month>', views.get_month_by_name, name = 'month-challange'),
] 

