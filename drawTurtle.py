# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

def draw_half_diamond(diamond_angle,length):
	turtle.forward(length)
	turtle.right(diamond_angle)
	turtle.forward(length)
	turtle.right(180-diamond_angle)

def draw_diamond(turn_angle,length):
	draw_half_diamond(turn_angle,length)
	draw_half_diamond(turn_angle,length)

def draw_flower(diamond_angle, turn_angle,length):
	index = 0
	while index < 360:
		draw_diamond(diamond_angle,length)
		turtle.right(turn_angle)
		index += turn_angle

def draw_end(end_degree,end_length):
	turtle.right(end_degree)
	turtle.forward(end_length)

turtle.speed(10)
turtle.shape("turtle")
turtle.shapesize(.5, .5, .5)
turtle.color("blue")
turtle.width(1)

draw_flower(30,10,50)
draw_end(90,200)

# Your code here.
raw_input('Hit any key to close')