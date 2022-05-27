import pygame
import copy as copy
from graphics import SCREEN
from graphics import FPS
from graphics import SCREEN_COLOR
from graphics import Logo
from graphics import WIDTH
from graphics import HEIGHT
from graphics import Background
from graphics import fonts_folder
from buttons import initiate_buttons
from buttons import FONT_COLOR
from buttons import init_list_this_button
from constants import RED
from constants import WHITE
from constants import BLUE
from constants import BLACK
from base_constants import LIST_OF_MATIRIAL
from business import Contract
from business import Answer

class Game:
    def __init__(self):
        pygame.display.set_caption("MIPT clicker")
        self.clock = pygame.time.Clock()
        self.running = True
        self.logo = Logo((WIDTH / 10, 23 * HEIGHT / 24), WIDTH, HEIGHT)
        self.background = Background((WIDTH / 2, HEIGHT / 2), WIDTH, HEIGHT)
        self.font = pygame.font.Font(fonts_folder + '/Font.ttf', 20)
        self.font2 = pygame.font.Font(fonts_folder + '/Font.ttf', 40)
        answe = initiate_buttons(WIDTH, HEIGHT)
        self.upgradesCPC = answe[0]
        self.upgradesCPS = answe[1]
        self.menu_buttons = answe[2]
        self.settings_buttons = answe[3]
        self.business_button = answe[4]
        self.back_business = answe[5]
        self.my_business_button = answe[6]
        self.YES_button = answe[7]
        self.NO_button = answe[8]
        self.text_pole_make_offer = answe[9]
        self.make_offer_button = answe[10]
        self.add_button = answe[11]
        self.add_worker = answe[12]

        self.menu_running = True
        self.settings_running = True
        self.rub_score = 0
        self.dollar_score = 0
        self.booster = 1
        self.auto_clicks = 0
        self.prev_tick = 0
        self.my_business = list()
        self.business_id = 1

    def render_main(self):
        SCREEN.fill(SCREEN_COLOR)
        SCREEN.blit(self.background.image, self.background.rect)
        SCREEN.blit(self.logo.image, self.logo.rect)
        text = self.upgradesCPC.text
        self.upgradesCPC.text += " $ 1"
        self.upgradesCPC.draw(SCREEN)
        self.upgradesCPC.check_if_available(self.dollar_score)
        self.upgradesCPC.text = text
        self.upgradesCPS.draw(SCREEN)
        text_score_dollar = self.font.render("$" + str(self.dollar_score), True, FONT_COLOR)
        SCREEN.blit(text_score_dollar, (WIDTH / 20, HEIGHT / 20 + 200))
        pygame.display.flip()

    def render_menu(self):
        SCREEN.fill(BLACK)
        for button in self.menu_buttons:
            button.draw(SCREEN)
        pygame.display.flip()

    def render_settings(self):
        SCREEN.fill(BLACK)
        for button in self.settings_buttons:
            button.draw(SCREEN)
        pygame.display.flip()

    def check_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.menu_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.menu_buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.text == "Play!":
                            self.menu_running = False

    def check_settings_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.menu_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                global WIDTH
                global HEIGHT
                global SCREEN
                for button in self.settings_buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.text == "FullScreen":
                            WIDTH = 1920
                            HEIGHT = 1080
                        elif button.text == "800 x 600":
                            WIDTH = 800
                            HEIGHT = 600
                        elif button.text == "1200 x 900":
                            WIDTH = 1200
                            HEIGHT = 900
                        elif button.text == "Back":
                            self.settings_running = False
                        self.change_screen_size()
                        SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

    def render_my_own_business(self, business):
        list_of_nes = list()
        for material in business.recipt.ingredient.items():
            if (material[1] != 0):
                list_of_nes.append(material)
        string_of_nes = str()
        for material in list_of_nes:
            string_of_nes += material[0] + ' ' + str(material[1])

        SCREEN.fill(SCREEN_COLOR)
        SCREEN.blit(self.background.image, self.background.rect)
        SCREEN.blit(self.logo.image, self.logo.rect)
        self.back_business.draw(SCREEN)
        self.make_offer_button.draw(SCREEN)
        self.add_button.draw(SCREEN)
        self.add_worker.draw(SCREEN)
        LIST_THIS_PODPIS = ["id", 'what', 'How math', 'cost']
        for button in self.text_pole_make_offer:
            button.draw(SCREEN)
        podpis = self.font.render(LIST_THIS_PODPIS[0], True, FONT_COLOR)
        SCREEN.blit(podpis, (WIDTH / 20 + 350, HEIGHT / 20 + 100))

        podpis = self.font.render(LIST_THIS_PODPIS[1], True, FONT_COLOR)
        SCREEN.blit(podpis, (WIDTH / 20 + 450, HEIGHT / 20 + 100))

        podpis = self.font.render(LIST_THIS_PODPIS[2], True, FONT_COLOR)
        SCREEN.blit(podpis, (WIDTH / 20 + 525, HEIGHT / 20 + 100))

        podpis = self.font.render(LIST_THIS_PODPIS[3], True, FONT_COLOR)
        SCREEN.blit(podpis, (WIDTH / 20 + 650, HEIGHT / 20 + 100))
        draw_string = ''
        for material in business.sclad.items():
            draw_string += material[0] + ' ' + str(material[1]) + ' '
        text_sclad = self.font.render(draw_string, True, FONT_COLOR)
        SCREEN.blit(text_sclad, (WIDTH / 20, HEIGHT / 20 + 200))
        text_sclad = self.font.render("склад", True, FONT_COLOR)
        SCREEN.blit(text_sclad, (WIDTH / 20, HEIGHT / 20 + 150))
        text_recipt = self.font.render(string_of_nes, True, FONT_COLOR)
        SCREEN.blit(text_recipt, (WIDTH / 20, HEIGHT / 20 + 300))

        text_recipt = self.font.render("$ : " + str(business.cost_of_work),
                True, FONT_COLOR)
        SCREEN.blit(text_recipt, (WIDTH / 20, HEIGHT / 20 + 350))

        text_recipt = self.font.render("$_SCORE " + str(business.rub_score),
                True, FONT_COLOR)
        SCREEN.blit(text_recipt, (WIDTH / 20 + 100, HEIGHT / 20 + 350))

        text_recipt = self.font.render("count worker " + str(business.work_resurce),
                True, FONT_COLOR)
        SCREEN.blit(text_recipt, (WIDTH / 20, HEIGHT / 20 + 400))


        text_recipt = self.font.render("add dollar", True, FONT_COLOR)
        SCREEN.blit(text_recipt, (WIDTH / 20 - 10, HEIGHT / 20))


        text_recipt = self.font.render("необходимые материалы", True, FONT_COLOR)
        SCREEN.blit(text_recipt, (WIDTH / 20, HEIGHT / 20 + 250))

        text_business_id = self.font.render("business_id" +
                str(business.business_id), True, FONT_COLOR)
        SCREEN.blit(text_business_id, (WIDTH / 20 + 300, HEIGHT / 20 ))
        if (len(business.offer)):
            self.YES_button.draw(SCREEN)
            self.NO_button.draw(SCREEN)
            offer = business.offer[0]
            text_offer = self.font.render("from " +
                    str(offer.business_id_from) + " " +
                    offer.name + " " + str(offer.count), True, FONT_COLOR)
            SCREEN.blit(text_offer, (WIDTH / 20 + 500, HEIGHT / 20 + 200 ))
            text_offer = self.font.render( " cost " + str(offer.cost) , True, FONT_COLOR)
            SCREEN.blit(text_offer, (WIDTH / 20 + 500, HEIGHT / 20 + 250 ))

        pygame.display.flip()

    def check_events_my_own_business(self, business):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.business_running = False
                self.my_business_flag = False
                self.my_own_business = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.business_running = False
                    self.my_business_flag = False
                    self.my_own_business = False
                else:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode
                    self.text_pole_make_offer[self.now_write_in].text = self.user_text

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if (self.back_business.rect.collidepoint(event.pos)):
                    self.my_own_business = False
                    for button in self.text_pole_make_offer:
                        button.text = ''
                if (self.YES_button.rect.collidepoint(event.pos)):
                    dec_of_dollar, ans_to_buyer = business.say_yes()
                    self.dollar_score += dec_of_dollar
                    if (dec_of_dollar != 0):
                        import server
                        server.server.send_ans(ans_to_buyer)
                if (self.NO_button.rect.collidepoint(event.pos)):
                    import server
                    server.server.send_ans(business.say_no())
                for incr in range(5):
                    if (self.text_pole_make_offer[incr].rect.collidepoint(event.pos)):
                        self.now_write_in = incr
                        self.user_text = ''
                if (self.make_offer_button.rect.collidepoint(event.pos)):
                    helper = self.text_pole_make_offer[0 : 4]
                    offer = Contract(business.business_id,
                            int(helper[3].text), 
                            LIST_OF_MATIRIAL[int(helper[2].text)],
                            int(helper[1].text), int(helper[0].text))
                    for button in helper:
                        button.text = ''
                    if (offer.cost <= self.dollar_score):
                        self.dollar_score -= offer.cost
                        import server
                        server.server.put_contract(offer)
                if (self.add_button.rect.collidepoint(event.pos)):
                    if (self.dollar_score >= int(self.text_pole_make_offer[4].text)):
                        self.dollar_score -= int(self.text_pole_make_offer[4].text)
                        business.add_rub(int(self.text_pole_make_offer[4].text))
                    self.text_pole_make_offer[4].text = ''
                if (self.add_worker.rect.collidepoint(event.pos)):
                    if (self.dollar_score >= price_of_worker):
                        business.add_worker()
                        self.dollar_score -= price_of_worker



    def render_my_business(self):
        SCREEN.fill(SCREEN_COLOR)
        SCREEN.blit(self.background.image, self.background.rect)
        SCREEN.blit(self.logo.image, self.logo.rect)
        for button in self.my_business_buttons:
            button.draw(SCREEN)
        self.back_business.draw(SCREEN)
        pygame.display.flip()

    

    def check_events_my_business(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.business_running = False
                self.my_business_flag = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.business_running = False
                    self.my_business_flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if (self.back_business.rect.collidepoint(event.pos)):
                    self.my_business_flag = False
                for button in self.my_business_buttons:
                    if (button.rect.collidepoint(event.pos)):
                        self.my_own_business = True
                        self.now_write_in = 0
                        while(self.my_own_business):
                            self.render_my_own_business(button.business)
                            self.check_events_my_own_business(button.business)



    def render_business(self):
        SCREEN.fill(SCREEN_COLOR)
        SCREEN.blit(self.background.image, self.background.rect)
        SCREEN.blit(self.logo.image, self.logo.rect)
        for button in self.business_button:
            text = button.text
            button.text += " $ " + str(button.business.price)
            button.draw(SCREEN)
            button.check_if_available(self.dollar_score)
            button.text = text
        self.back_business.draw(SCREEN)
        self.my_business_button.draw(SCREEN)
        text_score_dollar = self.font.render("$" + str(self.dollar_score), True, FONT_COLOR)
        SCREEN.blit(text_score_dollar, (WIDTH / 20, HEIGHT / 20 + 200))
        pygame.display.flip()

    def check_events_business(self):        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.business_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.business_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.business_button:
                    if (button.rect.collidepoint(event.pos) 
                            and button.clicable(self.dollar_score)):
                        business, self.dollar_score = button.click(self.dollar_score)
                        self.my_business.append(copy.deepcopy(business))
                        self.my_business[-1].business_id = self.business_id
                        import server
                        server.server.data_base[self.business_id] = (server.user_name,
                                len(self.my_business) - 1)
                        self.business_id += 1

                if (self.back_business.rect.collidepoint(event.pos)):
                    self.business_running = False
                if (self.my_business_button.rect.collidepoint(event.pos)):
                    self.my_business_flag = True
                    self.my_business_buttons = init_list_this_button(self.my_business,
                            WIDTH, HEIGHT)
                    while (self.my_business_flag):
                        self.render_my_business()
                        self.check_events_my_business()

    def check_events(self):
        if pygame.time.get_ticks() - self.prev_tick >= 1000:
            self.dollar_score += self.auto_clicks
            self.prev_tick = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # space button is pressed
                    self.dollar_score += self.booster
                    for business in self.my_business:
                        business.work()
                elif event.key == pygame.K_ESCAPE:  # escape is pressed
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # right mouse click
                if self.upgradesCPS.rect.collidepoint(event.pos):
                    self.auto_clicks, self.rub_score = self.upgradesCPS.click(
                            self.auto_clicks, self.rub_score)
                    self.business_running = True
                    while (self.business_running):
                        self.render_business()
                        self.check_events_business()

                if self.upgradesCPC.rect.collidepoint(event.pos):
                    self.booster, self.dollar_score = self.upgradesCPC.click(
                            self.booster, self.dollar_score)
    def game_end(self):
        while self.running:
            self.render_win()
            self.check_events()

    def game_loop(self):
        while self.menu_running:
            self.render_menu()
            self.check_menu_events()

        while self.running:
            self.clock.tick(FPS)
            self.check_events()
            self.render_main()
def run():
    global game
    game = Game()
    game.game_loop()

