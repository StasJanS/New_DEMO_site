from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название фильма')
    genre = models.ManyToManyField('Genre', verbose_name='Жанр фильма')
    country = models.ManyToManyField('Country', verbose_name='Страна')
    year = models.ForeignKey('Year', on_delete=models.CASCADE, verbose_name='Год выпуска')
    image = models.ImageField(upload_to='image/media/')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Фильмы'
        verbose_name = 'Фильм'
        ordering = ['title']


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'


class Country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Страны'
        verbose_name = 'Страна'


class Year(models.Model):
    date = models.CharField(max_length=6)

    def __str__(self):
        return self.date

    class Meta:
        verbose_name_plural = 'Года'
        verbose_name = 'Год'
