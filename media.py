

class Movie:
    """Data structure for a film entry.

    Attributes:
        title (str): The film's title.
        tagline (str): A tagline used to advertise the film.
        trailer_youtube_url (str): URL for a Youtube page of the film's trailer.
        poster_image_url (str): URL to an image of the film's theatrical release poster.
        background_color (str): Any valid CSS color value.
        director (str): The credited director(s).
        release_year (str): The year of the movie's first theatrical release.
    """

    def __init__(self, title, tagline, trailer_youtube_url, poster_image_url,
                 background_color, director, release_year):
        self.title = title
        self.tagline = tagline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.background_color = background_color
        self.director = director
        self.release_year = release_year
