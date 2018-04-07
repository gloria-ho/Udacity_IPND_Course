# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

import media
# This imports the local media.py file to call the class Movie 
import fresh_tomatoes
'''
This imports the local fresh_tomatoes.py file which holds the layout and style information requited
to create a webpage with the data below
'''

lucky_number_slevin = media.Movie("Lucky Number Slevin", "2006", "R",
	"A case of mistaken identity puts a man named Slevin in the middle of a war between two rival New York crime lords: The Rabbi and the Boss.",
	"https://upload.wikimedia.org/wikipedia/en/a/a0/Lucky_Number_Slevin_Theater_Poster.JPG",
	"https://www.youtube.com/watch?v=fVIUEcizkPc")

crash = media.Movie("Crash", "2004", "R",
	"An American drama film featuring racial and social tensions in Los Angeles.",
	"https://upload.wikimedia.org/wikipedia/en/d/d0/Crash_ver2.jpg",
	"https://www.youtube.com/watch?v=Q3ahUiPnIvY")

the_departed = media.Movie("The Departed", "2006", "R",
	"An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
	"https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
	"https://www.youtube.com/watch?v=auYbpnEwBBg")

fight_club = media.Movie("Fight Club", "1999", "R",
	"An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an \
	underground fight club that evolves into something much, much more.",
	"https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
	"https://www.youtube.com/watch?v=SUXWAEX2jlg")

shutter_island = media.Movie("Shutter Island", "2010", "R",
	"In 1954, a U.S. marshal investigates the disappearance of a murderess who escaped from a hospital for the criminally insane.",
	"https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg",
	"https://www.youtube.com/watch?v=5iaYLCiq5RM")

seven = media.Movie("Seven", "1995", "R",
	"Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.",
	"https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg",
	"https://www.youtube.com/watch?v=znmZoVkCjpI")

movies = [lucky_number_slevin, crash, the_departed, fight_club, shutter_island, seven]
# List of all the movies so I can easily call it

fresh_tomatoes.open_movies_page(movies)
'''
This calls the open_movies_page function from the local fresh_tomatoes.py file that was imported above,
This will create a webpage useing all the data and fuctions that have been input and stored from entertainment_center.py,
fresh_tomatoes.py, and media.py
'''
