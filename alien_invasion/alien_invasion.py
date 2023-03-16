import imp
import sys
import pygame
from ship import Ship
from setting import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")
    def run_game(self):
        while True:
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            self._check_events()
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()
            # pygame.display.flip()
            self._update_screen()
    def _check_events(self):
        """ 响应按键和鼠标事件 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
