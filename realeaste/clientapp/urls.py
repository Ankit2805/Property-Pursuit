from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard_0,name='dashboard_0'),
    path('login/', views.login_0, name='login_0'),
    path('register/', views.register_0, name='register_0'),
    path('logout/',views.logout,name='logout_0'),
]
