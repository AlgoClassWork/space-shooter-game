from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player = GameSprite(img='player.png', x=300, y=400, w=100, h=100)

window = display.set_mode( (700,500) )
display.set_caption('Шутер')

background =  transform.scale(image.load('background.jpg'), (700,500))

while True:
    for some_event in event.get():
        if some_event.type == QUIT:
            exit()

    window.blit( background, (0, 0) )
    player.show()

    display.update()
