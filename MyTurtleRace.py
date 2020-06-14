import time
import turtle
from turtle import Turtle
from random import randint

#WINDOW SETUP
window=turtle.Screen()
window.title("My TURTLE RACE")
turt=turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-250,200)
turtle.write(" Turtle Race Championships",font=("Arial","30","bold"))
turtle.penup()
turtle.hideturtle()
#DIRT

turtle.setpos(-400,-180)
turtle.color("brown")
turtle.begin_fill()
turtle.pendown()
turtle.fd(800)
turtle.right(90)
turtle.fd(300)
turtle.right(90)
turtle.fd(800)
turtle.right(90)
turtle.fd(300)
turtle.end_fill()

#FINSH LINE
stamp_size2=20
square_size2=15
finsh_line2=200
turtle.color("black")
turtle.shape("square")
turtle.shapesize=(square_size2/stamp_size2)
turtle.penup()

for i in range(10):
    turtle.setpos(finsh_line2,(150-(i*square_size2*2)))
    turtle.stamp()
turtle.hideturtle()
for j in range (10):
    turtle.setpos( finsh_line2 +square_size2,((150-square_size2)- (j*square_size2*2)))
    turtle.stamp()
turtle.hideturtle()


#Sart lane Drawn
start_line = turtle.Turtle()
start_line.up()
start_line.speed(10)
start_line.right(90)
start_line.color("white")
start_line.goto((-210,110))
start_line.write("Starting Line", font = ("Times New Roman",12, "bold"))
start_line.down()


#Drawing the starting line.
for i in range(21):
	start_line.color("black")
	start_line.forward(5)
	start_line.color("white")
	start_line.forward(5)
start_line.hideturtle()

#RUN LINE

runline= turtle.Turtle()
runline.up()
runline.goto((-190,110))
runline.down()
runline.speed(120)
for y in range(26):
    runline.right(90)
    for x in range(11):
        runline.up()
        runline.fd(10)
        runline.down()
        runline.fd(10)
    runline.up()
    runline.bk(235)
    runline.left(45)
    runline.up()
    runline.fd(20)
    runline.down()
    runline.left(45)         
#Turtle 1
turt1=Turtle()
turt1.speed(0)
turt1.color("brown")
turt1.shape("turtle")
turt1.penup()
turt1.goto(-250,100)
turt1.pendown()

#TURTLE 2

turt2=Turtle()
turt2.speed(0)
turt2.color("orange")
turt2.shape("turtle")
turt2.penup()
turt2.goto(-250,50)
turt2.pendown()

#TURTLE 3

turt3=Turtle()
turt3.speed(0)
turt3.color("red")
turt3.shape("turtle")
turt3.penup()
turt3.goto(-250,0)
turt3.pendown()

#TURTLE 4

turt4=Turtle()
turt4.speed(0)
turt4.color("Blue")
turt4.shape("turtle")
turt4.penup()
turt4.goto(-250,-50)
turt4.pendown()

time.sleep(2) #Game pauses for 2 seconds as turtles prepare



#MOVING THE TURTLES
secondplace=turtle.Turtle()
secondplace.hideturtle()
for i in range(200): 
    turt1.fd(randint(1,5))
    turt2.fd(randint(1,5))
    turt3.fd(randint(1,5))
    turt4.fd(randint(1,5))
    if turt1.xcor() >= 190:
        turt1.color("Gold")
        turt1.write("BROWN TURTLE WINS!", font = ("Times New Roman", 14, "normal"))
        orangeturtle=turt2.xcor()
        blueturtle=turt4.xcor()
        redturtle=turt3.xcor()
        list1=[redturtle,orangeturtle,blueturtle]
        secondplace=max(list1)
        if blueturtle== max(list1):
            turt4.color("Silver")
            turt4.write("BLUE TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            newlist=list1.remove(max(list1))
            thirdplace==max(newlist)
            if redturtle==thirdplace:
                turt3.color("goldenrod")
                turt3.write("BLUE TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
            else:
                turt2=turt2.color("goldenrod")
                turt2.write("BROWN TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
                            
        elif orangeturtle== max(list1):
            turt2.color("Silver")
            turt2.write("ORANGE TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
        else:
            redturtle==max(list1)
            turt3.color("Silver")
            turt2.write("RED TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            
        #This tells white turtle to move to a position if they win (cross a certain x position that is equivalent to the x position of the finish line).
        break
        #This will stop the loop (and thus the turtles moving) regardless of if they have finished the range set earlier.
    if turt2.xcor() >= 190:
        turt2.color("Gold")
        turt2.write("ORANGE TURTLE WINS", font = ("Times New Roman", 14, "normal"))
        brownturtle=turt1.xcor()
        yellowturtle=turt4.xcor()
        redturtle=turt3.xcor()
        list2=[brownturtle,redturtle,yellowturtle]
        secondplace=max(list2)
        if brownturtle== secondplace:
            turt1.color("Silver")
            turt1.write("BROWN TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            newlist=list2.remove(max(list2))
            thirdplace=max(newlist)
            if redturtle==thirdplace:
                turt3.color("goldenrod")
                turt3.write("BLUE TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
            else:
                turt4=turt2.color("goldenrod")
                turt4.write("BROWN TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
        elif redturtle== max(list2):
            turt2.color("Silver")
            turt2.write("RED TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            newlist=list2.remove(max(list2))
            thirdplace=max(newlist2)
            if blueturtle==thirdplace:
                turt4.color("goldenrod")
                turt4.write("BLUE TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))

            else:
                turt3.color("goldenrod")
                turt3.write("RED TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
        
        else:
            turt4.color("Silver")
            turt4.write("BLUE TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            newlist=list1.remove(max(list1))
            thirdplace=max(newlist1)
            if redturtle==thirdplace:
                turt3.color("goldenrod")
                turt3.write("RED WINS BRONZE", font = ("Times New Roman", 14, "normal"))
            else:
                turt2.color("goldenrod")
                turt2.write("ORANGE TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
        #This tells white turtle to move to a position if they win (cross a certainx position that is equivalent to the x position of the finish line).
        break
        #This will stop the loop (and thus the turtles moving) regardless of if they have finished the range set earlier.
    if turt3.xcor() >= 190:
        turt3.color("Gold")
        turt3.write("RED TURTLE WINS!!!!!", font = ("Times New Roman", 14, "normal"))
        brownturtle=turt1.xcor()
        orangeturtle=turt2.xcor()
        blueturtle=turt4.xcor()
        list2=[greenturtle,orangeturtle,blueturtle]
        secondplace=max(list2)
        if brownturtle== secondplace:
            turt1.color("Silver")
            turt1.write(" BROWN TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            newlist=list1.remove(max(list1))
            thirdplace=max(newlist1)
            if redturtle==thirdplace:
                turt3.color("goldenrod")
                turt3.write("RED TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
            else:
                turt4=turt2.color("goldenrod")
                turt4.write("BROWN TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
            
        elif orangeturtle== max(list3):
            turt2.color("Silver")
            turt2.write("ORANGE TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            if blueturtle==thirdplace:
                turt4.color("goldenrod")
                turt4.write("BLUE TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
            else:
                turt1=turt2.color("goldenrod")
                turt1.write("BROWN TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
        else:
            blueturtle==max(list3)
            turt1.color("Silver")
            turt1.write("BLUE TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            newlist=list2.remove(max(list2))
            thirdplace=max(newlist2)
            if redturtle==thirdplace:
                turt2.color("goldenrod")
                turt2.write("ORANGE TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
                if brownturtle==thirdplace:
                    turt1.color("goldenrod")
                    turt1.write("BLUE TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
                else:
                    turt4.color("goldenrod")
                    turt1.write("RED TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
            else:
                turt4=turt2.color("goldenrod")
                turt4.write("BROWN TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
        #This tells white turtle to move to a position if they win (cross a certain x position that is equivalent to the x position of the finish line).
            break
        #This will stop the loop (and thus the turtles moving) regardless of if they have finished the range set earlier.
    if turt4.xcor() >= 190:
        turt4.color("Gold")
        turt4.write("BLUE TURTLE WINS !", font = ("Times New Roman", 14, "normal"))
        redturtle=turt3.xcor()
        orangeturtle=turt2.xcor()
        brownturtle=turt1.xcor()
        list4=[greenturtle,orangeturtle,redturtle]
        secondplace=max(list4)
        if brownturtle== max(list4):
            turt1.color("Silver")
            turt1.write("BROWN TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            list3=[brownturtle,orangeturtle,blueturtle]
            newlist=list3.remove(max(list3))
            thirdplace=max(newlist)
            if redturtle==thirdplace:
                turt3.color("goldenrod")
                turt3.write("RED TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
            else:
                turt2=turt2.color("goldenrod")
                turt2.write("BROWN TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
        elif orangeturtle== max(list4):
            turt2.color("Silver")
            turt2.write("ORANGE TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            newlist=list4.remove(max(list4))
            thirdplace=max(newlist)
            if redturtle==thirdplace:
                turt3.color("goldenrod")
                turt3.write("RED TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
            else:
                turt1.color("goldenrod")
                turt1.write("BROWN TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
        else:
            turt3.color("Silver")
            turt3.write("RED TURTLE WINS SLIVER", font = ("Times New Roman", 14, "normal"))
            if orangeturtle==thirdplace:
                turt2.color("goldenrod")
                turt2.write("ORANGE TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
            else:
                turt1.color("goldenrod")
                turt1.write("BROWN TURTLE WINS BRONZE", font = ("Times New Roman", 14, "normal"))
        #This tells white turtle to move to a position if they win (cross a certain x position that is equivalent to the x position of the finish line).
        break
        #This will stop the loop (and thus the turtles moving) regardless of if they have finished the range set earlier.
 
turtle.exitonclick()
