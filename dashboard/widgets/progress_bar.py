# create a progress bar 
import pygame

class ProgressBar:
    def progress_bar(self):
    # calculate progress
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    progress_ratio=min(elapsed_time / TOTAL_DURATION, 1)
    progress_width = progress_ratio * (WIDTH/2 - 200)
    # draw rectangle
    pygame.draw.rect(screen, BLUE, (100, 100, progress_width, 100), border_radius=20)


    
