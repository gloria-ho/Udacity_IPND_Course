import webbrowser
# The webbrowser module allows the displaying of web-based documents

class Movie():
# This class provides a way to store movie related information

	def __init__(self, movie_title, movie_release_year, movie_rating, movie_storyline, Poster_image, trailer_youtube):
		'''
		This function within the Movoe class initializes a new instance of the class Movie.
		The __init__ function allocates memory for us to pass through and set the values
		for the movie's title, release year, rating, storyline, image url, and trailer url.

		'''
		self.title = movie_title
		self.release_year = movie_release_year
		self.rating = movie_rating
		self.storyline = movie_storyline
		self.poster_image_url = Poster_image
		self.trailer_youtube_url = trailer_youtube


	def show_trailer(self):
		'''
		This function opens the default web browswer to call and display the URL that is stored
		using the __init__ function above
		'''
		webbrowser.open(self.trailer_youtube_url) 