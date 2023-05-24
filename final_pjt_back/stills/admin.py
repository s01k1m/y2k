from django.contrib import admin
from .models import Movie
from .models import Still
from .models import Collection

admin.site.register(Movie)
admin.site.register(Still)
admin.site.register(Collection)