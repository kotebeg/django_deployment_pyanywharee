from django.urls import path
from . import views

urlpatterns = [
        path('apps_dashboard', views.apps_dashboard, name = 'apps_dashboard'),
        path('', views.login_view, name = 'login'), # for login
        ] 
