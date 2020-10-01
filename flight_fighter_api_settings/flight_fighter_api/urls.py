from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index_page, name = 'index'),
    path('player/', views.PlayerView.as_view()),
    path('auth/', views.AuthPlayerView.as_view())
]