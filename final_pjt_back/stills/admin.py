from django.contrib import admin
from .models import Movie
from .models import Still


admin.site.register(Movie)
admin.site.register(Still)