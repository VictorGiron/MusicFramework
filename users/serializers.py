from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import User
from songs.models import FavoriteSong, Song
import datetime

from django.db.models import Sum

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SongDetailSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name']

class UserSongSerializer(ModelSerializer):
    songs = SongDetailSerializer()

    class Meta:
        model = FavoriteSong
        fields = ['id', 'duration', 'songs']



class UserDetailSerializer(ModelSerializer):
    song = SerializerMethodField()
    duration_playlist = SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'song', 'duration_playlist']

    def get_duration_playlist(self, user):
        durations = FavoriteSong.objects.filter(users=user).values('songs__duration')
        duration_total = datetime.timedelta(0)
        for duration in durations:
            duration_total += duration['songs__duration']

        return duration_total

    def get_song(self, user):
        song = FavoriteSong.objects.filter(users__id=user.id)

        songs = [favorite_song.songs for favorite_song in song]

        return SongDetailSerializer(instance=songs, many=True).data
5