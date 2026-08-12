# dashboard/widgets/panel.py
import pygame
from .. import settings
from . import progress_bar

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
    
    def _draw_tics(self, screen, rect):
        day = rect.width / 7
        i = 1
        while i < 7:
            x_pos = rect.x + (day * i)
            pygame.draw.line(screen, settings.BLACK, (x_pos, rect.y), (x_pos, rect.y + 10), 2)
            i += 1
    
    def draw(self, screen):
        for rect in self.rects:
            self._draw_tics(screen, rect)
            pygame.draw.rect(screen, settings.BLACK, rect, width=2, border_radius=20)

    def detect_click(self, event):
        for index, rect in enumerate(self.rects):
            if rect.collidepoint(event.pos):
                return index
        return None
