# Adam Gallant 2018-01-06

# media.py contains defines the Movie class which provides a way to store
# movie related information.

# import webbrowser to use for opening the trailer urls in the browser
import webbrowser


class Movie():
    # A class variable that defines the valid movie ratings in an array.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

# The init function allows the creation of class Movie instances,
# it requires the movie title, a brief synopsis, poster image url,
# and youtube trailer url.
# After defining a class Movie instance, it's instance variables can
# be accessed easily by typing "move_instance".title, for example.
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

# The show_trailer method can be called on an instance of class
# Movie easily by typing "movie_instance".show_trailer().
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
