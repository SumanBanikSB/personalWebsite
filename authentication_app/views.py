from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import InfoForm
from .models import Info
from django.http import HttpResponseRedirect

@login_required
def index(request):
    return render(request,'registration/base.html')


def test(request):
    # print('hi')

    content = dict()
    content['form'] = InfoForm()
    content['check'] = 'Check worked!!'

   
    if request.method == 'POST':
        data = Info.objects.all()
        # print(data)
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        
    return render(request,'test.html',content)

