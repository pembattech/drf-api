from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Drink
from .serializers import DrinkSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def drink_list(request):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        
        drink_serializer = DrinkSerializer(drinks, many=True)

        return Response(drink_serializer.data)

    if request.method == 'POST':
        drink_serializer = DrinkSerializer(data = request.data)
        if drink_serializer.is_valid():
            drink_serializer.save()
            
            return Response(drink_serializer.data, status = status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detial(request, id):
    try:
        drink = Drink.objects.get(id = id)
    except Drink.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        drink_serializer = DrinkSerializer(drink)
        return Response(drink_serializer.data)

    if request.method == 'PUT':
        drink_serializer = DrinkSerializer(drink, data= request.data)
        if drink_serializer.is_valid():
            drink_serializer.save()
            return Response(drink_serializer.data)

        return Response(drink_serializer.erros, status = status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        drink.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)