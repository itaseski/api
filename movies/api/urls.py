from django.urls import path
from movies.api import views


urlpatterns = [
    # path('list/', views.movie_list, name="movie-list"),
    # path('<int:pk>/', views.movie_details, name='movie-detail'),
    path('list/', views.WatchListAV.as_view(), name="movie-list"),
    path('<int:pk>/', views.WatchDetail.as_view(), name='movie-detail'),
    path('stream/', views.StreamPlatformList.as_view(), name="platform-list"),
    path('stream/<int:pk>/', views.StreamPlatformDetail.as_view(), name='platform-detail')

]