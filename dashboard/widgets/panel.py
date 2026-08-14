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
            pygame.Rect(50, 150, w/2-200, 100),
            pygame.Rect(50, 300, w/2-200, 100),
            pygame.Rect(50, 450, w/2-200, 100),
            pygame.Rect(50, 600, w/2-200, 100),
            pygame.Rect(w/2+50, 150, w/2-200, 100),
            pygame.Rect(w/2+50, 300, w/2-200, 100),
            pygame.Rect(w/2+50, 450, w/2-200, 100),
            pygame.Rect(w/2+50, 600, w/2-200, 100),
        ]
    
    def _draw_tics(self, screen, rect):
        day = rect.width / 7
        i = 1
        while i < 7:
            x_pos = rect.x + (day * i)
            pygame.draw.line(screen, settings.BLACK, (x_pos, rect.y), (x_pos, rect.y + 10), 2)
            i += 1
    
    def draw_rects(self, screen):
        for rect in self.rects:
            self._draw_tics(screen, rect)
            pygame.draw.rect(screen, settings.BLACK, rect, width=2, border_radius=20)

    def detect_click(self, event):
        for index, rect in enumerate(self.rects):
            if rect.collidepoint(event.pos):
                return index
        return None

    def _render_header_text(self, font, input_text):
        text = font.render(input_text, True, settings.BLACK)
        text_rect = text.get_rect()
        if input_text == "Tumble Bee":
            text_rect.center = (settings.WIDTH * 0.25, 60)
        else:
            text_rect.center = (settings.WIDTH * 0.75, 60)
        return (text, text_rect)

    def build_header(self):
         self.header = []
         self.font = pygame.font.SysFont("Arial", 50)
         for input_text in ["Tumble Bee", "Lortone"]:
            self.header.append(self._render_header_text(self.font, input_text))


    def draw_header(self, screen):
        screen.blits(self.header)