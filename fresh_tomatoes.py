
import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <link rel="stylesheet" href="fresh_tomatoes.css">
    <link href='https://fonts.googleapis.com/css?family=Sorts+Mill+Goudy' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Lato:400,300,100' rel='stylesheet' type='text/css'>
    <script src="https://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" charset="utf-8">
        // Stop the video when the modal is closed
        $(document).on('click', '.modal', function (event) {
            // Remove the src and the player itself,
            // only reliable way to stop the video in IE
            $("#trailer-video-container").empty();
        });
        // Start the video when the modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $('#trailer-video-container').empty().append($('<iframe></iframe>', {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
<body>
    <header id="banner">
        <a class="title" href="#">
            <svg class="tomato" viewBox="0 0 48 48">
                <circle cx="24" cy="24" r="20"/>
            </svg>
            Fresh Tomatoes
            <span class="avoid-wrap">Movie Trailers
                <svg class="tomato" viewBox="0 0 48 48">
                    <circle cx="24" cy="24" r="20"/>
                </svg>
            </span>
        </a>
    </header>

    <main class="flex-container">
      {movie_tiles}
    </main>

    <div class="modal" id="trailer" style="display:none">
        <div id="trailer-video-container"></div>
    </div>
</body>
</html>
'''


# An html template for a single movie entry
movie_tile_content = '''
<div class="movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" style="background:{background_color}">
    <img src="{poster_image_url}">
    <h2>{movie_title}</h2>
    <p class="tagline">"{tagline}"</p>
    <p class="byline">{director}, {release_year}</p>
</div>
'''

# Object used to store and render each movie
class Movie:

    def __init__(self, title, tagline, trailer_youtube_url, poster_image_url, background_color, director, release_year):
        self.title = title
        self.tagline = tagline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.background_color = background_color  # valid CSS color value for movie-tile background
        self.director = director
        self.release_year = release_year


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            tagline=movie.tagline,
            trailer_youtube_id=trailer_youtube_id,
            poster_image_url=movie.poster_image_url,
            background_color=movie.background_color,
            director=movie.director,
            release_year=movie.release_year
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


# MAIN
if __name__ == '__main__':

    movie1 = Movie('The Matrix',
                   'The fight for the future begins.',
                   'https://www.youtube.com/watch?v=m8e-FF8MsqU',
                   'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg',
                   '#878CA9',
                   'The Wachowskis',
                   '1999'
                   )

    movie2 = Movie('Lost in Translation',
                   'Everyone wants to be found.',
                   'https://www.youtube.com/watch?v=sU0oZsqeG_s',
                   'https://upload.wikimedia.org/wikipedia/en/4/4c/Lost_in_Translation_poster.jpg',
                   '#FF7941',
                   'Wes Anderson',
                   '2003'
                   )

    movie3 = Movie('The Life Aquatic',
                   'The deeper you go,<br>the weirder life gets.',
                   'https://www.youtube.com/watch?v=yh401Rmkq0o',
                   'https://upload.wikimedia.org/wikipedia/en/7/7c/Lifeaquaticposter.jpg',
                   '#CFDB53',
                   'Wes Anderson',
                   '2004'
                   )

    movie4 = Movie('Fargo',
                   'A homespun murder story.',
                   'https://www.youtube.com/watch?v=h2tY82z3xXU',
                   'https://upload.wikimedia.org/wikipedia/en/a/ac/Fargo.jpg',
                   '#CA4954',
                   'Coen Brothers',
                   '1996'
                   )

    movies = [movie1, movie2, movie3, movie4]
    open_movies_page(movies)