from django.urls import path
from movies.api import views


urlpatterns = [
    # path('list/', views.movie_list, name="movie-list"),
    # path('<int:pk>/', views.movie_details, name='movie-detail')
    path('list/', views.MovieList.as_view(), name="movie-list"),
    path('<int:pk>/', views.MovieDetail.as_view(), name='movie-detail')

]