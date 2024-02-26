from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index,name='index'),
    path('profile/', views.profile, name='profile'),
    path('property_details/<int:id>', views.property_details, name='property_details'),
    path('properties/', views.properties, name='properties'),
    path('buy/', views.buy, name='buy'),
    path('view_list/', views.view_list, name='view_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('another_view/', views.another_view, name='another_view'),
    path('sendrequest/<int:id>/', views.sendrequest, name='sendrequest'),
    path('login/', views.login_0,name='login_0'),
    path('register/', views.register_0,name='register_0'),
    path('logout',views.logout,name='logout_0'),
]