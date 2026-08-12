# create a progress bar 
import pygame

from .. import settings

class ProgressBar:
    def start_progress(self, screen, start_time, rect):
        # make a new rectangle for the progress bar
        prog_rect = rect.copy()
        # calculate progress
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        progress_ratio=min(elapsed_time / settings.TOTAL_DURATION, 1)
        prog_rect.width = progress_ratio * prog_rect.width
        # draw rectangle
        pygame.draw.rect(screen, settings.BLUE, prog_rect, border_radius=20)

    
