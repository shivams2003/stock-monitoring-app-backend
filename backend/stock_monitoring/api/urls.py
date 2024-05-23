from django.urls import path
from .views import register, login, get_stocks, stock_quote, company_profile, add_to_watchlist, get_watchlist,delete_from_watchlist

urlpatterns = [
    path('auth/register/', register, name='register'),
    path('auth/login/', login, name='login'),
    path('stocks/', get_stocks, name='get_stocks'),
    path('stock_quote/', stock_quote, name='stock_quote'),
    path('company_profile/', company_profile, name='company_profile'),
    path('watchlist/add/', add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/', get_watchlist, name='get_watchlist'),
    path('watchlist/delete/<str:symbol>/', delete_from_watchlist, name='delete_from_watchlist'),
]
