# This is a fill-in-the-blanks quiz for my Unit 2 project.
# Introduction
print 'Hello and welcome to my Stage 2 project, a fill-in-the-blanks game.'

# The actual content for the various difficulties
easy = '\nA common first thing to do in a language is display "Hello world!" In Python this is particularly easy: all you have to do is type in: print "Hello world!"\n\nOf course, that isn\'t a very useful thing to do. However it is an example of how to output to the user using the print command, and produces a program which does something, so it is useful in that capacity.\n\nIt may seem a bit off to do something in a Turing complete language that can be done even more easily with an HTML file in a browser, but it\'s a step in learning Python syntax, and that\'s really its purpose.'
'''
EASY SOLUTIONS
world, python, print, html
'''
medium = '\nA function is created with the def keyword. You specify the inputs a function takes by adding arguments seperated by commas between the parentheses. Functions by default returns none if you don\'t specify the value to return. Arguments can be standard data types such as string, integer, disctionaty, typle, and list or can be more complicated such as objects and lambda functions.'
'''
MEDUM SOLUTIONS
function, arguments, none, list
'''
hard = '\nWhen you create a class, certain methods are automatically generated for you if you don\'t make them manually. These contain multiple underscores before and after the word defining them. When you write a class, you almost always include at least the __init__ method, defining variables for when instances of the class get made. Additionally, you generally want to create a __repr__ method, which will allow a string representation of the method to be viewed by other developers.\n\nYou can also create binary operators, like __add__ and __sub__, which allow + and - to be used by instances of the class. Similarily, __lt__, __gt__, and __eq__ allow instances of the class to be compared (with <,>, and ==).'
'''
HARD SOLUTIONS
class, method, __init__, instance, __repr__, __add__, __sub__, __lt__, __gt__, __eq__
'''
difficulty = [easy, medium, hard]
# The various levels the use can choose later
lives = {'easy': 7, 'medium': 5, 'hard': 3}
# The number of chances the user gets to guess per blank
total_lives = ()
# The number of guesses the user gets per level - TBD

# They key for the words that will be replaced and the user will need to guess in the game
answer_key = [['world', 'python', 'print', 'html'], ['function', 'arguments', 'none', 'list'], ['class','method', '__init__', 'instance', '__repr__', '__add__', '__sub__', '__lt__', '__gt__', '__eq__']]

def select_level():
# This funtion prompts the user to choose a level of difficulty
	level = raw_input('\nPlease select a level of difficulty by typing it in. \nPossible choices are easy, medium, or hard.').lower()
	def selected_level(user_input_level):
	# This function prints the level and total guesses per problem based on user input
		global total_lives
		# Sets the total_lives variable to global so the program can pull it up in other functions later on
		total_lives= lives[level]
		print '\nYou have selected '+ level +'! You will have ' + str(total_lives) + ' guesses per problem.'
	if level == 'easy':
		selected_level(level)
		return 0
	elif level == 'medium':
		selected_level(level)
		return 1
	elif level == 'hard':
		selected_level(level)
		return 2
	else:
		print '\nInvalid selection, please try again'
		return select_level()
		# If anything other than 'easy', 'medium', or 'hard' is input, try again

def end_game():
# User controls when the window closes, to ensure they've had a chance to read everything.	
	raw_input('\nThank you for trying my game. Press any key to close this window.')

def try_again():
# Present the option to try the level again without ckisung the window
	while True:
		try_again = raw_input('\nWould you like to try this level again? (Y/N)')
		if try_again.lower() == 'y':
			return play(level)
		elif try_again.lower() == 'n':
			return play_again()
		else:
			# If anything other than 'YES' or 'NO' is input, try again
			print '\nInvalid selection, please try again'

def play_again():
# Present the option to try a different level without closing the window
	while True:
		keep_playing = raw_input('\nWould you like to try a different level? (Y/N)')
		if keep_playing.lower() == 'y':
			return game()
		elif keep_playing.lower() == 'n':
			end_game()
			return none
		else:
		# If anything other than 'YES' or 'NO' is input, try again
			print '\nInvalid selection, please try again'

def search_for_blanks(level,missing):
	# This function searches for and replaces the key words
	content = difficulty[level]
	while missing < len(answer_key[level]):
		keyword = answer_key[level][missing]
		# Import the findall() regex to be able to split the string on multiple parameters including punctuations
		import re
		words = re.findall(r'[\w"\']+|[.,!?;]+|[\bmethods?\b]', content)
		index = 0
		while index < len(words):
			if words[index].lower() == keyword.lower():
				words[index] = '__' + str(missing + 1) + '__'
			index += 1
		missing += 1
		content = " ".join(words)
	return content

def play(level):
# This function will prompt the user to input the replacement words for the missing blanks
	missing_word = 0
	lives_left = total_lives
	while missing_word <len(answer_key[level]):
		print search_for_blanks(level, missing_word)
		question = '\nWhat should go in blank number ' + str(missing_word + 1) + '?'
		reply = raw_input(question).lower()
		answer = answer_key[level][missing_word].lower()
		if reply == answer:
			print '\nCorrect!'
			missing_word += 1
		else:
			if lives_left == 1:
				print "\nIncorrect. Sorry, you have run out of guesses. GAME OVER."
				return try_again()
			else:
				lives_left -=1
				print '\nIncorrect, please try again. You have ' + str(lives_left) + ' guesses left.'
	print difficulty[level]
	print '\nWell done, you\'ve completed this level!'

def game():
# This function runs the actual game and the option to continue or try again
	global level
	level = select_level()
	while True:
		play(level)
		try_again()

game()