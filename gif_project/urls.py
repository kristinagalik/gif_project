from django.contrib import admin
from django.urls import path
from django.urls import include
from databank_system import views

urlpatterns = [
    path('', include('databank_system.urls')),
    path('admin/', admin.site.urls),
]
