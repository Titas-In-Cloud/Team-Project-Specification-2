import pygame
import random
from pygame.locals import (
    K_RETURN,
    KEYUP,
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
screen_width = 800
screen_height = 600
pygame.mixer.init()
move_up_sound = pygame.mixer.Sound("./practical-3/specification-4/resources/phaserUp5.ogg")
move_down_sound = pygame.mixer.Sound("./practical-3/specification-4/resources/phaserDown2.ogg")
collision_sound = pygame.mixer.Sound("./practical-3/specification-4/resources/zapThreeToneDown.ogg")
shoot_sound = pygame.mixer.Sound("./practical-3/specification-4/resources/laser4.ogg")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./practical-3/specification-4/resources/playerShip2_blue.png")
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.radius = 18
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height
        self.speed_x = 0
        self.speed_y = 0

    def update(self, pressed_keys):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.speed_x = 0
        self.speed_y = 0
        if pressed_keys[K_UP]:
            self.speed_y = -5
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.speed_y = 6
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.speed_x = -8
        if pressed_keys[K_RIGHT]:
            self.speed_x = 8

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

    def shoot(self):
        shoot_sound.play()
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.surf = pygame.image.load("./practical-3/specification-4/resources/laserBlue02.png")
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = -10

    def update(self, pressed_keys):
        self.rect.move_ip(0, -10)
        if self.rect.bottom < 0:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super(Meteor, self).__init__()
        self.surf = pygame.image.load("./practical-3/specification-4/resources/meteorBrown_big1.png")
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(150, screen_width - 150),
                random.randint(-150, -75),
            )
        )
        self.radius = 65
        self.speed_y = random.randint(2, 10)
        self.speed_x = random.randint(-3, 3)

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)
        if (self.rect.top > screen_height + 30 or self.rect.right >
            screen_width + 30 or self.rect.left < -30):
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("./practical-3/specification-4/resources/enemyRed1.png")
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center =(
                random.randint(screen_width / 2 - 200, screen_width / 2 + 200),
                random.randint(-100, -50)
            )
        )
        self.radius = 18
        self.speed_x = random.randint(-7, 7)
        self.speed_y = random.randint(-1, 1)

    def update(self):
        self.rect.move_ip(self.speed_x, self.speed_y)
        if (self.rect.top > screen_height + 30 or self.rect.right >
                screen_width + 30 or self.rect.left < -30):
            self.kill()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(EnemyBullet, self).__init__()
        self.surf = pygame.image.load("./practical-3/specification-4/resources/laserBlue02.png")
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speed_y = -10

    def update(self, pressed_keys):
        self.rect.move_ip(0, 10)
        if self.rect.top > screen_height:
            self.kill()


font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


pygame.init()
pygame.display.set_caption("Arterius")
clock = pygame.time.Clock()
result = 0
pygame.mixer.music.load("./practical-3/specification-4/resources/background.mp3")
pygame.mixer.music.play(loops=-1)
screen = pygame.display.set_mode([screen_width, screen_height])
background = pygame.image.load("./practical-3/specification-4/resources/starfield.png")
ADDMETEOR = pygame.USEREVENT + 1
pygame.time.set_timer(ADDMETEOR, 250)
ADDENEMY = pygame.USEREVENT + 2
pygame.time.set_timer(ADDENEMY, 1000)

player = Player()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
meteors = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Run until the user asks to quit
menu = True
while menu:
    screen.blit(background, background.get_rect())
    draw_text(screen, "Arterius", 80, screen_width / 2, screen_height / 4)
    draw_text(screen, "To move use arrow keys, to shoot press space", 30,
              screen_width / 2, screen_height / 2)
    draw_text(screen, "Press enter to continue", 22, screen_width / 2, screen_height * 3 / 4)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                running = False
                                menu = False

                            elif event.key == pygame.K_SPACE:
                                player.shoot()

                        elif event.type == QUIT:
                            running = False

                        elif event.type == ADDMETEOR:
                            new_meteor = Meteor()
                            meteors.add(new_meteor)
                            all_sprites.add(new_meteor)

                        elif event.type == ADDENEMY:
                            new_enemy = Enemy()
                            enemies.add(new_enemy)
                            all_sprites.add(new_enemy)

                    pressed_keys = pygame.key.get_pressed()
                    player.update(pressed_keys)
                    bullets.update(pressed_keys)
                    meteors.update()
                    enemies.update()
                    screen.fill((0, 0, 0))
                    screen.blit(background, background.get_rect())

                    for entity in all_sprites:
                        screen.blit(entity.surf, entity.rect)

                    if pygame.sprite.spritecollide(player, meteors, False, pygame.sprite.collide_circle) or (
                            pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_circle)):
                        player.kill()
                        move_up_sound.stop()
                        move_down_sound.stop()
                        collision_sound.play()
                        screen.blit(background, background.get_rect())
                        draw_text(screen, "Game over", 120, screen_width / 2, screen_height / 4)
                        draw_text(screen, "Press any key to play again", 50, screen_width / 2, screen_height * 3 / 4)
                        draw_text(screen, "Your score was:" + " " + str(result), 40, screen_width / 2, screen_height / 2)
                        pygame.display.flip()
                        reset = True
                        while reset:
                            clock.tick(60)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()

                                if event.type == KEYUP:
                                    reset = False
                        all_sprites = pygame.sprite.Group()
                        meteors = pygame.sprite.Group()
                        bullets = pygame.sprite.Group()
                        enemies = pygame.sprite.group()
                        player = Player()
                        all_sprites.add(player)
                        result = 0
                    scores = pygame.sprite.groupcollide(meteors, bullets, True, True)
                    for score in scores:
                        result += 50
                    draw_text(screen, str(result), 20, 100, 10)

                    pygame.display.flip()
                    clock.tick(60)
            elif event.key == K_ESCAPE:
                pygame.quit()
        elif event.type == pygame.QUIT:
            pygame.quit()


pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
