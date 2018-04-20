import pygame

class Sprite:
    def __init__(self, imageName, pos = (0,0)):
        self.imageName = imageName
        self.image = load_image(imageName)
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos

    def move(self, pos):
        self.pos = pos
        self.rect.center = pos

class Button(Sprite):
    def __init__(self, imageName, pos = (0,0), enabled = True):
        super().__init__(imageName, pos)
        self.enabled = enabled
        self.pressed = False

def load_image(imageName):
    try:
        image = pygame.image.load(imageName)
    except pygame.error:
        print("Cannot load image: ", imageName)
        raise SystemExit
    return image
