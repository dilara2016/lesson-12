import turtle   #inporting librari
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle() #denified variable

num_sides = 6 #variable
side_length = 70
angel = 360.0 / num_sides
#itirate loop for total number of sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angel)
turtle.done()