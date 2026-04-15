from django.contrib import admin
from .models import TVShow, Genre, TVShowGenre, Country, TVShowCountry

# Register your models here.
@admin.register(TVShow)
class TVShowAdmin(admin.ModelAdmin):
    list_display = ("name", "first_air_date", "original_language")
    search_fields = ("name", "original_language")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)    

@admin.register(TVShowGenre)
class TVShowGenreAdmin(admin.ModelAdmin):
    list_display = ("tvshow", "genre")
    search_fields = ("tvshow__name", "genre__name")

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code") 

@admin.register(TVShowCountry)
class TVShowCountryAdmin(admin.ModelAdmin):
    list_display = ("tvshow", "country")
    search_fields = ("tvshow__name", "country__code")       