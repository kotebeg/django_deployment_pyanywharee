from django.urls import path
from . import views

urlpatterns = [
        path('apps_dashboard', views.apps_dashboard, name = 'apps_dashboard'),
        path('logout', views.logout_view, name = 'logout'),
        path('register', views.register_view, name = 'register'),
        path('', views.login_view, name = 'login'),
        ]
