
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from authentication_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',index),

]
