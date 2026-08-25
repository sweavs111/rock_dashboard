import os
import pygame
import sys
import math
from datetime import timedelta

from .. import settings

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "..", "assets")

class Symbols:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 30)
        try:
            soap_icon = pygame.image.load(os.path.join(ASSETS_DIR, "soap-bar.png")).convert_alpha()
        except pygame.error:
            print("could not load image: make sure file path is correct.")
            sys.exit()
        self.soap_icon = pygame.transform.scale(soap_icon, (100, 100))

    def wash_step(self, screen, prog_entry):
        # wash time
        current_time = timedelta(milliseconds=pygame.time.get_ticks())
        wash_elapsed = current_time - prog_entry.wash_start
        wash_text = self.font.render(self._format_timestr(wash_elapsed), True, settings.WHITE)
        wash_text_rect = wash_text.get_rect()
        wash_text_rect.topleft = (prog_entry.rect.right + 30, prog_entry.rect.bottom - (prog_entry.rect.height / 3))
        
        #wash icon
        ms, _ = math.modf(wash_elapsed.total_seconds())
        if ms <= 0.5:
            soap_icon_rect = self.soap_icon.get_rect()
            soap_icon_rect.midbottom = (wash_text_rect.centerx, wash_text_rect.top-5)
            screen.blit(self.soap_icon, soap_icon_rect)
    
        screen.blit(wash_text, wash_text_rect)

    
    def _format_timestr(self, wash_elapsed):
        total_seconds = int(wash_elapsed.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, remainder = divmod(remainder, 60)
        return f"{hours:02}:{minutes:02}:{remainder:02}"