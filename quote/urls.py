from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints, name='endpoints'),
    path('quotes/', views.get_quotes, name='quotes'),
    path('quotes/random/', views.random_quotes, name='random-quote'),
    path('quotes/search', views.search_quotes, name='search'),

    path('create/', views.QuoteCreateView.as_view(), name='create'),
    path('quotes/<str:pk>/', views.get_quote_detail, name='quote-details'),
]