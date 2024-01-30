from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class account(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=300, blank=True)
    last_name = models.CharField(max_length=300, blank=True)
    avatar = models.ImageField(upload_to='user_profile/', default='avatar.jpg', blank=True)
    adress = models.TextField(blank=True)
    post_code = models.CharField(max_length=9, blank=True)

    def __str__(self):
        return self.user.username
