from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Photo
from .forms import ContactForm


def index(request):
    photos = Photo.objects.all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('myprofile:index') + '?sent=1#contact')
    return render(request, 'myprofile/index.html', {
        'photos': photos,
        'form': form,
    })
