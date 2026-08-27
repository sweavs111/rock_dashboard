# dashboard/widgets/panel.py
import pygame
import os
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from dataclasses import dataclass

from .. import settings
from . import progress_bar

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "assets")

@dataclass
class ProgressEntry:
    rect: pygame.Rect
    start_tick: timedelta
    start_timestamp: datetime
    elapsed_time: timedelta = timedelta()
    current_pausetime: timedelta = timedelta(0)
    total_pausetime: timedelta = timedelta(0)
    pause_tick: datetime = None
    endtime: datetime = None
    paused: bool = False
    finish: bool = False
    washing: bool = False
    wash_start = timedelta

class Panel:
    def __init__(self):
        self.rects = self._build_rects()
        self.rect_index = 0
        self.progress_bar = progress_bar.ProgressBar()
        self.prog_bars: list[ProgressEntry | None] = [None] * len(self.rects)
        self._load_pictures()

    def _build_rects(self):
        # this order makes the indexes of the rectangles
        # 0 1
        # 2 3
        # 4 5
        # 6 7
        # Makes the hard-coded index hopping via key presses work
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
            if prog_bar is not None:
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
            self.bee_rect1.midright = (text_rect.left-20, text_rect.centery)
            self.bee_rect2.midleft = (text_rect.right+20, text_rect.centery)
        else:
            text_rect.center = (settings.WIDTH * 0.75, 60)
            self.rock_rect1.midright = (text_rect.left-20, text_rect.centery)
            self.rock_rect2.midleft = (text_rect.right+20, text_rect.centery)
        return (text, text_rect)

    def build_header(self):
        self.header = []
        self.font = pygame.font.SysFont("Arial", 50)
        for input_text in ["Tumble Bee", "Lortone"]:
           self.header.append(self._render_header_text(self.font, input_text))
        icon_header = (
            (self.bee_icon, self.bee_rect1),
            (self.bee_icon, self.bee_rect2),
            (self.rock_icon, self.rock_rect1),
            (self.rock_icon, self.rock_rect2),
        )
        self.header += icon_header


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
                if self.prog_bars[self.rect_index] is None: # if theres no entry create a new one
                     self.prog_bars[self.rect_index] = ProgressEntry(
                         rect=self.rects[self.rect_index],
                         start_tick=timedelta(milliseconds=pygame.time.get_ticks()),
                         start_timestamp=datetime.now(ZoneInfo("America/New_York"))
                    )
                     self.prog_bars[self.rect_index].endtime = self.prog_bars[self.rect_index].start_tick + settings.TOTAL_DURATION
                elif not self.prog_bars[self.rect_index].paused and not self.prog_bars[self.rect_index].finish: #if the progress bar isn't paused and isn't finished, pause it
                    self.prog_bars[self.rect_index].paused = True
                    self.prog_bars[self.rect_index].pause_tick = timedelta(milliseconds=pygame.time.get_ticks())
                elif self.prog_bars[self.rect_index].paused and not self.prog_bars[self.rect_index].finish: # if the progress bar just got unpaused, reset the start tick
                    self.prog_bars[self.rect_index].total_pausetime += self.prog_bars[self.rect_index].current_pausetime
                    self.prog_bars[self.rect_index].current_pausetime = timedelta(0)
                    self.prog_bars[self.rect_index].pause_tick = None
                    self.prog_bars[self.rect_index].paused = False
                elif self.prog_bars[self.rect_index].finish:
                    self.prog_bars[self.rect_index].washing = True
                    self.prog_bars[self.rect_index].wash_start = timedelta(milliseconds=pygame.time.get_ticks())
            case pygame.K_BACKSPACE:
                self.prog_bars[self.rect_index] = None

    def _load_pictures(self):
        try:
            bee_icon = pygame.image.load(os.path.join(ASSETS_DIR, "bee.png")).convert_alpha()
        except pygame.error:
            print("could not load bee image: make sure file path is correct.")
            sys.exit()
        self.bee_icon = pygame.transform.scale(bee_icon, (settings.ICON_SIZE, settings.ICON_SIZE))
        self.bee_rect1 = self.bee_icon.get_rect()
        self.bee_rect2 = self.bee_rect1.copy()
        try:
            rock_icon = pygame.image.load(os.path.join(ASSETS_DIR, "rock.png")).convert_alpha()
        except pygame.error:
            print("could not load bee image: make sure file path is correct.")
            sys.exit()
        self.rock_icon = pygame.transform.scale(rock_icon, (settings.ICON_SIZE, settings.ICON_SIZE))
        self.rock_rect1 = self.rock_icon.get_rect()
        self.rock_rect2 = self.rock_rect1.copy()
