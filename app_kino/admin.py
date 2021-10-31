from django.contrib import admin

from app_kino.models import Year, Movie, Genre, Country


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'year')
    list_filter = ('year', 'country', 'genre')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Year)
admin.site.register(Country)
# Register your models here.
