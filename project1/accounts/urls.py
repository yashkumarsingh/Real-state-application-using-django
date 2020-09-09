from django.urls import path

from . import views

urlpatterns = [
    path('Login',views.Login, name='Login'),
    path('Register',views.Register, name='Register'),
    path('Logout', views.Logout, name='Logout'),
    path('Dashboard', views.Dashboard, name='Dashboard'),
]