from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from songs.models import FavoriteSong, Song
from songs.serializers import SongSerializer, SongDetailSerializer, FavoriteSongSerializer, FavoriteSongDetailSerializer

#song
class ListCreateSong(ListCreateAPIView):
    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SongDetailSerializer
        elif self.request.method == 'POST':
            return SongSerializer

class RetrieveUpdateDestroySong(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SongDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return SongSerializer

#FavoriteSong
class ListCreateFavoriteSong(ListCreateAPIView):
    queryset = FavoriteSong.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FavoriteSongDetailSerializer
        elif self.request.method == 'POST':
            return FavoriteSongSerializer

class RetrieveUpdateDestroyFavoriteSong(RetrieveUpdateDestroyAPIView):
    queryset = FavoriteSong.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FavoriteSongDetailSerializer
        elif self.request.method == 'PATCH' or self.request.method == 'PUT':
            return FavoriteSongSerializer

