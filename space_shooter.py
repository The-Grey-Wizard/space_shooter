import random, turtle
screen = turtle.Screen()
####SETUP THE BALL###
ball = turtle.Turtle()
ball.speed(3)
ball.shape("circle")
ball.color("white")
ball.penup()
###SETUP PLAYER###
player = turtle.Turtle()
player.shape("arrow")
player.color("white")
player.penup()
player.forward(40)
player.right(360)
player.speed(7)
###Collision function###
def collision(bullet,ball):
  if abs(bullet.xcor() - ball.xcor()) < 10 and abs(bullet.ycor() - ball.ycor()) < 10:
    print("Hit!")
while True:
  x=random.randrange(-250,250)
  y=random.randrange(-250,250)
  ball.goto(x,y)
  player.setheading(player.towards(ball))
  bullet = player.clone()   #Clone your player to "shoot"
  bullet.shape("classic")
  bullet.speed(10)
  bullet.forward(300)
  collision(bullet,ball)
