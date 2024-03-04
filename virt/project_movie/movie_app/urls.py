from django.urls import path
from movie_app import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),    
    path("details/<int:id>", views.details, name="detail")    
]
