import pygame
import sys

# pygame setup
pygame.init()

# size
w = 1280
h = 720

# setup window
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Draw a Box")

# define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

#Progress bar config
start_time=pygame.time.get_ticks()
TOTAL_DURATION = 5000 # 5 seconds

# dashboard loop
running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(WHITE)

    # calculate progress
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    progress_ratio=min(elapsed_time / TOTAL_DURATION, 1)

    progress_width = progress_ratio * (w/2 - 200)

    # Draw boxes left side
    pygame.draw.rect(screen, BLUE, (100, 100, w/2-200, 100), width=1, border_radius=20)
    # progress for the first bar
    pygame.draw.rect(screen, BLUE, (100, 100, progress_width, 100), border_radius=20)

    pygame.draw.rect(screen, BLUE, (100, 250, w/2-200, 100), width=1, border_radius=20)
    pygame.draw.rect(screen, BLUE, (100, 400, w/2-200, 100), width=1, border_radius=20)
    pygame.draw.rect(screen, BLUE, (100, 550, w/2-200, 100), width=1, border_radius=20)

    # Draw boxes right side 
    pygame.draw.rect(screen, BLUE, (w/2+100, 100, w/2-200, 100), width=1, border_radius=20)
    pygame.draw.rect(screen, BLUE, (w/2+100, 250, w/2-200, 100), width=1, border_radius=20)
    pygame.draw.rect(screen, BLUE, (w/2+100, 400, w/2-200, 100), width=1, border_radius=20)
    pygame.draw.rect(screen, BLUE, (w/2+100, 550, w/2-200, 100), width=1, border_radius=20)

    # flip() the display to put your work on screen
    pygame.display.flip()

# Clean up and exit
pygame.quit()
sys.exit
