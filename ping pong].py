from pygame import *
from pygame.cursors import ball


back = (200, 255, 255) 
win_width = 600
win_height = 500
window = display.set_mode( (win_width, win_height)) 
window.fill(back)

game = True 
finish - False 
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

while game:
    for e in event.get():
        if e.type - QUIT:
            game = False

if finish != True:
    window.fill(back)
    racket1.update_l()
    racket2.update_r()

    racket1.reset()
    rocetka2.reset()
    ball.reset()
    
display.update()
clock.tick(FPS)


win_width = 700
win_height = 500
display.set_caption("ping pong")
window = display.set_mode((win_width, win_height))
Window.fill(back)
rocetka = Player(img_hero, 5, win_height - 100, 80, 100, 10)


  





