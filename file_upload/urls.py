from django.urls import path
from . import views

urlpatterns = [
        path('', views.ProfileView.as_view(), name='file_upload_home'),
        path('get_excel', views.get_excel, name='get_excel'),
        # path('home', views.home, name = 'home'), # for login
        ]