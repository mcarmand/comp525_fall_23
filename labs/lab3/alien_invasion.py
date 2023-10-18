import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien

def run_game():
    """
    Initialize game and create a screen object.
    """
    ai_settings = Settings()

    pygame.init();
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen, ship, aliens)

    # main game loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == "__main__":
    run_game()
