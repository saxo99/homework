from turtle import* 


#we want to paint a house 

#step 1: draw a square
speed(30)

width(7)
color("brown") 
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70) 
left(90)
color("black")
begin_fill()
forward(110)    #height of the door 
right(90)
forward(60)
right(90)
forward(110)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
color("blue")
 
penup()
goto(0,70)
pendown()
begin_fill()
left(120)
forward(40)
left(90)
forward(60)         #height of the window
left(90)
forward(40)
end_fill()

color("blue")

penup()
goto(200,70)
pendown()
begin_fill()
forward(40)
right(90)
forward(60)
right(90)
forward(40)
end_fill()

color("green")
width(50)
penup()
goto(-150,-25)
pendown()
forward(500)

exitonclick()

