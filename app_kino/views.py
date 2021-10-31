from django.shortcuts import render

from .models import Movie, Country, Genre, Year

menu = [{'zagolovok': 'Главная', 'url_name': 'all_kino'},
        {'zagolovok': 'Жанры', 'url_name': 'genre_kino'},
        {'zagolovok': 'Страны', 'url_name': 'country_kino'},
        {'zagolovok': 'Года', 'url_name': 'year_kino'},
        {'zagolovok': 'Добавить', 'url_name': 'add_kino'},
        ]


def all_kino(request):
    all_kino = Movie.objects.all()
    context = {
        'menu': menu,
        'zagolovok': 'Главная',
        'all_kino': all_kino,
    }
    return render(request, 'all_kino.html', context)


def movie(request, title):
    mov = Movie.objects.filter(title=title)
    print(menu)
    context = {
        'menu': menu,
        'mov': mov,
    }
    return render(request, 'movie.html', context)


def country_kino(request):
    country = Country.objects.all()
    context = {
        'menu': menu,
        'zagolovok': 'Страны',
        'country': country,
    }
    return render(request, 'country_kino.html', context)


def genre_kino(request):
    genre = Genre.objects.all()
    context = {
        'menu': menu,
        'zagolovok': 'Жанры',
        'genre': genre,
    }
    return render(request, 'genre_kino.html', context)


def year_kino(request):
    year = Year.objects.all()
    context = {
        'menu': menu,
        'zagolovok': 'Года',
        'year': year,
    }
    return render(request, 'year_kino.html', context)


def country(request, id):
    con = Movie.objects.filter(country=id)
    context = {
        'menu': menu,
        'con': con,
    }
    return render(request, 'country.html', context)


def genre(request, id):
    gen = Movie.objects.filter(genre=id)
    context = {
        'menu': menu,
        'gen': gen,
    }
    return render(request, 'genre.html', context)


def year(request, id):
    year = Movie.objects.filter(year_id=id)
    print(year)
    context = {
        'menu': menu,
        'year': year,
    }
    return render(request, 'year.html', context)


def add_kino(request):
    context = {
        'menu': menu,
        'zagalovok': 'Добавить',
    }
    return render(request, 'add_kino.html', context)
