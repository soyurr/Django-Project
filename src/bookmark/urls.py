from django.urls import path
from bookmark.views import BookmarkLV,BookmarkDV
from bookmark import views

app_name = 'bookmark' #네임스페이스
urlpatterns = [
    path('',BookmarkLV.as_view(),name='index'), #그냥 입력하면 리스트를 보여주고
    path('<int:pk>/',BookmarkDV.as_view(),name='detail'), #번호를 넘기면 그 번호값에 맞는 것이 상세보기로 나온다

    path('add/', views.BookmarkCreateView.as_view(), name="add",), #/bookmark/add/
    path('change/', views.BookmarkChangeLV.as_view(), name="change",), #/bookmark/change/
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name="update",), #/bookmark/99/update
    path('<int:pk>/delete/', views.BookmarkDeleteView.as_view(), name="delete",), #/bookmark/99/delete
]
