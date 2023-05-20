from rest_framework import serializers
from stills.models import Still


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Still
        fields = '__all__'

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user
