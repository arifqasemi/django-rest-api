from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from currency.currencyserializer import CurrencySerializer
from currency.models import Currency
from rest_framework import status
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.data.get('token')  

        if not token:
            return None

        try:
            token_obj = Token.objects.get(key=token)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        return token_obj.user, token_obj 
    
class CurrencyView(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        currencies = Currency.objects.all()
        currency = CurrencySerializer(currencies,many=True,context={'request': request})
        return Response(currency.data)
    
    
    
    
    
    
class AddCurrency(APIView):
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        currencies = Currency.objects.all()
        currency = CurrencySerializer(currencies,many=True,context={'request': request})
        return Response(currency.data)
    
    def post(self, request):
        serializer = CurrencySerializer(data=request.data)

        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=400)
    
    
class UpdateCurrency(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request,pk):
        
        currency = Currency.objects.get(pk=pk)
        currency_serializer = CurrencySerializer(currency,context={'request': request})
        return Response(currency_serializer.data)
    def post(self,request,pk):
        # currency_id = request.data['id']
        # currency = Currency.objects.get(pk=currency_id)
        currency = Currency.objects.get(pk=pk)
        currency_serializer = CurrencySerializer(instance=currency, data=request.data)
        if currency_serializer.is_valid():
            currency_serializer.base = request.data['base']
            currency_serializer.counter = request.data['counter']
            currency_serializer.rate = request.data['rate']
            currency_serializer.save()
            return Response(currency_serializer.data, status=202)
        else:
            return Response(currency_serializer.errors, status=400)
        
        
        
class DeleteCurrency(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            currency = Currency.objects.get(pk=pk)
        except Currency.DoesNotExist:
            return Response({'error': 'Currency not found'}, status=status.HTTP_404_NOT_FOUND)

        currency.delete()
        return Response({'message': 'Currency deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

