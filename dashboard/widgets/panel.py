# dashboard/widgets/panel.py
import pygame
from datetime import datetime
from zoneinfo import ZoneInfo

from .. import settings
from . import progress_bar

class Panel:
    def __init__(self):
        self.rects = self._build_rects()
        self.rect_index = 0
        self.progress_bar = progress_bar.ProgressBar()
        self.prog_bars = [() for _ in range(len(self.rects))] # format is start tick, date/time

    def _build_rects(self):
        w = settings.WIDTH
        return [
            pygame.Rect(50, 150, w/2-200, 100),
            pygame.Rect(w/2+50, 150, w/2-200, 100),
            pygame.Rect(50, 300, w/2-200, 100),
            pygame.Rect(w/2+50, 300, w/2-200, 100),
            pygame.Rect(50, 450, w/2-200, 100),
            pygame.Rect(w/2+50, 450, w/2-200, 100),
            pygame.Rect(50, 600, w/2-200, 100),
            pygame.Rect(w/2+50, 600, w/2-200, 100),
        ]
    
    def _draw_tics(self, screen, rect):
        day = rect.width / 7
        i = 1
        while i < 7:
            x_pos = rect.x + (day * i)
            pygame.draw.line(screen, settings.WHITE, (x_pos, rect.y), (x_pos, rect.y + 10), 2)
            i += 1
    
    def draw_rects(self, screen):
        # draw the ongoing progress bars
        for index, prog_bar in enumerate(self.prog_bars):
            if len(prog_bar) > 0:
                self.progress_bar.start_progress(screen, prog_bar, self.rects[index])
                
        # Draw all rectangles
        for index, rect in enumerate(self.rects):
            self._draw_tics(screen, rect)
            if index == self.rect_index:
                pygame.draw.rect(screen, settings.RED, rect, width=6, border_radius=20)
            else:
                pygame.draw.rect(screen, settings.WHITE, rect, width=2, border_radius=20)
        


    def detect_click(self, event):
        for index, rect in enumerate(self.rects):
            if rect.collidepoint(event.pos):
                return index
        return None

    def _render_header_text(self, font, input_text):
        text = font.render(input_text, True, settings.WHITE)
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

    def update_rect_index(self, keystroke_event):
        match keystroke_event:
            case pygame.K_LEFT:
                if self.rect_index % 2 == 0: # if even
                   self.rect_index += 1
                else:
                   self.rect_index -= 1
            case pygame.K_RIGHT:
                if self.rect_index % 2 != 0: # if odd
                    self.rect_index -= 1
                else:
                    self.rect_index += 1
            case pygame.K_UP:
                if self.rect_index < 2:
                    self.rect_index += 6
                else:
                    self.rect_index -= 2
            case pygame.K_DOWN:
                if self.rect_index > 5:
                    self.rect_index -= 6
                else:
                    self.rect_index += 2
            case pygame.K_RETURN:
                    self.prog_bars[self.rect_index] = (pygame.time.get_ticks(), datetime.now(ZoneInfo("America/New_York")))
