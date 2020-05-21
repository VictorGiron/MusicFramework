from django.urls import path
from songs import views

urlpatterns = [
    path('songs/', views.ListCreateSong.as_view(), name='songs'),
    path('songs/<int:pk>/', views.RetrieveUpdateDestroySong.as_view(), name='song'),

    path('favorite/', views.ListCreateFavoriteSong.as_view(), name='favoritesongs'),
    path('favorite/<int:pk>/', views.RetrieveUpdateDestroyFavoriteSong.as_view(), name='favoritesong'),
]
