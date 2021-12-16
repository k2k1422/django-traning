from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " +self.last_name

class Books(models.Model):
    id = models.AutoField(primary_key=True,editable=False, db_column='book_id')
    author_name = models.CharField(max_length=64,db_column='author_name')
    book_name = models.CharField(max_length=64,default='',db_column='book_name')
    gener = models.CharField(max_length=64,db_column='gener')
    publication = models.CharField(max_length=64,db_column='publication')
    issued_to = models.ForeignKey(User, on_delete=models.CASCADE,db_column='issued_to')

    class Meta:
        db_table = "book"
