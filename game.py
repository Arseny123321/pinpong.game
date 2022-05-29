from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
    def flip(self):
        self.image = transform.flip(self.image, True, False)

class Player(GameSprite) :
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 180:
            self.rect.y += self.speed

class Player2(GameSprite) :
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 180:
            self.rect.y += self.speed

win_width = 900
win_height = 600
background_color = (255,255,255)


display.set_caption("ПинПонг")
window = display.set_mode((win_width, win_height))
window.fill(background_color)

clock = time.Clock()

player = Player('игрок.png', (win_width - 870) - 30, win_height/3, 40, 180, 5)
player2 = Player2('игрок.png', (win_width - (-30)) - 70, win_height/3, 40, 180, 5)
ball = GameSprite('мячик.png', (win_width/1.8) - 70, win_height/2.5, 40, 40, 5)

font.init()
font = font.Font(None, 80)
lose1 = font.render('PLAYER 1 LOSE', True, (255, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (255, 0, 0))

speed_x = 5
speed_y = 5

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if ball.rect.y > win_height - 40 or ball.rect.y < 0:
        speed_y *= -1

    if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball) :
        speed_x *= -1

    if ball.rect.x <= 0 :
        finish = True
        window.blit(lose1, (250, 250))

    if ball.rect.x > (win_width - 40) :
        finish = True
        window.blit(lose2, (250, 250))

    if finish != True:
        window.fill(background_color)
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        player.reset()
        player2.reset()
        ball.reset()

        player.update()
        player2.update()

    display.update()
    clock.tick(60)