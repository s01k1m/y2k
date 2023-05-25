from rest_framework import serializers
from .models import Movie, Still, Collection

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

# create collection


class CollectionSerializer(serializers.ModelSerializer):
    # 스틸 필드를 빈 상태로 생성하기 위해 allow_empty=True 설정
    stills = StillSerializer(many=True, allow_empty=True, read_only=True)

    class Meta:
        model = Collection
        fields = ('id', 'user', 'collection_name', 'stills')

# 한개의 콜렉션은 여러개의 스틸을 가질 수 있다.


class CollectionsStillSerializer(serializers.ModelSerializer):
    # Stills 데이터가 없어도 collection을 가져오려면 allow_null=True
    stills = StillSerializer(many=True, allow_null=True)
    username = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = ('id', 'user', 'username', 'collection_name', 'stills')

    def get_username(self, collection):
        username = collection.user.username
        return username
