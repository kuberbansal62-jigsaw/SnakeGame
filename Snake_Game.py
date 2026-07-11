import turtle
import random
import time

delay=0.05
# Score
score=0
high_score=0
# Screen setup
win=turtle.Screen()
win.title("Snake Bite by @CodesbyKB")
win.bgcolor("#080E12")
win.setup(width=600,height=600)
win.tracer(0)


# Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#39FF14")
head.penup()
head.goto(0,0)
head.direction="stop"


# Snake Food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#CC76A1")
food.penup()
food.goto(0,100)
seg=[]

#Pen
pen=turtle.Turtle()
pen.color("White")
pen.speed(0)
pen.penup()
pen.shape("square")
pen.hideturtle()
pen.goto(0,260)
pen.write("Score :  0 High Score : 0 ",align="center",font=("courier",24,"normal"))
# Functions

def go_up():
  if head.direction!="down":
   head.direction="up"
def go_down():
  if head.direction!="up":
   head.direction="down"
def go_left():
  if head.direction!="right":
   head.direction="left"
def go_right():
  if head.direction!="left":
   head.direction="right"

def move():
    if(head.direction=="up"):
        y=head.ycor()
        head.sety(y+20)
    elif(head.direction=="down"):
        y=head.ycor()
        head.sety(y-20)
    elif(head.direction=="left"):
        x=head.xcor()
        head.setx(x-20)
    elif(head.direction=="right"):
        x=head.xcor()
        head.setx(x+20)

# Keyboard Bindings
win.listen()
win.onkeypress(go_up,"w")
win.onkeypress(go_down,"s")
win.onkeypress(go_left,"a")
win.onkeypress(go_right,"d")
# Main Game Loop
while True:
    win.update()
    # Check for Body collision
    for segment in seg:
        if segment.distance(head)<20:
            time.sleep(1)
            head.direction="stop"
            head.goto(0,0)
            for segment in seg:
              segment.goto(1000,1000)
          
            seg.clear()
            score=0
            pen.clear()
            pen.write(f"Score : {score} High Score : {high_score}".format(score,high_score),align="center",font=("courier",24,"normal"))
       #add a segment 
    # Check for Border Collision
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
      time.sleep(1)
      head.goto(0,0)
      
      head.direction="stop"
      # Removing segments
      for segment in seg:
          segment.goto(1000,1000)
          
      seg.clear()
      score=0
      pen.clear()
      pen.write(f"Score : {score} High Score : {high_score}".format(score,high_score),align="center",font=("courier",24,"normal"))
       #add a segment 
    if head.distance(food)<20:
       #Collision happened
       x=random.randint(-290,290)
       y=random.randint(-270,270)
       food.goto(x,y)
      #  Scoring game
       score+=10
       if score>high_score:
          high_score=score
       pen.clear()
       pen.write(f"Score : {score} High Score : {high_score}".format(score,high_score),align="center",font=("courier",24,"normal"))
       #add a segment 
       n_seg=turtle.Turtle()
       n_seg.color("green")
       n_seg.shape("square")
       n_seg.speed(0)
       n_seg.penup()
       seg.append(n_seg)
       #move segments in reverse order
    for index in range(len(seg)-1,0,-1):
          x=seg[index-1].xcor()
          y=seg[index-1].ycor()
          seg[index].goto(x,y)
    if(len(seg)>0):
          x=head.xcor()
          y=head.ycor()
          seg[0].goto(x,y)
          
    
    move()
    time.sleep(delay)

win.mainloop()