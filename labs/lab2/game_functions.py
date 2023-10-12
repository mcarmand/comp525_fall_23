import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """respond to keypresses and mouse events"""
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()

        elif ev.type == pygame.KEYDOWN:
            check_keydown_events(ev, ai_settings, screen, ship, bullets);

        elif ev.type == pygame.KEYUP:
            check_keyup_events(ev, ai_settings, screen, ship, bullets);


def check_keydown_events(ev, ai_settings, screen, ship, bullets):
    """respond to keypresses"""
    if ev.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif ev.key == pygame.K_LEFT:
        ship.moving_left = True

    elif ev.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(ev, ai_settings, screen, ship, bullets):
    """respond to key releases"""
    if ev.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif ev.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)



def update_bullets(bullets):
    """Update position of bullets and remove old ones"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(ai_settings, screen, ship, bullets):
    """update images on the screen"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()
