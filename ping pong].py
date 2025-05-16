from pygame import *



font.init()
font1 = font.Font(None, 80)
win = font1.render('win 2!', True, (255, 255, 255))
lose = font1.render('win 1!', True, (180, 0, 0))




img_ball = 'ball.png'
img_rocetka = 'rocetka.png'


class Plaeyer(sprite.Sprite):


class roketka(GameSprite):

    def update_l(self):
        keys key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y - self.speed
        if keys[K_s] and self.rect.y > 5:
self.rect.y += self.speed




def update_r(self):
keys = key.get_pressed()
if keys[K_UP] and self.rect.y > 5:
self,rect.y - self. speed
if keys[K_D0WN] and solf.rect.y > 5:
self.rect.y +- self.speed




def update_l(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y > 5:
        self.rect.y += self.speed

def update_l(self):
    keys = key.get_pressed()
    if keys[K_s] and self.rect.y > 5:
        self.rect.y -= self.speed


def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
        self.rect.y += self.speed

def update_r(self):
    keys = key.get_pressed()
    if keys[K_DOWN] and self.rect.y > 5:
        self.rect.y -= self.speed

win_width = 700
win_height = 500
display.set_caption("ping pong")
window = display.set_mode((win_width, win_height))
Window.fill(back)
rocetka = Player(img_hero, 5, win_height - 100, 80, 100, 10)


  def __init__(self, player_image, player_y, size_y, player_speed):
      sprite.Sprite.__init__(self)
      self.image = transform.scale(image.load(player_image), (size_y))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.y = player_y

  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))





