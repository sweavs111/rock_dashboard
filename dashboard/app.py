# core pygame loop
import pygame
import sys

import settings

class Dashboard:
    def __init__(self):
        self.screen = None

    def run(self):
        # pygame setup
        pygame.init()

        # setup window
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))