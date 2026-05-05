from django.urls import path
from .views import index

app_name = 'myprofile'

urlpatterns = [
    path('', index, name='index'),
]
