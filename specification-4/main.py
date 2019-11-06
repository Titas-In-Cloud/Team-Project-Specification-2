import pygame
import random
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("./resources/ship (2).png").convert()
        self.surf.set_colorkey((136, 205, 250), RLEACCEL)
        self.rect = self.surf.get_rect(center=(
                random.randint(100, 600),
                random.randint(-150, -100),
        )
    )
    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.right < 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./resources/filimon stand.png").convert()
        self.surf.set_colorkey((136, 205, 250), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height


    def update(self):
        self.rect.move_ip(5, 0)
        if self.rect.right < 0:
            self.kill()


    def update1(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
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
        self.surf = pygame.image.load("./resources/barrel.png").convert()
        self.surf.set_colorkey((135, 206, 250), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(150, 550),
                random.randint(-150, -75),
            )
        )
        self.speed = random.randint(5, 20)


    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.right < 0:
            self.kill()


pygame.mixer.init()
pygame.init()
screen_width = 800
screen_height = 600
clock = pygame.time.Clock()

pygame.mixer.music.load("./resources/background.mp3")
pygame.mixer.music.play(loops=-1)
# Set up the drawing window
screen = pygame.display.set_mode([screen_width, screen_height])

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT +2
pygame.time.set_timer(ADDCLOUD, 1000)

player = Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
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

        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)


    move_up_sound = pygame.mixer.Sound("./resources/rising pitch.ogg")
    move_down_sound = pygame.mixer.Sound("./resources/falling pitch.ogg")
    collision_sound = pygame.mixer.Sound("./resources/beb.ogg")

    pressed_keys = pygame.key.get_pressed()
    player.update1(pressed_keys)

    enemies.update()
    clouds.update()
    # Fill the background with white
    screen.fill((135, 206, 250))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()
        running = False

    # Flip the display
    pygame.display.flip()
    clock.tick(15)
# Done! Time to quit.
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
