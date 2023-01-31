import pygame


class Brick:
    def __init__(self, pos_x, pos_y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos_x, pos_y)

class Rock(Brick):
    pass