# TV Shows Catalog

## Description

TV Shows Catalog is a Django web application that allows users to browse, search, and filter a large collection of television series.

The project uses a dataset of more than 44,000 TV shows, providing information such as titles, release dates, genres, countries of origin, ratings, seasons, episodes, overviews, and poster images.

Users can search the catalog by title and refine results using genre and country filters. The application features a responsive interface built with the Bootstrap Green template and is deployed on Render using PostgreSQL as its database backend.

This project was developed as part of a back-end portfolio with a focus on relational database design, filtering and search functionality, pagination, deployment, and maintainable Django development practices.

## Features

- Browse a catalog of more than 44,000 TV shows.
- Search TV shows by title.
- Filter results by genre.
- Filter results by country of origin.
- Combine search and filters simultaneously.
- Pagination for improved performance and navigation.
- Detailed page for each TV show with additional information.
- TV show posters displayed in catalog and detail views.
- Responsive user interface based on the Bootstrap Green template.
- AJAX-powered filtering for a smoother user experience.
- PostgreSQL database deployment on Render.

## Technologies Used

- Python 3
- Django 5.1
- PostgreSQL
- Bootstrap 5 (Green Template)
- JavaScript
- AJAX
- WhiteNoise
- Gunicorn
- Render

## Database Design

The database was structured using a normalized relational model.

The original dataset was reorganized into separate TVShow, Genre, and Country entities, with TVShowGenre and TVShowCountry relationship tables connecting TV shows to their genres and countries. This approach avoids redundant data storage and supports reliable filtering by genre and country.

Main entities:

- TVShow
- Genre
- Country
- TVShowGenre
- TVShowCountry

## Dataset

The project uses the following public dataset:

- All TV Series Details Dataset (Kaggle)

The original dataset was cleaned and normalized before being imported into PostgreSQL. This process helped structure the data consistently for the application's relational model and filtering functionality.

After processing, the application database contains:

- 44,311 TV shows
- 21 genres
- 122 countries
- 73,357 TV show–genre relationships
- 45,693 TV show–country relationships

## Key Implementation Decisions

Several implementation choices were made during development:

- PostgreSQL was selected instead of SQLite to gain experience with a production-oriented relational database system.
- Django pagination was implemented to improve performance when browsing large datasets.
- URL query parameters preserve search and filter state, allowing filtered views to be shared and revisited.
- AJAX was selectively introduced to improve the filtering experience while keeping the overall application server-rendered and easy to maintain.
- A fallback image is displayed when poster artwork is unavailable.
- Bootstrap Green was retained as the visual foundation of the project while adapting it to the application's requirements.
- Query correctness and maintainability were prioritized before applying advanced optimization techniques.

## Dataset Notes

The dataset used for this project comes from an external source. Some entries may contain mature or explicit imagery.

Since no reliable metadata field was available to consistently identify and filter such content without removing legitimate titles, the dataset was kept largely intact.

## Screenshots

### Home Page

![Home Page](screenshots/home-page.png)

### Catalog — Search and Filters

![Catalog — Search and Filters](screenshots/catalog-filters.png)

### TV Show Details

![TV Show Details](screenshots/tvshow-details.png)

