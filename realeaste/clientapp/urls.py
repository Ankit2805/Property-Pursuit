from django.urls import path
from  . import views

urlpatterns = [
    path('',views.landing,name='landingpage'),
    path('contact/',views.contact,name='contact')

]
