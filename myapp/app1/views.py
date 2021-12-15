from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from app1.serializers import PersonSerializer
from app1.models import Person

# Create your views here.


@api_view(["GET"])
def helloWorld(request):
    return Response({
        "message": "hello world"
    }, status.HTTP_200_OK)

@api_view(["GET"])
def getAllPerson(request):
    data =  PersonSerializer(Person.objects.all(),many=True).data
    return Response(data, status.HTTP_200_OK)
