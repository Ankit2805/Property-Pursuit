from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('manage-details/',views.property_manage_details_2,name='manage-details'),
    path(r'^delete_property/(?P<id>[0-9]+)/$', views.delete_property_2, name='delete_property_2'),
    path('show/<int:id>',views.showdetails_2,name='show-details'),
    path('profile',views.profile,name='profile-2'),
    path('bookings',views.booking_history,name='booking_2'),
    path('logout',views.logout,name='logout-2'),
]
