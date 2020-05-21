from django.contrib import admin
from songs.models import FavoriteSong, Song
# Register your models here.
admin.site.register(FavoriteSong)
admin.site.register(Song)
