from pygame import *
from pygame.cursors import ball


back = (200, 255, 255) 
win_width = 600
win_height = 500
window = display.set_mode( (win_width, win_height)) 
window.fill(back)

game = True 
finish = False 
clock =time.Clock()
FPS = 60


img_ball = 'ball.png'
img_rocetka = 'rocetka.png'



font.init()
font1 = font.Font(None, 80)
win = font1.render('win 2!', True, (255, 255, 255))
lose = font1.render('win 1!', True, (180, 0, 0))

class GameSprite():
    def __init__(self, player_image, player_y, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y - self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self,rect.y - self. speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y +- self.speed

racket1 = Player('rocetka.png',30, 200, 4, 50, 150) 
racket2 = Player('rocetka.png', 520, 200, 4, 50, 150)
ball = Player('ball.png',200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type - QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset()

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose, (200, 200))
            game_over = True 
        if ball.rect.x > win_width - 50:
            finish = True
            window.blit(win, (200, 200))
        
    display.update()
    clock.tick(FPS)





  





