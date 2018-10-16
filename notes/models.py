from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings


# Create your models here.
class Notes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now())
    content = models.TextField(default='<div>...</div>')
