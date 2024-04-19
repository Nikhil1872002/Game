# Game.py
This Python script uses the turtle and random modules to draw colorful stars randomly on a 600x600 screen.
It creates an engaging visual display of stars in different colors and positions.
Importing Modules:
The program starts by importing the turtle and random modules.
import turtle: This module is used to create graphical drawings and animations using turtles.
import random: This module provides tools for generating random numbers and making random choices.
Set Up the Screen
The script initializes a 600x600 pixel screen with a black background.
Create a Turtle for Drawing
A turtle named star_turtle is created to draw the stars.
The turtle's pen is lifted off the screen (penup()) to avoid leaving trails between drawing locations.
The turtle's speed is set to maximum (speed(0)) for faster drawing.
Color Options:
The script uses a list of colors (red, green, blue, yellow, purple, orange) to color the stars randomly.
Drawing Stars:
The function draw_star(size) draws a small star of the specified size.
It uses a loop to draw the five points of the star.
The turtle moves forward a given size, then turns right 144 degrees to form the star shape.
The function begins and ends filling the star shape.
Drawing Random Stars:
The function draw_random_stars() continuously draws stars at random positions and colors.
The function moves the turtle to random coordinates on the screen (x and y coordinates).
A random color is chosen from the list of colors to fill the star.
The function calls draw_star(20) to draw a star of size 20.
After each star is drawn, the function pauses for a short time (time.sleep(0.5)) before drawing the next star.
Run the script: Run the script using Python