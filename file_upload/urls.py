from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='file_upload_home'),
        # path('home', views.home, name = 'home'), # for login
        ] 

