import os
import pygame
from business import Recipt
from business import LIST_OF_MATIRIAL
from business import Business
from base_constants import price_of_worker

game_folder = os.path.dirname(__file__)
resources_folder = game_folder + '/../resources'
img_folder = os.path.join(resources_folder, 'sprites')
fonts_folder = os.path.join(resources_folder, 'fonts')
logo_img = pygame.image.load(os.path.join(img_folder, 'MIPT.png'))
background_img = pygame.image.load(os.path.join(img_folder, 'background.png'))


# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (100, 100, 200)
RED = (200, 100, 100)
GREEN = (100, 200, 100)
SCREEN_COLOR = WHITE
BUTTON_COLOR = BLUE
FONT_COLOR = BLACK

def recipt_maker(dict_this_ingredient):
    answer = dict()
    for material in LIST_OF_MATIRIAL:
        answer[material] = 0
    for material in dict_this_ingredient.keys():
        answer[material] = dict_this_ingredient[material]
    return answer

recipt_of_petrol = Recipt(recipt_maker({LIST_OF_MATIRIAL[0] : 3}),
                       recipt_maker({LIST_OF_MATIRIAL[1] : 2 }))
recipt_of_oil = Recipt(recipt_maker(dict()),
                    recipt_maker({LIST_OF_MATIRIAL[0] : 3}))
recipt_of_grass = Recipt(recipt_maker(dict()),
                      recipt_maker({LIST_OF_MATIRIAL[2] : 5}))
recipt_of_meat = Recipt(recipt_maker({LIST_OF_MATIRIAL[1] : 10,
                     LIST_OF_MATIRIAL[2] : 5}),
                     recipt_maker({LIST_OF_MATIRIAL[3] : 4}))

ferma = Business('Ферма', 6, recipt_of_meat, True, LIST_OF_MATIRIAL[3], 1)
pole = Business('Поле', 2, recipt_of_grass, False, LIST_OF_MATIRIAL[2], 2)
neft = Business('Нефтяная вышка', 1, recipt_of_oil, False, LIST_OF_MATIRIAL[0], 3)
zapravka = Business('заправка', 5, recipt_of_petrol, True, LIST_OF_MATIRIAL[1], 2)

LIST_OF_BUSINESS = [neft, zapravka, pole, ferma]
