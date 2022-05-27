from constants import fonts_folder
from constants import logo_img
from constants import SCREEN_COLOR
from constants import background_img
from constants import BUTTON_COLOR
import constants as const
import pygame

WIDTH = 800  # game window width
HEIGHT = 600  # game window height
FPS = 30  # частота кадров в секунду
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()
pygame.mixer.init()

FONT = pygame.font.Font(fonts_folder + '/Font.ttf', int(HEIGHT / 45))


class Logo(pygame.sprite.Sprite):
    def __init__(self, position, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(logo_img, (int(width / 5), int(height / 12)))
        self.image.set_colorkey(SCREEN_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = position


class Background(pygame.sprite.Sprite):
    def __init__(self, position, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(background_img, (int(width), int(height)))
        self.image.set_colorkey(SCREEN_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = position
