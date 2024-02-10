from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    path('dashboard/',views.dashboard_1,name='dashboard_1'),
    path('add/',views.property_add_details,name='add_details'),
    path('manage/',views.property_manage_details,name='manage_details'),
    path('show/<int:id>',views.showdetails,name='showdetails'),
    path('edit_property/<int:id>', views.edit_property, name='edit_property'),
    path('update_property/<int:id>', views.update_property, name='update_property'),
    path(r'^delete_property/(?P<id>[0-9]+)/$', views.delete_property, name='delete_property'),
    path('booking/',views.booking_history,name='booking_history'),
    path('login/',views.login_1,name='login_1'),
    path('register/',views.register_1,name='register_1'),
    path('contact/',views.contact,name='contact'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
    path('image/',views.upload_image),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
