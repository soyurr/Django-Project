from django.contrib import admin
from django.urls import path,include
from bookmark import views
from mysite.views import HomeView, BotView
from django.conf.urls.static import static
from django.conf import settings
from mysite.views import UserCreateView, UserCreateDoneTV


urlpatterns = [
    # path('',views.start),  #views의 start 함수를 실행하라
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/register/',UserCreateView.as_view(),name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    path('',HomeView.as_view(), name='home'), #아무것도 없다면 홈 보여주도록 
    path('bookmark/',include('bookmark.urls')),
    path('blog/',include('blog.urls')),
    path('polls/',include('polls.urls')),
    path('photo/',include('photo.urls')),
    path('chatbot/', BotView.as_view(), name='chatbot'),
    path('core/', include('core.urls')),
    
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#리스트 속에 하나의 아이템으로 경로를 주므로 콤마 필요
