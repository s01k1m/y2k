from django.db import models
from django.conf import settings


class Movie(models.Model):
    id = models.AutoField(primary_key=True)            # pk 역할
    movie_id = models.IntegerField()                         # 해당 영화 TMDB id
    movie_title = models.CharField(max_length=20)               # 영화 이름
    overview = models.TextField()
    movie_released_date = models.DateField()                            # 개봉일
    genre = models.CharField(max_length=30, blank=True)               # 장르

    def __str__(self):
        return self.movie_title



class Still(models.Model):

    id = models.AutoField(primary_key=True)                            # pk 역할
    still_image = models.FileField(
        upload_to="stills/", null=False)                               # 스틸컷
    still_color = models.CharField(
        max_length=6, blank=True
        # choices=COLOR_IN_STILL_CHOCIES,
    )                                                                   # 스틸컷 컬러 카테고리
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)       # 무비 id
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='likes')


class Collection(models.Model):
    # pk 역할
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)  # 콜렉션을 만든 유저
    collection_name = models.CharField(
        max_length=20)                                       # 콜렉션 이름
    stills = models.ManyToManyField(
        Still, related_name='stills')                 # 콜렉션에 담기는 여러 스틸컷