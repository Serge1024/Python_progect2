import constants as const
from constants import LIST_OF_BUSINESS 
from constants import RED
from constants import WHITE
from constants import BLUE
from constants import BLACK
from constants import FONT_COLOR
from base_constants import price_of_worker
import pygame
from graphics import Logo
from graphics import WIDTH
from graphics import HEIGHT
from graphics import Background
from graphics import BUTTON_COLOR
from graphics import fonts_folder
from graphics import FONT


class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size, height):
        pygame.sprite.Sprite.__init__(self)
        self.text = text
        self.image = pygame.Surface(size)
        self.image.fill(BUTTON_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.font = pygame.font.Font(fonts_folder + '/Font.ttf', int(height / 20))

    def draw(self, surface):
        pygame.draw.rect(surface,const.BLUE, self.rect, 0)
        pygame.draw.rect(surface, const.WHITE, self.rect, 2)
        text_surface = self.font.render(self.text, False, FONT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)


# CPS means Clicks per second
class UpgradeCPS(Button):
    def __init__(self, pos, text, size, height):
        super().__init__(pos, text, size, height)
        self.rect = Button(pos, text, size, height).rect
        self.count = 0
        self.text = text
        self.color =const.RED
        self.border_color =const.BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)
        text_surface = FONT.render(" " + str(self.text), False, FONT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)

    def click(self, auto_clicks, rub_score):
        return 0, 0


# CPC means clicks per click
class UpgradeCPC(Button):
    def __init__(self, pos, text, price, size, height):
        super().__init__(pos, text, size, height)
        self.rect = Button(pos, text, size, height).rect
        self.count = 0
        self.text = text
        self.price = price
        self.color = const.RED
        self.border_color = const.BLACK

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)
        text_surface = FONT.render(" " + str(self.text), False, FONT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)

    def click(self, booster, dollar_score):
        if dollar_score >= self.price:
            self.count += 1
            dollar_score -= self.price
            booster += 1
            self.price *= 1.2
            self.price = int(self.price)
        return booster, dollar_score

    def check_if_available(self, dollar_score):
        if self.price <= dollar_score:
            self.color = BLUE
            return True
        else:
            self.color = const.RED
            return False

class BusinessButton(Button):
    def __init__(self, pos, text, price, size, height, business):
        super().__init__(pos, text, size, height)
        self.rect = Button(pos, text, size, height).rect
        self.count = 0
        self.text = text
        self.price = price
        self.color = RED
        self.border_color = const.BLACK
        self.business = business

    def clicable(self, dollar_score):
        return self.business.price <= dollar_score

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)
        text_surface = FONT.render(" " + str(self.text), False, FONT_COLOR)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (self.rect.left + 10, self.rect.top + self.rect.height * 0.25)
        surface.blit(text_surface, text_rect)
    def click(self, dollar_score):
        if dollar_score >= self.price:
            dollar_score -= self.price
        return self.business, dollar_score

    def check_if_available(self, dollar_score):
        if self.price <= dollar_score:
            self.color = const.BLUE
            return True
        else:
            self.color = const.RED
            return False

def init_list_this_button(LIST_OF_BUSINESS, width, height):
    bisnes_button = list()
    for inc in range(len(LIST_OF_BUSINESS)):
        bisnes_button.append(
            BusinessButton((width / 4 + width / 2 * (inc % 2), 
                (int(inc / 2) * height / 6) + height / 6),
                LIST_OF_BUSINESS[inc].name,
                LIST_OF_BUSINESS[inc].price,
                (width * 3 / 8, height / 12),
                height, LIST_OF_BUSINESS[inc]))
    return bisnes_button

def initiate_buttons(width, height):
    upgrade_cpc = UpgradeCPC(
            (width / 4,  height / 6),
            'Повысить свой razryad', 1, 
            (width * 3 / 8, height / 12), height)
    upgrade_cps = UpgradeCPS(
            (width / 4 + width / 2,  height / 6),
            'Купить бизнес',
            (width * 3 / 8, height / 12), height)

    main_menu = [
                 Button(
                     (width / 2, height / 3),
                     "Play!", (width / 4, height / 6),
                     height)]

    settings = [Button((width / 3, 2 * height / 3), "FullScreen",
                    (width / 4, height / 6), height),
                Button((2 * width / 3, height / 3),
                    "800 x 600", (width / 4, height / 6), height),
                Button((2 * width / 3, 2 * height / 3),
                    "1200 x 900", (width / 4, height / 6), height),
                Button((width / 3, height / 3), 
                    "Back", (width / 4, height / 6), height)]

    bisnes_button = init_list_this_button(LIST_OF_BUSINESS, width, height)
    back_business = Button((width / 4, height / 6 + 400),
                        "Back", (width * 3 / 8, height / 12), height)
    my_business = Button((width / 4 + 400, height / 6 + 400),
                      "My business", (width * 3 / 8, height / 12), height)
    YES_button = Button((width / 4 + 350, height / 6 + 300 ),
                     "YES", (width * 3/ 20, height / 12), height)
    NO_button = Button((width / 4 + 500, height / 6 + 300),
                    "NO", (width * 3 /20, height / 12), height)
    text_pole_make_offer = list()
    for inc in range(4):
        text_pole_make_offer.append(
                Button((width / 4 + 500 - inc * 100, height / 6 + 100),
                    "", (width * 3 /30, height / 12), height))
    make_offer_button = Button(
            (width / 4 + 450, height / 6), "make offer", 
            (width * 3 /12, height / 12), height)
    add_rub_button = Button(
            (width / 4 - 150, height / 6 ), "", (width * 3 /30, height / 12), height)
    text_pole_make_offer.append(add_rub_button)
    add_button_for_rub = Button(
            (width / 4 - 50, height / 6 ), "add", (width * 3 /30, height / 12), height)

    add_worker = Button(
            (width / 4 + 450, height / 6 + 400),
            "add_worker $" + str(price_of_worker), 
            (width * 3 /10, height / 12), height)
    list_this_ans = [upgrade_cpc, upgrade_cps, main_menu,
            settings,  bisnes_button, back_business, my_business,
            YES_button, NO_button, text_pole_make_offer,
            make_offer_button, add_button_for_rub, add_worker]
    return list_this_ans
