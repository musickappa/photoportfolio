from django.shortcuts import render, redirect

# モデルとフォームを呼び出す
from .models import Myprofile
from .forms import MyprofileForm

# 投稿機能と投稿の表示
def myprofile(request):
    template_name = 'myprofile/myprofile.html'
    contents = Myprofile.objects.all()
    form = MyprofileForm(request.POST or None)
    params = {'contents': contents, 'form': form}
    if form.is_valid():
        myprofile = form.save(commit=False)
        myprofile.save()
        return redirect('myprofile:myprofile')
    return render(request, template_name, params)