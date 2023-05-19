from rest_framework import serializers
from .models import Movie


# class DecodeSerializer(serializers.ModelSerializer) :

#     class Meta:
#         model = Still
#         fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'