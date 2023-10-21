from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dealerapp/',include('dealerapp.urls')),
    path('adminapp/',include('adminapp.urls')),
    path('',include('clientapp.urls')),

]
