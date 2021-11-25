from django.urls import path

from . import views

app_name = 'tweets'
urlpatterns = [
    path('', views.index, name='index'),
    path('my-tweets/', views.user_tweets, name='user_tweets'),
]
