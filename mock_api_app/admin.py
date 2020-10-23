from django.contrib import admin
from mock_api_app.models import Person,Student
# Register your models here.
admin.site.register(Person)
admin.site.register(Student)