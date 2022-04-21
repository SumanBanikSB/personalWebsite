from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Student


def home(request):
    template = 'home.html'
    content = dict()
    content['form'] = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print("This is happening")
            form.save()
            return HttpResponseRedirect('/show')
    return render(request,template,content)

def homeview(request):
    # this view will deal with only showing the students
    template = 'base.html'
    content = dict()
    data = Student.objects.all()
    # data.save()
    content['data'] = data
    # print(content['data'])
    for key in content:
        print(content[key])
    return render(request,template,content)

