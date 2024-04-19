import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Create a turtle for drawing stars
star_turtle = turtle.Turtle()
star_turtle.penup()
star_turtle.speed(0)  # Set the turtle speed to maximum

# List of possible colors
colors = ["red", "green", "blue", "yellow", "purple", "orange"]

# Function to draw a small star
def draw_star(size):
    star_turtle.begin_fill()
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(144)
    star_turtle.end_fill()

# Function to draw random stars
def draw_random_stars():
    while True:
        # Move the turtle to a random position
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        star_turtle.goto(x, y)
        
        # Set a random color
        star_turtle.color(random.choice(colors))
        
        # Draw a small star of size 20
        draw_star(20)
        
        # Pause for a short time before drawing the next star
        turtle.time.sleep(0.5)

# Start drawing random stars
draw_random_stars()

# Keep the turtle graphics window open
turtle.done()