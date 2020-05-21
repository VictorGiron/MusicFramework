from django.urls import path
from users import views

urlpatterns = [
    path('', views.ListCreateUser.as_view(), name='users'),
    path('<int:pk>/', views.RetrieveUpdateDestroyUser.as_view(), name='user'),
]
