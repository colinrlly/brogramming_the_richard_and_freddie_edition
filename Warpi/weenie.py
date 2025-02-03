from turtle import *
color("orange")
bgcolor("black")


forward(200)
left(90)
forward(25)
right(90)
circle(-50,180) #the negative 50 is the radius of the circle and this lets it curve to the right, postive kept curving to the left
right(90)
forward(25)
left(90)
forward(125)
left(90)
circle(-30,180) #-30 is the radius to make the ball smaller than the tip
left(180) #including this sets the draw direction to go straight down, not including this kept making a full circle with the below command
circle(-30,180)



        



hideturtle()
done()