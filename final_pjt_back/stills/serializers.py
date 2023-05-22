from rest_framework import serializers
from .models import Movie, Still, Comment

# movie detail
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
# still datail
class StillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Still
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'