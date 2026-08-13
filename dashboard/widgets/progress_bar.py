# create a progress bar 
import pygame
from datetime import timedelta

from .. import settings

class ProgressBar:
    def __init__(self):
        self.font = pygame.font.Font(None, 25)
    def start_progress(self, screen, prog_bar, rect):
        # make a new rectangle for the progress bar
        prog_rect = rect.copy()

        #write timestamps
        self._write_timestamps(screen, prog_bar[1], rect)

        # calculate progress
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - prog_bar[0]
        progress_ratio=min(elapsed_time / settings.TOTAL_DURATION, 1)
        prog_rect.width = progress_ratio * prog_rect.width
        # draw rectangle
        if prog_rect.width < rect.width:
            pygame.draw.rect(screen, settings.BLUE, prog_rect, border_radius=20)
        else:
            pygame.draw.rect(screen, settings.GREEN, prog_rect, border_radius=20)
    
    def _render_label(self, timestamp, font, anchor_attr, anchor_x, rect):
        text = font.render(timestamp.strftime("%a, %b %d, %I:%M %p"), True, settings.BLACK)
        textRect = text.get_rect()
        # anchor_attr is the *name* of a Rect positioning attribute (e.g. "topleft",
        # "topright"); setattr() looks it up dynamically instead of hardcoding it,
        # so this one method can position either label.
        setattr(textRect, anchor_attr, (anchor_x, rect.y - 25))
        return text, textRect

    def _write_timestamps(self, screen, timestamp, rect):
        # start time
        text_start, textRect_start = self._render_label(
            timestamp, self.font, "topleft", rect.left, rect
        )

        # end time
        endtime = timestamp + timedelta(milliseconds=settings.TOTAL_DURATION)
        text_end, textRect_end = self._render_label(
            endtime, self.font, "topright", rect.right, rect
        )

        # draw timestamps
        screen.blits(((text_start, textRect_start), (text_end, textRect_end)))

