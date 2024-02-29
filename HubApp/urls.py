from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from MoviesHub.sitemap import MovieCardSitemap,StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from MoviesHub.views import moviesView

sitemaps = {
    'Movies': MovieCardSitemap,
    'Static': StaticViewSitemap,
}
admin.site.site_header = 'MoviesHub'
admin.site.site_title = 'MoviesHub'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MoviesHub.urls')),
    path('moviesview/<slug>', moviesView, name='movie_detail'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
