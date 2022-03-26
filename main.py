# Game inspired by chrome dino game
# Pygame Show sqaure on screen
from math import gamma
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from config import Config
config = Config()
# Initialize pygame
pygame.init()

from game import Game

# Startscreen class
class Startscreen:
    def __init__(self, config):
        self.config = config
        self.screen = pygame.display.set_mode((self.config.width, self.config.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.config.bg_color)
        self.font = pygame.font.SysFont("monospace", self.config.font_size)
        self.text = self.font.render("Press space to start", 1, self.config.font_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.centerx = self.background.get_rect().centerx
        self.text_rect.centery = self.background.get_rect().centery
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text, self.text_rect)
        pygame.display.flip()

    def update(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text, self.text_rect)
        pygame.display.flip()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
        return False

s = Startscreen(config)
while True:
    while True:
        if s.handle_events(pygame.event.get()):
            break
        s.update()
    game = Game()
    game.run()
    config.obstacle_speed = config.obstacle_start_speed
    # Check if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        