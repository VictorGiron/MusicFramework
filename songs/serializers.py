from rest_framework.serializers import ModelSerializer, SerializerMethodField
from songs.models import Song, FavoriteSong
from users.models import User

#User
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

#Song
class SongSerializer(ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'

class SongDetailSerializer(ModelSerializer):
    user = SerializerMethodField()

    class Meta:
        model = Song
        fields = ['id', 'name', 'artist', 'album', 'duration', 'user']

    def get_user(self, song):
        user = FavoriteSong.objects.filter(songs__id=song.id)

        users = [favorite_song.users for favorite_song in user]

        return UserSerializer(instance=users, many=True).data

#FavoriteSong
class FavoriteSongSerializer(ModelSerializer):
    class Meta:
        model = FavoriteSong
        fields = '__all__'

class FavoriteSongDetailSerializer(ModelSerializer):
    class Meta:
        model = FavoriteSong
        fields = ['id', 'songs', 'songs']

