from rest_framework import serializers
from mock_api_app.models import Person,Student
class personSerializers(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'