import pygame
import sys
from dashboard.app import Dashboard

if __name__ == "__main__":
    Dashboard().run()


pygame.display.set_caption("Draw a Box")

#Progress bar config
start_time=pygame.time.get_ticks()
TOTAL_DURATION = 5000 # 5 seconds

# rectangle list
rect_list = [
    pygame.Rect(100, 100, WIDTH/2-200, 100),
    pygame.Rect(100, 250, WIDTH/2-200, 100),
    pygame.Rect(100, 400, WIDTH/2-200, 100),
    pygame.Rect(100, 550, WIDTH/2-200, 100),
    pygame.Rect(WIDTH/2+100, 100, WIDTH/2-200, 100),
    pygame.Rect(WIDTH/2+100, 250, WIDTH/2-200, 100),
    pygame.Rect(WIDTH/2+100, 400, WIDTH/2-200, 100),
    pygame.Rect(WIDTH/2+100, 550, WIDTH/2-200, 100),
]


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

    
    # Draw boxes
    for rectangle in rect_list:
        pygame.draw.rect(screen, BLUE, rectangle, width=1, border_radius=20)
    
    # progress for the first bar
    progress_bar()

    # flip() the display to put your work on screen
    pygame.display.flip()

# Clean up and exit
pygame.quit()
sys.exit()
