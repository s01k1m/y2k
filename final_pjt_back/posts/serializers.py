from rest_framework import serializers
from stills.models import Still, Movie


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Still
        fields = ['still_image', 'still_color', 'movie_id', 'user']

    # #  Django REST Framework에서 사용되는 Serializer Method Field의 예시입니다. 이 메서드는 해당 필드가 시리얼라이저로 직렬화되거나 역직렬화될 때 호출되는 함수입니다. 위의 예시는 현재 사용자를 반환하는 함수로, 필드에 현재 요청의 사용자를 할당하는 데 사용됩니다
    # def __call__(self, serializer_field):
    #     return serializer_field.context['request'].user


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
