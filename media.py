

class Movie:

    def __init__(self, title, tagline, trailer_youtube_url, poster_image_url, background_color, director, release_year):
        self.title = title
        self.tagline = tagline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.background_color = background_color  # valid CSS color value for movie-tile background
        self.director = director
        self.release_year = release_year
