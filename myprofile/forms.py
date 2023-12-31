from django import forms

from .models import Myprofile


class MyprofileForm(forms.ModelForm):
    class Meta:
        model = Myprofile
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(),
            'content': forms.Textarea()
        }