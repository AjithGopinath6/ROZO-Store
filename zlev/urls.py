from django.urls import path
from zlev import views


urlpatterns = [
    path('', views.home, name='home'),
]