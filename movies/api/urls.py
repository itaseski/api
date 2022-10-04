from django.urls import path
from movies.api import views


urlpatterns = [
    # path('list/', views.movie_list, name="movie-list"),
    # path('<int:pk>/', views.movie_details, name='movie-detail'),
    path('list/', views.WatchListAV.as_view(), name="watchlist-list"),
    path('<int:pk>/', views.WatchDetail.as_view(), name='watchlist-detail'),
    path('stream/', views.StreamPlatformAV.as_view(), name="streamplatform-list"),
    path('stream/<int:pk>/', views.StreamPlatformDetail.as_view(), name='streamplatform-detail')

]