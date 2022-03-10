from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Song(models.Model):
    songArtist = models.CharField(max_length=255,primary_key=True)
    song = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255)

    def __str__(self):
        return self.song

class Rating(models.Model):
    #id is primary key
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return '{}->{}'.format(self.song,self.rating)

class Album(models.Model):
    # "albumArtist","albumTitle","artistName", "genre", "yearProduced", "explicit"
    albumArtist = models.CharField(max_length=255, primary_key=True) # composite field of both song album title and artist name
    albumTitle = models.CharField('Album', max_length=255)   
    artistName = models.CharField('Artist', max_length=255) # not a foreign key since artist should not be deleted if album is deleted from other table (e.g. songs)
    genre = models.CharField('Genre', max_length=255)
    yearProduced = models.IntegerField('Year Released')
    explicit = models.BooleanField('Explicit')

    def __str__(self):
        return self.albumTitle
    def return_info(self):
        return {
            'title': self.albumTitle,
            'artist': self.artistName,
            'genre': self.genre,
            'year released': self.yearProduced,
            'explicit': self.explicit,
        }
#sql query returns 2 extra fields