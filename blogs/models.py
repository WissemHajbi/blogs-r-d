from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class blog(models.Model):
    
    id = models.AutoField(primary_key=True)
    creator = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=5000)
    created_time = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title[:100]+"..." if len(self.title) > 100 else self.title
    
class user(models.Model):

    genders = (
        ('m', 'male'),
        ('f', 'female'),
    )

    profile_picture_numbers = (
        ("['1']", '1'),
        ("['2']", '2'),
        ("['3']", '3'),
        ("['4']", '4'),
        ("['5']", '5'),
        ("['6']", '6'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    username = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=genders)
    started_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username