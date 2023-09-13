import sys
import pygame

def check_events():
    """respond to keypresses and mouse events"""
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """update images on the screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()

