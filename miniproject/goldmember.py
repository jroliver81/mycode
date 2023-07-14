# ADDING PHOTOS WITH TURTLE

#import turtle.screen()

#screen.bgcolor("white")

#screen.register_shape("goldmember.gif")

#image_turtle = turtle.turtle("goldmember.gif")

#screen.exitonclick()

#2nd attempt
#import turtle
#win = turtle.Screen()
#win.setup(width=800,height=600)
#win.bgpic('goldmember.gif')
#turtle.done()

#3rd

import turtle

# Register a custom turtle shape based on an image
turtle.register_shape("goldmember.gif")

# Create a turtle instance
t = turtle.Turtle()

# Set the turtle shape to the registered image shape
t.shape("goldmember.gif")

# Move the turtle to a desired position and angle
t.goto(100, 100)
t.setheading(45)

# Continue with other turtle movements and actions
t.forward(200)
t.left(90)
t.circle(100)

# Close the turtle graphics window
turtle.done()

