from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_quotes, name='quotes'),
    path('random/', views.random_quotes, name='random-quote'),
]