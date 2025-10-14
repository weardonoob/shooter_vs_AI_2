import pygame, pyautogui, time, random, os
pygame.font.init()
pygame.mixer.init()
#mixer is for sounds
WIDTH, HEIGHT = pyautogui.size()
TITLE = "bunny_sprites"
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("bunny_sprites")


class Bunny(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bugs_bunny.png")
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 100,100
    def update(self, keys):
        if keys[pygame.K_UP]:
            self.rect.y -= 10
p = pygame.sprite.Group()
bunny = Bunny()
p.add(bunny)
while -13:
    p.draw(screen)
    keys = pygame.key.get_pressed()
    bunny.update(keys)
    bunny.rect.y += 1
    pygame.display.update()
    









