from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_quotes, name='quotes'),
    path('random/', views.random_quotes, name='random-quote'),
    path('search/', views.search_quotes, name='search'),

    path('create/', views.QuoteCreateView.as_view(), name='create'),
]