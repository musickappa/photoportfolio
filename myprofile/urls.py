from django.urls import path

# views.pyからboardを呼び出す
from .views import myprofile

app_name = 'myprofile'

urlpatterns = [
    path('', myprofile, name='myprofile'),
]