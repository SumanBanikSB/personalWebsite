
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from authentication_app.views import index
from authentication_app.views import test
from students import views
from homework.views import create,show

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',index),
    path('test',test),
    path('create',views.home,name = "createStudent"),
    path('show',views.homeview),
    path('createh',create,name = "homework_create"),
    path('showh',show),

]

