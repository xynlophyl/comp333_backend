from django.contrib import admin

# Register your models here.
from .models import User, Song, Rating, Album

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("username",)
    search_fields = ("username",)

@admin.register(Song)
class SongsAdmin(admin.ModelAdmin):
    list_display = ("song", "artist",)
    search_fields = ("song", "artist",)

@admin.register(Rating)
class RatingsAdmin(admin.ModelAdmin):
    list_display = ("username", "song", "rating",)
    search_fields =  ("username", "song", "rating",)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("albumArtist","albumTitle","artistName", "genre", "yearProduced", "explicit",)
    search_fields = ("albumArtist","albumTitle","artistName", "genre", "yearProduced", "explicit",)


#sql query: album genre