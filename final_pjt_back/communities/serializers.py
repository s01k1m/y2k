from rest_framework import serializers
from .models import Comment
from accounts.models import User

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'
    
    def get_username(self, comment):
        username = comment.user.username
        return username