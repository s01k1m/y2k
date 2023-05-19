from rest_framework import serializers
from stills.models import Still


class DecodeSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Still
        fields = '__all__'