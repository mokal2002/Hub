from django.contrib.sitemaps import Sitemap
# from django.db.models.base import Model

# from django.contrib.sitemaps.views import sitemap
from django.urls import reverse
from .models import MovieCard
class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = "daily"

    def items(self):
        return [
            'Home',
            'disclaimer',
            'MovieRequest',
        ]


    def location(self,item):
        return reverse(item)

class MovieCardSitemap(Sitemap):
    priority = 0.8
    changefreq = "daily"

    def items(self):
        return MovieCard.objects.all().order_by('-pub_date')

    def location(self, obj):
        # Assuming you have a detail view for MovieCard objects named 'movie_detail'
        return reverse('movie_detail', args=[obj.m_slug])



