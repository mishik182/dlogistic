from rest_framework import serializers
from models.models import (
    Accounttype,
)


class AccountTypeSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    createon = serializers.CharField(read_only=True)
    modifiedon = serializers.CharField(read_only=True)
    createbyid = serializers.CharField(read_only=True)
    modifiedbyid = serializers.CharField(read_only=True)

    class Meta:
        model = Accounttype
        fields = [
            'id',
            'createon',
            'modifiedon',
            'createbyid',
            'modifiedbyid',
            'name'
        ]
