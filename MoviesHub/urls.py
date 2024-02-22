from django.urls import path
from MoviesHub import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path("search/", views.search, name="EbookAppSearch"),
    path("moviesview/<int:myid>", views.moviesView, name="moviesView"),
    path("category/<int:category_id>", views.category, name="category"),
    path("request-a-movie",views.MovieRequest,name="MovieRequest"),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    

    
]

