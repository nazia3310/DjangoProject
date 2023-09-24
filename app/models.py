from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to="file/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    