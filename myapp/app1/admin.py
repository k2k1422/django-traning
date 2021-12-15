from django.contrib import admin
from app1.models import Person
# Register your models here.


@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = (
        "id", "first_name","last_name","age"
    )
