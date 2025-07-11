from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dealerapp/',include('dealerapp.urls')),
    path('adminapp/',include('adminapp.urls')),
    path('clientapp/',include('clientapp.urls')),
    path('',include(('landingpage.urls'))),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
