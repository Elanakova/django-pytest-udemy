from rest_framework import serializers
from .models import Company


# django model to json
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "status", "last_update", "application_link", "notes"]
