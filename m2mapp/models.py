from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Song(models.Model):
    user = models.ManyToManyField(User) # ManyToManyField is a list of objects 
    song_name = models.CharField(max_length=50) 
    song_duration = models.IntegerField() 

    def __str__(self):
        return self.song_name

    def written_by(self):
        return ",".join([user.username for user in self.user.all()])