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
<<<<<<< HEAD

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
=======
        


# 무비 아이디로 스틸 찾는 중계테이블
# class MovieStillSerializer(serializers.ModelSerializer):
#     stills = StillSerializer(many=True, read_only=True)
    
#     class Meta:
#         model = Movie
#         fields = '__all__'
>>>>>>> 190f083782c9e69502e3dc0a86dcc551849fb6a0
