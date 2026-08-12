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
        clock = pygame.time.Clock()

        # set up progress bar
        self.progress_bar = progress_bar.ProgressBar()
        prog_bars = [None] * len(self.panel.rects)

        # dashboard loop
        running = True
        while running:
            clock.tick(60)
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 1 represents the left mouse button
                        index = self.panel.detect_click(event)
                        if index is not None:
                            prog_bars[index] = pygame.time.get_ticks()


            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(settings.WHITE)


            
            for index, start_time in enumerate(prog_bars):
                if start_time is not None:
                    self.progress_bar.start_progress(self.screen, start_time, self.panel.rects[index])

            self.panel.draw(self.screen)

            # flip() the display to put your work on screen
            pygame.display.flip()

        # Clean up and exit
        pygame.quit()
        sys.exit()
