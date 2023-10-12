import sys
import pygame

def check_events(ship):
    """respond to keypresses and mouse events"""
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()

        elif ev.type == pygame.KEYDOWN:
            check_keydown_events(ev, ship);

        elif ev.type == pygame.KEYUP:
            check_keyup_events(ev, ship);


def check_keydown_events(ev, ship):
    """respond to keypresses"""
    if ev.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif ev.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(ev, ship):
    """respond to key releases"""
    if ev.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif ev.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """update images on the screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()
