# core pygame loop
import pygame
import sys

from . import settings
from .widgets import panel, progress_bar

class Dashboard:
    def __init__(self):
        self.screen = None
        self.panel = None

    def run(self):
        pygame.init()

        self.panel = panel.Panel()

        # setup window
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        clock = pygame.time.Clock()
        pygame.display.set_caption("Rock Dashboard")
        self.panel.build_header()
        
        # setup controller support
        pygame.joystick.init()
        # Keep track of connected joysticks
        joysticks = {}

        # dashboard loop
        running = True
        while running:
            clock.tick(60)
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # xbox controller plugged in
                if event.type == pygame.JOYDEVICEADDED:
                    xbox = pygame.joystick.Joystick(event.device)
                    xbox.init()
                    joysticks[xbox.get_instance_id()] = xbox
                # xbox controller unplugged
                if event.type == pygame.JOYDEVICEREMOVED:
                    del joysticks[event.instance_id()]

                if event.type == pygame.KEYDOWN:
                    self.panel.update_rect_index(event.key)

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(settings.GREY)

            self.panel.draw_rects(self.screen)

            self.panel.draw_header(self.screen)

            # flip() the display to put your work on screen
            pygame.display.flip()

        # Clean up and exit
        pygame.quit()
        sys.exit()
