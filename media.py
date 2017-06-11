import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    # Valid Ratings which is not yet implemented
    VALID_RAITINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Calls init function with 4 arguments that will store data
        in the class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        """Opens up browser to play the youtube link"""
