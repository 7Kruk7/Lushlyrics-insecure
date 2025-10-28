from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.default), name='default'),
    path("playlist/", login_required(views.playlist), name='your_playlists'),
    path("search/", login_required(views.search), name='search_page') 
]