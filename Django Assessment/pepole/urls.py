"""
URL configuration for society_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Register, name='Register'),
    path('otp/', views.otp, name='otp'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('back/', views.back, name='back'),
    path('members/', views.members, name='members'),
    path('details/<int:pk>', views.details, name='details'),
    path('show_notice/', views.show_notice, name='show_notice'),
    path('create_notice/', views.create_notice, name='create_notice'),
    path('watchmen/', views.watchmen, name='watchmen'),
    path('add_watchmen/', views.add_watchmen, name='add_watchmen'),
    path('Watchmen_details/<int:pk>', views.Watchmen_details, name='Watchmen_details'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('event/', views.event, name='event'),
    path('add_event/', views.add_event, name='add_event'),
    path('Event_details/<int:pk>', views.Event_details, name='Event_details'),
]
