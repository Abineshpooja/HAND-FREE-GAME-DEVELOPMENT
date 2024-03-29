import pygame
import sys
from settings import *
from background import Background
import ui
class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.background = Background()
        self.click_sound = pygame.mixer.Sound(f"Assets/Sounds/slap.wav")
    def draw(self):
        self.background.draw(self.surface)
        ui.draw_text(self.surface, GAME_TITLE1, (SCREEN_WIDTH//2, 150), COLORS["title"], font=FONTS["big"],
                    shadow=True, shadow_color=(255,255,255), pos_mode="center")
        ui.draw_text(self.surface, GAME_TITLE2, (SCREEN_WIDTH // 2, 70), COLORS["title"], font=FONTS["small"],
                     shadow=True, shadow_color=(34,139, 34), pos_mode="center")
    def update(self):
        self.draw()
        if ui.button(self.surface, 320, "START", click_sound=self.click_sound):
            return "game"
        if ui.button(self.surface, 320+BUTTONS_SIZES[1]*1.5, "Quit", click_sound=self.click_sound):
            pygame.quit()
            sys.exit()
