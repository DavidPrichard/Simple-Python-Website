

class Movie:

    def __init__(self, title, trailer_youtube_id, trailer_youtube_url, poster_image_url):
        self.title = title
        self.trailer_youtube_id = trailer_youtube_id
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url


# movie = Movie('title', 'trailer', 'trailer_url', 'poster_url')

movie1 = Movie('The Matrix',
               'TRAILER-ID1',
               'https://www.youtube.com/watch?v=m8e-FF8MsqU',
               'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg'
               )

movie2 = Movie('Lost in Translation',
               'TRAILER-ID2',
               'https://www.youtube.com/watch?v=sU0oZsqeG_s',
               'https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg'
               )

movie3 = Movie('The Life Aquatic with Steve Zissou',
               'TRAILER-ID3',
               'https://www.youtube.com/watch?v=yh401Rmkq0o',
               'https://upload.wikimedia.org/wikipedia/en/7/7c/Lifeaquaticposter.jpg'
               )

movies = [movie1, movie2, movie3]