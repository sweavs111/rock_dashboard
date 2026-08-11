# dashboard/widgets/panel.py
import pygame
from .. import settings

class Panel:
    def __init__(self):
        self.rects = self._build_rects()

    def _build_rects(self):
        w = settings.WIDTH
        return [
            pygame.Rect(100, 100, w/2-200, 100),
            pygame.Rect(100, 250, w/2-200, 100),
            pygame.Rect(100, 400, w/2-200, 100),
            pygame.Rect(100, 550, w/2-200, 100),
            pygame.Rect(w/2+100, 100, w/2-200, 100),
            pygame.Rect(w/2+100, 250, w/2-200, 100),
            pygame.Rect(w/2+100, 400, w/2-200, 100),
            pygame.Rect(w/2+100, 550, w/2-200, 100),
        ]
    
    def draw(self, screen):
        for rect in self.rects:
            pygame.draw.rect(screen, settings.BLACK, rect, width=1, border_radius=20)
