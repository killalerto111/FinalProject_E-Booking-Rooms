from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('form/', views.form_view, name='form'),
    path('booking_list/', views.booking_list, name='booking_list'),
    path('api/events/', views.booking_events, name='booking_events'),
]