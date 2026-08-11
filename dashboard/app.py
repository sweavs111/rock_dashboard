# core pygame loop
import pygame
import sys

from . import settings
from .widgets import panel, progress_bar

class Dashboard:
    def __init__(self):

        
        self.screen = None
        self.panel = panel.Panel()

    def run(self):
        # pygame setup
        pygame.init()

        # setup window
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

        # set up progress bar
        start_time=pygame.time.get_ticks()
        self.progress_bar = progress_bar.ProgressBar()

        # dashboard loop
        running = True
        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(settings.WHITE)

            self.panel.draw(self.screen)
            
            # progress for the first bar
            self.progress_bar.start_progress(self.screen, start_time, self.panel.rects[0])

            # flip() the display to put your work on screen
            pygame.display.flip()

        # Clean up and exit
        pygame.quit()
        sys.exit()
