from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import api_views

app_name = 'api'

urlpatterns = [
    path('auth/token/', obtain_auth_token, name='api_token'),
    path('signals/generate/', api_views.GenerateSignalView.as_view(), name='api_signal_generate'),
    path('signals/upload/', api_views.UploadSignalView.as_view(), name='api_signal_upload'),
]
