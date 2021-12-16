from django.contrib import admin
from app1.models import Person,Books
# Register your models here.


@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = (
        "id", "first_name","last_name","age"
    )

@admin.register(Books)
class Books(admin.ModelAdmin):
    list_display = (
        "id", "book_name","author_name","gener","publication","issued_to",
    )
