import pygame

class Ball():
    def __init__(self, speed, image_path):
        self.__image = pygame.image.load(image_path)
        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(240, 350)
        self.__speed = speed
        self.__dirx = 1
        self.__diry = -1

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, valor):
        self.__rect = valor

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, valor):
        self.__speed = valor

    @property
    def dirx(self):
        return self.__dirx

    @dirx.setter
    def dirx(self, valor):
        self.__dirx = valor

    @property
    def diry(self):
        return self.__diry

    @diry.setter
    def diry(self, valor):
        self.__diry = valor

class Bate():
    def __init__(self, speed, image_path):
        self.__image = pygame.image.load(image_path)
        self.__rect = self.__image.get_rect()
        self.__rect.move_ip(240, 420)
        self.__speed = speed
        self.__prev_dir = -1

    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, valor):
        self.__rect = valor

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, valor):
        self.__speed = valor

    @property
    def prev_dir(self):
        return self.__prev_dir

    @prev_dir.setter
    def prev_dir(self, valor):
        self.__prev_dir = valor



class Brick():
    def __init__(self, pos_x, pos_y, image_path):
        self.__image = pygame.image.load(image_path)
        self.__rect = self.image.get_rect()
        self.__rect.move_ip(pos_x, pos_y)

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image

    def move(self, posx, posy):
        self.__rect.move(posx, posy)


class Rock(Brick):
    pass
