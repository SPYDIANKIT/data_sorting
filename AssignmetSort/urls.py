
from django.urls import path
from .views import *

urlpatterns = [
     path('', upload_file, name='upload_file'),
    path('display/', display_data, name='display_data'),
    path('download/<str:option>/', download_data, name='download_data'),
]