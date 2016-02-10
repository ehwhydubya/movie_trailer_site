import webbrowser


class Movie():

    """ This class provides a way to store movie-related information """

    # from http://www.mpaa.org/film-ratings/
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube_url, actors=[], release_date=None,
                 rating=None):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

        # ensures that user enters a list of actors instead of a string of
        # actors
        if not isinstance(actors, list):
            raise TypeError("Expecting actors as type <list>")

        self.actors = actors
        self.release_date = release_date

        # if you're going to enter a movie rating, enter a valid one
        if rating not in Movie.VALID_RATINGS and rating is not None:
            raise ValueError("You must enter a valid MPAA rating")

        self.rating = rating

    # opens trailer page
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    # lists actors if they're available
    def list_actors(self):
        if self.actors:
            for i in range(len(self.actors)):
                print self.actors[i]
        else:
            return "no actors to list"
