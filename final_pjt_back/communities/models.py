from django.db import models
from django.conf import settings
from stills.models import Still

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    still = models.ForeignKey(Still, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent  = models.ForeignKey(
        'self', 
        on_delete   =models.CASCADE, 
        null        =True, 
        related_name='replies',
    )