from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
]
# link/first_app/ for viewing that page