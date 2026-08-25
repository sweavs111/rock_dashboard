import pygame
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Wash:
    wash_start: timedelta

class Symbols:
    def wash_step(self, screen, prog_entry):
        current_time = pygame.time.get_ticks()
        wash_elapsed = current_time - prog_entry.current_wash.wash_start
