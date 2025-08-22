from django.urls import path
from . import views

urlpatterns = [
        path('', views.table_file_upload_index, name='table_file_upload_index'),
        # path('home', views.home, name = 'home'), # for login
        ] 

