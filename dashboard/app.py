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
        # Keep track of connected joysticks
        joysticks = {}

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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # 1 represents the left mouse button
                        index = self.panel.detect_click(event)
                        if index is not None:
                            prog_bars[index] = (pygame.time.get_ticks(), datetime.now(ZoneInfo("America/New_York")))

                # xbox controller plugged in
                if event.type == pygame.JOYDEVICEADDED:
                    xbox = pygame.joystick.Joystick(event.device)
                    xbox.init()
                    joysticks[xbox.get_instance_id()] = xbox
                # xbox controller unplugged
                if event.type == pygame.JOYDEVICEREMOVED:
                    del joysticks[event.instance_id()]

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
