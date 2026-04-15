from django.db import models

# Create your models here.
class TVShow(models.Model):
    name = models.CharField(max_length=255)
    original_language = models.CharField(max_length=10)
    number_of_seasons = models.PositiveIntegerField()
    number_of_episodes = models.PositiveIntegerField()

    first_air_date = models.DateField(null=True, blank=True)
    last_air_date = models.DateField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    poster_path = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = "TV Shows"
        
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name        

class TVShowGenre(models.Model):
    tvshow = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('tvshow', 'genre')
        verbose_name_plural = "TV Show Genres"

    def __str__(self):
        return f"{self.tvshow.name} - {self.genre.name}"

class Country(models.Model):
    code = models.CharField(max_length=5, unique=True)  # Ex: "US", "JP"
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Countries"  # Plural- admin

    def __str__(self):
        return f"{self.name} ({self.code})"    

class TVShowCountry(models.Model):
    tvshow = models.ForeignKey("TVShow", on_delete=models.CASCADE)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("tvshow", "country")
        verbose_name_plural = "TV Show Countries"

    def __str__(self):
        return f"{self.tvshow.name} - {self.country.code}"