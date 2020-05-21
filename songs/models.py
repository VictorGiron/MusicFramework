from django.db import models
from users.models import User
# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=30)
    duration = models.DurationField()

    def __str__(self):
        return self.name + ', ' + self.artist + '(' + self.album + ')'

class FavoriteSong(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.songs + '(' + self.users + ')'
