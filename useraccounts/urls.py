from django.urls import path

from . import views

app_name = 'useraccounts'
urlpatterns = [
    path('results/<search_string>/', views.search_results, name='search_results'),
    path('follow/<useraccount_id>/', views.follow, name='follow'),
    path('unfollow/<useraccount_id>/', views.unfollow, name='unfollow'),
]