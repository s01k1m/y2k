from rest_framework import serializers
from .models import Movie, Still


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class StillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Still
        fields = '__all__'