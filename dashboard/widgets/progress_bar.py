# create a progress bar 
import pygame
from datetime import datetime, timedelta

from .. import settings

class ProgressBar:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 20)
    def start_progress(self, screen, prog_bar, rect):
        # make a new rectangle for the progress bar
        prog_rect = rect.copy()

        current_time = timedelta(milliseconds=pygame.time.get_ticks())
        if prog_bar.paused:
            prog_bar.current_pausetime = current_time - prog_bar.pause_tick

        # calculate progress if not finished
        if not prog_bar.finish:
            prog_bar.end_timestamp = prog_bar.start_timestamp + settings.TOTAL_DURATION + prog_bar.current_pausetime + prog_bar.total_pausetime
            prog_bar.elapsed_time = current_time - prog_bar.start_tick - prog_bar.current_pausetime - prog_bar.total_pausetime
            progress_ratio=min(prog_bar.elapsed_time / settings.TOTAL_DURATION, 1)
            prog_rect.width = progress_ratio * prog_rect.width
            if progress_ratio >= 1:
                prog_bar.finish = True
 
        # draw rectangle
        if not prog_bar.finish:
            pygame.draw.rect(screen, settings.BLUE, prog_rect, border_radius=20)
        else:
            pygame.draw.rect(screen, settings.GREEN, prog_rect, border_radius=20)

        #write timestamps
        self._write_timestamps(screen, prog_bar, rect)
    
    def _render_label(self, timestamp, font, anchor_attr, anchor_x, rect):
        text = font.render(timestamp.strftime("%a, %b %d, %I:%M %p"), True, settings.WHITE)
        textRect = text.get_rect()
        # anchor_attr is the *name* of a Rect positioning attribute (e.g. "topleft",
        # "topright"); setattr() looks it up dynamically instead of hardcoding it,
        # so this one method can position either label.
        setattr(textRect, anchor_attr, (anchor_x, rect.y - 25))
        return text, textRect

    def _write_timestamps(self, screen, prog_bar, rect):
        # start time
        text_start, textRect_start = self._render_label(
            prog_bar.start_timestamp, self.font, "topleft", rect.left, rect
        )

        # end time
        text_end, textRect_end = self._render_label(
            prog_bar.end_timestamp, self.font, "topright", rect.right, rect
        )

        # draw timestamps
        screen.blits(((text_start, textRect_start), (text_end, textRect_end)))

