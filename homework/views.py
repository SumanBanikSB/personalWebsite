from django.shortcuts import render
from .forms import homeworkForms
from django.http import HttpResponseRedirect
from .models import Homework

# Create your views here.

def create(request):
    template = 'homework_create.html'
    content = dict()
    content['form'] = homeworkForms()
    if request.method == 'POST':
        form = homeworkForms(request.POST)
        if form.is_valid():
            print("Homework saved")
            form.save()
            return HttpResponseRedirect('/show')
    return render(request,template,content)

    
def show(request):
    template = 'homework_show.html'
    content = dict()
    data = Homework.objects.all()
    content['data'] = data
    print(content)
    return render(request,template,content)

