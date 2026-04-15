from django.shortcuts import render, get_object_or_404
from .models import TVShow, Genre, TVShowGenre, Country, TVShowCountry
from django.http import JsonResponse
from django.template.loader import render_to_string

# Helper function to prepare poster URLs 
def prepare_poster_url(show):
    """Return the full poster URL or a placeholder if no image is available."""
    if show.poster_path:
        return "https://image.tmdb.org/t/p/w500/" + show.poster_path.lstrip('/')
    return "https://placehold.co/500x750?text=No+Image"


def tvshow_list(request):
    # Get the selected genre from the query parameters (?genre=Drama)
    genre_name = request.GET.get('genre')

    country_id = request.GET.get('country')

    q = request.GET.get('q')

    tvshows = TVShow.objects.all()

    # Filter TV shows by selected genre and/or country (if provided)
    if country_id:
        country_id = int(country_id)
        tvshows = tvshows.filter(tvshowcountry__country__id=country_id)

    if genre_name:
        genre_name = genre_name.strip()
        tvshows = tvshows.filter(tvshowgenre__genre__name__iexact=genre_name)

    if q:
        tvshows = tvshows.filter(name__icontains=q)   
    
    tvshows = tvshows.distinct().order_by('id')

    genres = Genre.objects.all()

    countries = Country.objects.all() 
    
    # Add a computed poster_url for each show
    for show in tvshows:
        show.poster_url = prepare_poster_url(show)        

    context = {
        'tvshows': tvshows,
        'genres': genres,
        'selected_genre': genre_name,
        'countries': countries,
        'selected_country': country_id,
        'q': q,
        'dynamic_title': 'TV Show List',
        'dynamic_description': 'Browse thousands of TV shows with posters and details in this Django-powered catalog.',
    }
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
        'catalog/partials/_tvshow_results.html',
        context,
        request=request
        )
        return JsonResponse({'html': html})

    return render(request, 'catalog/tvshow_list.html', context)


def tvshow_details(request, pk):
    show = get_object_or_404(TVShow, pk=pk)

    # Genres
    genres_shs = TVShowGenre.objects.filter(tvshow_id=pk)
    genre_ids = [genres_sh.genre_id for genres_sh in genres_shs]
    genres = Genre.objects.filter(pk__in=genre_ids) 

    # Countries
    countries_shs = TVShowCountry.objects.filter(tvshow_id=pk)
    country_ids = [countries_sh.country_id for countries_sh in countries_shs]
    countries = Country.objects.filter(pk__in=country_ids)

        
    # Add poster_url for the selected show
    show.poster_url = prepare_poster_url(show)

    # Clean and format overview text
    if show.overview:
        show.overview = show.overview.strip().replace('\\n', ' ')
         
    context = {
        'show': show,
        'genres': genres,
        'countries': countries,
        'dynamic_title': show.name,
        'dynamic_description': f"Details and information about {show.name}, released in {show.first_air_date.year if show.first_air_date else 'unknown year'}.",
    }
    return render(request, 'catalog/tvshow_details.html', context)

def about(request):
    context = {
        "dynamic_title": "About | TV Shows Catalog",
        "dynamic_description": "About the TV Shows Catalog project built with Django and Bootstrap."
    }
    return render(request, "catalog/about.html", context)