from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [
    path('', views.AlbumLV.as_view(), name='index'), # /photo/
    path('album', views.AlbumLV.as_view(), name='album_list'), # /photo/album/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'), #/photo/album/99/
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'), #/photo/photo/99/
    path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'), #/photo/album/add/
    path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'), #/photo/album/change/
    path('album/<int:pk>/update/', views.AlbumPhotoUV.as_view(), name='album_update'), #/photo/album/99/update/
    path('album/<int:pk>/delete/', views.AlbumDelV.as_view(), name='album_delete'), #/photo/album/99/delete/
    path('photo/add/', views.PhotoCV.as_view(), name='photo_add'), #/photo/photo/add/
    path('photo/change/', views.PhotoChangeLV.as_view(), name='photo_change'), #/photo/photo/change/
    path('photo/<int:pk>/update/', views.PhotoUV.as_view(), name='photo_update'), #/photo/photo/99/update/
    path('photo/<int:pk>/delete/', views.PhotoDelV.as_view(), name='photo_delete'), #/photo/photo/99/delete/
]