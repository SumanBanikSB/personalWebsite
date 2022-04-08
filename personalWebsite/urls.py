
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from authentication_app.views import index
from authentication_app.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',index),
    path('test',test),

]

