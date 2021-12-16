from rest_framework import serializers
from app1.models import Person,Books


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = "__all__"

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = "__all__"