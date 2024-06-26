import pgzrun
import random

WIDTH = 800
HEIGHT = 602

heart = 3

ship = Actor("player/spaceships/playership1_blue")
ship.x = 370
ship.y = 550

ship2 = Actor("player/spaceships/playership1_red")
ship2.x = 370
ship2.y = 550

gem = Actor("items/gemgreen")
gem.x = random.randint(20, 780)
gem.y = 0

score = 0
game_over = False


def on_mouse_move(pos, rel, buttons):
    ship.x = pos[0]


def update():
    global score, game_over, heart

    if keyboard.left:
        ship.x = ship.x - 5
    if keyboard.right:
        ship.x = ship.x + 5

    if keyboard.a:
        ship2.x = ship.x - 5
    if keyboard.d:
        ship2.x = ship.x + 5

    gem.y = gem.y + 4 + score / 5


    if heart == 0:
      game_over = True

    if gem.colliderect(ship):
        gem.x = random.randint(20, 780)
        gem.y = 0
        score = score + 1

    if gem.y > 600:
       heart = heart -1
       gem.y = 0

def draw():
    screen.fill((80, 0, 70))
    if game_over:
        screen.draw.text("Game Over", (360, 300), color=(255, 255, 255), fontsize=60)
        screen.draw.text(
            "Score: " + str(score), (360, 350), color=(255, 255, 255), fontsize=60
        )
    else:
        gem.draw()
        ship.draw()
        ship2.draw()
        screen.draw.text(
            "Score: " + str(score) +"       Hearts" + str(heart), (15, 10), color=(255, 255, 255), fontsize=30
        )


pgzrun.go()  # Must be last line
