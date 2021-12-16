from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from app1.serializers import PersonSerializer,BooksSerializer
from app1.models import Person,Books
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.


@api_view(["GET"])
def helloWorld(request):
    return Response({
        "message": "hello world"
    }, status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getAllPerson(request):
    data =  PersonSerializer(Person.objects.all(),many=True).data
    return Response(data, status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getAllBooks(request):
    data =  BooksSerializer(Books.objects.all(),many=True).data
    return Response(data, status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createBook(request):
    request_body = request.data
    booksSerializer = BooksSerializer(data=request_body)
    if booksSerializer.is_valid():
        booksSerializer.save()
        return Response({"message":"success"}, status.HTTP_201_CREATED)
    else:
        return Response({"message":str(booksSerializer.errors)},status.HTTP_400_BAD_REQUEST)
    return Response(data, status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def updateBook(request):
    request_body = request.data
    obj = Books.objects.get(id=request_body["id"])
    obj.author_name = request_body["author_name"]
    obj.book_name = request_body["book_name"]
    obj.gener = request_body["gener"]
    obj.publication = request_body["publication"]
    obj.issued_to =  User.objects.get(id=request_body["issued_to"]) 

    obj.save()
    
    return Response({"message":"success"}, status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def deleteBook(request):
    request_body = request.data
    obj = Books.objects.get(id=request_body["id"])

    obj.delete()
    
    return Response({"message":"success"}, status.HTTP_200_OK)
