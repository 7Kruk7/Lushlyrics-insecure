from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class playlist_user(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_genre = models.CharField(max_length=100, default='Pop', blank=True)

    '''
    def __str__(self):
        return f'Username = {self.username}, Liked Songs = {list(self.playlist_song_set.all())}'
    '''

    def __str__(self):
        return f'{self.username.username}'  # safe for admin and creation

    def liked_songs(self):
        return list(self.playlist_song_set.all())

class playlist_song(models.Model):
    user = models.ForeignKey(playlist_user, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    song_youtube_id =  models.CharField(max_length=20)
    song_albumsrc = models.CharField(max_length=255)
    song_dur = models.CharField(max_length=7)
    song_channel = models.CharField(max_length=100)
    song_date_added = models.CharField(max_length=12)

    def __str__(self):
      return f'Title = {self.song_title}, Date = {self.song_date_added}'


