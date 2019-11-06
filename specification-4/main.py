import pygame
import random
from pygame.locals import (
   K_UP,
   K_DOWN,
   K_LEFT,
   K_RIGHT,
   K_ESCAPE,
   KEYDOWN,
   QUIT,
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def update1(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screen_width + 20, screen_width + 100),
                random.randint(0, screen_height),
            )
        )
        self.speed = random.randint(5, 20)


    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

pygame.init()
screen_width = 800
screen_height = 600


# Set up the drawing window
screen = pygame.display.set_mode([screen_width, screen_height])

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Run until the user asks to quit
running = True
while running:

   # Did the user click the window close button?
    for event in pygame.event.get():
       if event.type == KEYDOWN:
           if event.key == K_ESCAPE:
               running = False
       elif event.type == QUIT:
           running = False

    pressed_keys = pygame.key.get_pressed()

    player.update1(pressed_keys)
    # Fill the background with white
    screen.fill((255, 255, 255))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
