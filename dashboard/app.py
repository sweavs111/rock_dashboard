# core pygame loop
import pygame
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

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
        pygame.display.set_caption("Rock Dashboard")
        self.header = self.panel.build_header()
        
        # setup controller support
        pygame.joystick.init()

        # set up progress bar
        self.progress_bar = progress_bar.ProgressBar()
        prog_bars = [() for _ in range(len(self.panel.rects))] # format is start tick, date/time

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
                            prog_bars[index] = (pygame.time.get_ticks(), datetime.now(ZoneInfo("America/New_York")))


            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(settings.GREY)
            
            for index, prog_bar in enumerate(prog_bars):
                if len(prog_bar) > 0:
                    self.progress_bar.start_progress(self.screen, prog_bar, self.panel.rects[index])

            self.panel.draw_rects(self.screen)

            self.panel.draw_header(self.screen)

            # flip() the display to put your work on screen
            pygame.display.flip()

        # Clean up and exit
        pygame.quit()
        sys.exit()
