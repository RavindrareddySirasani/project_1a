from .models import Employee
from rest_framework import serializers

class Emp_serialiser(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"