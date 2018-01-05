import fresh_tomatoes
import media

unusual_suspects = media.Movie("The Unusual Suspects",
                        "A sole survivor tells the story of a gun battle.",
                        "https://lh3.googleusercontent.com/hJohval5tdfrdfgGKzRajijfFvpYABVBlhUp2j2-UXX23LnaleQOmGOwKrLRICKChcE=w200-h300",
                        "https://www.youtube.com/watch?v=oiXdPolca5w")

avatar = media.Movie("Avatar",
                        "A marine on an alien planet.",
                        "http://www.impawards.com/2009/posters/avatar.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

count_of_monte_cristo = media.Movie("The Count of Monte Cristo",
                                   "The greatest tale of betrayal and reveng ethe world has ever known",
                                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MTQwMDk4OF5BMl5BanBnXkFtZTYwNzM4NTA5._V1_.jpg",
                                   "https://www.youtube.com/watch?v=gzRSVl8UewM")

spiderman = media.Movie("Spider-man",
                        "A man spider saves New York. ft. Mr. William Dafoe",
                        "https://vignette.wikia.nocookie.net/marvelmovies/images/6/62/Spider-Man%282002%29dvd.jpg/revision/latest?cb=20120523154526",
                        "https://www.youtube.com/watch?v=TYMMOjBUPMM")

zoolander = media.Movie("Zoolander",
                        "A model idiot.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BODI4NDY2NDM5M15BMl5BanBnXkFtZTgwNzEwOTMxMDE@._V1_.jpg",
                        "https://www.youtube.com/watch?v=MaEeSJZYkpY")

batman_begins = media.Movie("Batman Begins",
                        "The villians of Gotham are about to have a really bat day.",
                        "http://vignette4.wikia.nocookie.net/batman/images/b/bb/Batman_Begins-steelbook.jpg/revision/latest?cb=20130703173929",
                        "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

movies = [unusual_suspects, avatar, count_of_monte_cristo, spiderman, zoolander, batman_begins]
#count_of_monte_cristo.show_trailer()
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
