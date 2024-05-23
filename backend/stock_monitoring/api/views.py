
import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Watchlist
from .services import get_stock_data

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@api_view(['POST'])
def register(request):
    data = request.data
    password = data.get('password')
    hashed_password = make_password(password)
    data['password'] = hashed_password

    user = User(username=data['username'], email=data['email'], password=hashed_password)
    user.save()
    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    user = User.objects(email=email).first()
    if user and check_password(password, user.password):
        return Response({'message': 'Login successful', 'username': user.username, 'user_id': str(user.id)}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_to_watchlist(request):
    data = request.data
    user_id = data.get('user_id')
    symbol = data.get('symbol')
    if not user_id or not symbol:
        return Response({'error': 'User ID and Symbol are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    watchlist = Watchlist.objects(user_id=user_id).first()
    if not watchlist:
        watchlist = Watchlist(user_id=user_id, stocks=[])
    
    stock_data = get_stock_data(symbol)
    if not stock_data:
        return Response({'error': 'Failed to fetch stock data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    watchlist.stocks.append(symbol)
    watchlist.save()
    return Response({'message': 'Stock added to watchlist', 'price': stock_data['price']}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_watchlist(request):
    user_id = request.query_params.get('user_id')
    if not user_id:
        return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    watchlist = Watchlist.objects(user_id=user_id).first()
    if not watchlist:
        return Response({'error': 'Watchlist not found'}, status=status.HTTP_404_NOT_FOUND)
    
    stock_data = [get_stock_data(symbol) for symbol in watchlist.stocks]
    return Response(stock_data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_from_watchlist(request, symbol):
    user_id = request.query_params.get('user_id')
    if not user_id:
        return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    watchlist = Watchlist.objects(user_id=user_id).first()
    if not watchlist:
        return Response({'error': 'Watchlist not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if symbol in watchlist.stocks:
        watchlist.stocks.remove(symbol)
        watchlist.save()
        return Response({'message': 'Stock removed from watchlist'}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({'error': 'Symbol not found in watchlist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def stock_quote(request):
    symbol = request.query_params.get('symbol')
    if not symbol:
        return Response({'error': 'Symbol is required'}, status=400)
    data = get_stock_data(symbol)
    if data:
        return Response(data)
    return Response({'error': 'Failed to fetch data'}, status=500)

@api_view(['GET'])
def company_profile(request):
    symbol = request.query_params.get('symbol')
    if not symbol:
        return Response({'error': 'Symbol is required'}, status=400)
    data = get_company_profile(symbol)
    if data:
        return Response(data)
    return Response({'error': 'Failed to fetch data'}, status=500)

@api_view(['GET'])
def get_stocks(request):
    user_id = request.query_params.get('user_id')
    if not user_id:
        return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)

    watchlist = Watchlist.objects(user_id=user_id).first()
    if not watchlist:
        return Response({'error': 'Watchlist not found'}, status=status.HTTP_404_NOT_FOUND)

    stock_data = []
    for stock in watchlist.stocks:
        data = get_stock_data(stock)
        if data:
            stock_data.append(data)
        else:
            return Response({'error': f'Failed to fetch data for {stock}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(stock_data, status=status.HTTP_200_OK)
