from django.urls import path
from MoviesHub import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path("search/", views.search, name="Search"),
    path("moviesview/<slug:slug>", views.moviesView, name="moviesView"),
    path("category/<slug:slug>", views.category, name="category"),
    path("request-a-movie",views.MovieRequest,name="MovieRequest"),
    path('disclaimer/', views.disclaimer, name='disclaimer'),



]

