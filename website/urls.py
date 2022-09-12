from django.urls import path
from .views import *

app_name = 'rate'

urlpatterns = [
    path('', home, name='home'),
    path("rate-image", rateImg, name='rate-image')
]