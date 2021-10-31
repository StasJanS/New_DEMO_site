from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import all_kino, country_kino, genre_kino, year_kino, country, genre, year, movie, add_kino

# app_name = 'app_kino'
urlpatterns = [
                  path('', all_kino, name='all_kino'),
                  path('country_kino/', country_kino, name='country_kino'),
                  path('genre_kino/', genre_kino, name='genre_kino'),
                  path('year_kino/', year_kino, name='year_kino'),
                  path('add_kino/', add_kino, name='add_kino'),
                  path('country/<int:id>/', country, name='country'),
                  path('genre/<int:id>/', genre, name='genre'),
                  path('year/<int:id>/', year, name='year'),
                  path('movie/<str:title>', movie, name='movie'),
                  path('add_kino/', add_kino, name='add_kino'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
