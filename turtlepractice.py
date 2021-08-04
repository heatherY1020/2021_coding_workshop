import turtle as t
import random
import math
import numpy as np

screen = t.Screen()
screen.bgcolor('black')

p = t.Turtle()
p.shape('turtle')
p.color('white')
p.turtlesize(2,2)
speed_p = 5
speed = 2
score = 0
p.penup()

p2 = t.Turtle()
p2.shape('turtle')
p2.color('yellow')
p2.turtlesize(2,2)
p2.penup()

bug = t.Turtle()
bug.shape('circle')
bug.color('blue')
bug.turtlesize(1,1)
bug.penup()
bug.setposition(random.randint(-300,300), random.randint(-300,300))

e = t.Turtle()
e.shape('turtle')
e.color('red')
e.turtlesize(2,2)
e.penup()
e.setposition(200,200)
Ang=0
ang=0

def turnright():
    p.setheading(0)
def turnleft():
    p.setheading(180)
def turnup():
    p.setheading(90)
def turndown():
    p.setheading(270)
def turnright2():
    p2.setheading(0)
def turnleft2():
    p2.setheading(180)
def turnup2():
    p2.setheading(90)
def turndown2():
    p2.setheading(270)
    
screen.listen()
screen.onkeypress(turnright, "Right")
screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnup, "Up")
screen.onkeypress(turndown, "Down")
screen.onkeypress(turnright2, "d")
screen.onkeypress(turnleft2, "a")
screen.onkeypress(turnup2, "w")
screen.onkeypress(turndown2, "s")


while True:
    p.forward(speed_p)
    p2.forward(speed_p)
    e.forward(speed)
    if p.xcor()<-300 or p.xcor()>300:
        p.right(180)
    if p.ycor()<-300 or p.ycor()>300:
        p.right(180)
    if e.xcor()<-300 or e.xcor()>300:
        p.right(180)
    if e.ycor()<-300 or e.ycor()>300:
        p.right(180)
    if p2.xcor()<-300 or p2.xcor()>300:
        p2.right(180)
    if p2.ycor()<-300 or p2.ycor()>300:
        p2.right(180)
        
    def distance(x,y):
        return math.sqrt((x.xcor()-y.xcor())**2+(x.ycor()-y.ycor())**2)
    
    if distance(p,bug)<=20:
        bug.goto(random.randint(-300,300), random.randint(-300,300))
        score +=1
        print(score)
    if distance(p2,bug)<=20:
        bug.goto(random.randint(-300,300), random.randint(-300,300))
        score +=1
        print(score)
    if distance(p,bug)<distance(p2,bug):
        e.setheading(e.towards(p.pos()))
    if distance(p2,bug)<distance(p,bug):
        e.setheading(e.towards(p2.pos()))
    speed += score
    if speed>5:
        speed=5
    if distance(p,e)<15 or distance(p2,e)<15:
        break
text = "Score:"+str(score)
message = "Game Over!"+text
print(message)
score=0

screen.mainloop()
