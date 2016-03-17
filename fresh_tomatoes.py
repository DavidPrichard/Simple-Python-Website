#!/usr/bin/env python
"""Uses a list of movies and HTML templates to create an HTML document."""

import webbrowser
import os
import re
import entertainment_center

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
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
              'frameborder': 0,
              'scrolling': 'no'
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


# Takes a list of movie objects and outputs html movie tiles
def create_movie_tiles_content(movies):

    movie_tile_content = ''

    # An html template for a single movie tile
    movie_tile_template = '''
    <div class="movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" style="background:{background_color}">
    <img src="{poster_image_url}">
    <h2>{movie_title}</h2>
    <p class="tagline">"{tagline}"</p>
    <p class="byline">{director}, {release_year}</p>
    </div>
    '''

    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        movie_tile_content += movie_tile_template.format(
            movie_title=movie.title,
            tagline=movie.tagline,
            trailer_youtube_id=trailer_youtube_id,
            poster_image_url=movie.poster_image_url,
            background_color=movie.background_color,
            director=movie.director,
            release_year=movie.release_year
        )
    return movie_tile_content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace movie tile placeholder with movie tile content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file and open it in the browser
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


# MAIN
if __name__ == '__main__':

    open_movies_page(entertainment_center.movies)
