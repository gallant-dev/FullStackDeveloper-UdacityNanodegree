# Adam Gallant 2018-01-06

# entertainment_center.py contains the code defining the instances of the
# Movie() class.

# import media.py to use the created Movie class, and the Udacity supplied
# fresh_tomatoes.py to turn an array of my favourite movies into a website.
import fresh_tomatoes
import media

# Create instances of the class media.Movie with the details of my favourite
# movies.
unusual_suspects = media.Movie("The Unusual Suspects",
                               """A sole survivor tells the story of a gun
 battle.""",
                               """https://artandhistoryoffilmspring2014.
files.wordpress.com/2014/02/the-usual-suspects-poster-big.jpg""",
                               "https://www.youtube.com/watch?v=oiXdPolca5w")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://www.impawards.com/2009/posters/avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

count_of_monte_cristo = media.Movie("The Count of Monte Cristo",
                                    """The greatest tale of betrayal and revenge
                                    the world has ever known""",
                                    """https://images-na.ssl-images-amazon.com/
images/M/MV5BMTg2MTQwMDk4OF5BMl5BanBnXkFtZTYwNzM4NTA5._V1_.jpg""",
                                    """https://www.youtube.com/watch?v=gzRSVl8Ue
wM""")

spiderman = media.Movie("Spider-man",
                        "A man spider saves New York. ft. Mr. William Dafoe",
                        """https://vignette.wikia.nocookie.net/marvelmovies/
images/6/62/Spider-Man%282002%29dvd.jpg/revision/
latest?cb=20120523154526""",
                        "https://www.youtube.com/watch?v=TYMMOjBUPMM")

zoolander = media.Movie("Zoolander",
                        "A model idiot.",
                        """https://images-na.ssl-images-amazon.com/images/M/
MV5BODI4NDY2NDM5M15BMl5BanBnXkFtZTgwNzEwOTMxMDE@._V1_.jpg""",
                        "https://www.youtube.com/watch?v=MaEeSJZYkpY")

batman_begins = media.Movie("Batman Begins",
                            """The villians of Gotham are about to have a really
 bat day.""",
                            """http://vignette4.wikia.nocookie.net/batman/images
/b/bb/Batman_Begins-steelbook.jpg/revision/latest?cb=20130703173929""",
                            "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

# Create an array of the instanced movies beecause the function
# open_movies_page provided by Udacity requires an array of Movie
# class instances to populate the page.
movies = [unusual_suspects, avatar, count_of_monte_cristo, spiderman,
          zoolander, batman_begins]

# Feed the created array into the fresh_tomatoes.open_movies_page function
# which creates an HTML file and open's it in the webbrowser.
fresh_tomatoes.open_movies_page(movies)
