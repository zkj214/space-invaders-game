import turtle
import random
from scoreboard import Scoreboard
from lasers import Lasers
from ship import Ship
from aliens import Aliens
import time


screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("green")
screen.title("Space Invaders")
screen.bgpic("images/background.gif")

turtle.register_shape("images/invader.gif")
turtle.register_shape("images/player.gif")
screen.tracer(0)

scoreboard=Scoreboard()
player=Ship()
bullet=Lasers()

enemies = []
for i in range(10):
    alien=Aliens()
    enemies.append(alien)

enemyspeed = 5


def move_left():
    x = player.xcor()
    x -= player.playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player.playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    if bullet.bulletstate == "ready":
        bullet.bulletstate = "fire"
        
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x, y)
        bullet.showturtle()


turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


missed_enemies = 0
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.15)
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 270:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285:
                    e.hideturtle()
                    missed_enemies += 1
                    if missed_enemies == 5:
                        game_is_on=False

                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.goto(x, y)
                    e.showturtle()
           
            enemyspeed *= -1 # move in reverse

        if enemy.xcor() < -270:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
                if e.ycor() < -285:
                    e.hideturtle()
                    missed_enemies += 1
                    if missed_enemies == 5:
                        game_is_on=False

                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    e.goto(x, y)
                    e.showturtle()
           
            enemyspeed *= -1 # move in reverse

        if bullet.distance(enemy) < 20:
            bullet.hideturtle()
            bullet.bulletstate = "ready"
            bullet.goto(0, -400)
          
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.goto(x, y)

            scoreboard.score += 10
            scoreboard.update_scoreboard()

        if player.distance(enemy) < 37:
            game_is_on=False
            player.hideturtle()
            bullet.hideturtle()
            for e in enemies:
                e.hideturtle()
            screen.bgpic("images/end.gif")
            screen.bgcolor("black")
            time.sleep(3)
    # movement of bullet
    if bullet.bulletstate == "fire":
        y = bullet.ycor()
        y += bullet.bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet.bulletstate = "ready"