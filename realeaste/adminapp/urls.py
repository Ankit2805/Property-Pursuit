from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('manage-details/',views.property_manage_details_2,name='manage-details'),
    path('show/<int:id>',views.showdetails_2,name='show-details'),
    path('edit/<int:id>',views.edit_property_2,name='edit-details'),
    path('update-details/<int:id>',views.update_property_2,name='update-details'),
    path(r'^delete-property/(?P<id>[0-9]+)/$', views.delete_property_2, name='delete-property'),
    path('profile',views.profile,name='profile-2'),
]
