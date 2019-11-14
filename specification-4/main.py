# Importing libraries and functions
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
# Setting up the window's resolution, initializing music module and initiating the game
screen_width = 800
screen_height = 600
pygame.mixer.init()
pygame.init()


# Setting up classes


class Player(pygame.sprite.Sprite):
    """Sets up player, based on preexisting pygame sprite class"""
    def __init__(self):
        """Sets up player object"""
        super(Player, self).__init__()  # Allows class to inherit from pygame sprite class
        self.surf = pygame.image.load("./specification-4/resources/playerShip2_blue.png")  # Load the image
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)  # Allows image to blend in with the background and makes it faster
        self.rect = self.surf.get_rect()  # Allows manipulating coordinates
        self.radius = 18  # Sets radius for collision detection
        #  Starting position and speed
        self.rect.centerx = screen_width / 2
        self.rect.bottom = screen_height
        self.speed_x = 0
        self.speed_y = 0

    def update(self, pressed_keys):
        """Updates player object every frame, gets input from keyboard clicks"""
        # Player can move when pressing keys
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Sets starting speed to zero
        self.speed_x = 0
        self.speed_y = 0
        # When pressing an allowed key moves player by a given value
        if pressed_keys[K_UP]:
            self.speed_y = -6
            move_up_sound.play()  # Play sound when moving
        if pressed_keys[K_DOWN]:
            self.speed_y = 7
            move_down_sound.play()  # Play sound when moving
        if pressed_keys[K_LEFT]:
            self.speed_x = -8
        if pressed_keys[K_RIGHT]:
            self.speed_x = 8
        # Stops player from moving out of the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height

    def shoot(self):
        """Adds bullet sprite"""
        shoot_sound.play()
        bullet = Bullet(self.rect.centerx, self.rect.top)  # Sets starting location of a bullet
        # Add bullet to all the needed groups
        all_sprites.add(bullet)
        bullets.add(bullet)


class Bullet(pygame.sprite.Sprite):
    """Sets up bullet class, based on preexisting pygame sprite class"""
    def __init__(self, x, y):
        """Sets up bullet objects, takes input for starting location"""
        super(Bullet, self).__init__()  # Allows class to inherit from pygame sprite class
        self.surf = pygame.image.load("./specification-4/resources/laserBlue02.png")  # Load the image
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)  # Allows image to blend in with the background and makes it faster
        self.rect = self.surf.get_rect()
        # Part of a code allowing bullet to spawn at the top of the player sprite
        self.rect.bottom = y
        self.rect.centerx = x
        # Sets speed
        self.speed_y = -11

    def update(self, pressed_keys):
        """Updates bullet object every frame, takes input from keyboard"""
        # Moves bullet every frame, and stops processing it if it gets out of screen
        self.rect.move_ip(0, self.speed_y)
        if self.rect.bottom < 0:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    """Sets up meteor class, based on preexisting pygame sprite class"""
    def __init__(self):
        """Sets up meteor objects"""
        super(Meteor, self).__init__()  # Allows class to inherit from pygame sprite class
        self.surf = pygame.image.load("./specification-4/resources/meteorBrown_big1.png")  # Load the image
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)  # Allows image to blend in with the background and makes it faster
        # Set the starting random positions
        self.rect = self.surf.get_rect(
            center=(
                random.randint(150, screen_width - 150),
                random.randint(-150, -75),
            )
        )
        #  Collision detection
        self.radius = 65  # Sets radius for collision detection
        #  Moving speed
        self.speed_y = random.randint(2, 10)
        self.speed_x = random.randint(-3, 3)

    def update(self):
        """Updates meteor object every frame"""
        # Moves bullet every frame, and stops processing it if it gets out of screen
        self.rect.move_ip(self.speed_x, self.speed_y)
        if (self.rect.top > screen_height + 30 or self.rect.left >
                screen_width + 30 or self.rect.right < -30):
            self.kill()


class Enemy(pygame.sprite.Sprite):
    """Sets up enemy class, based on preexisting pygame sprite class"""
    def __init__(self):
        """Sets up enemy objects"""
        super(Enemy, self).__init__()  # Allows class to inherit from pygame sprite class
        self.surf = pygame.image.load("./specification-4/resources/enemyRed1.png")  # Load the image
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)  # Allows image to blend in with the background and makes it faster
        # Set the starting random positions
        self.rect = self.surf.get_rect(
            center=(random.randint(150, screen_width - 150),
                    random.randint(-50, -15),))
        self.radius = 18  # Sets radius for collision detection
        #  Moving speed part
        r = random.choice([(-6, -5), (5, 6)])  # Makes a random choice of either first or second group
        self.speed_x = random.randint(*r)
        self.speed_y = random.randint(3, 5)

    def update(self):
        """Updates enemy object every frame"""
        # Moves enemy every frame, and stops processing it if it gets out of screen
        self.rect.move_ip(self.speed_x, self.speed_y)
        if (self.rect.top > screen_height + 30 or self.rect.right >
                screen_width + 30 or self.rect.left < -30):
            self.kill()
        else:
            #  Shoot every frame
            shoot_sound.play()
            enemybullet = EnemyBullet(self.rect.centerx, self.rect.bottom)
            all_sprites.add(enemybullet)
            enemybullets.add(enemybullet)


class EnemyBullet(pygame.sprite.Sprite):
    """Sets up enemy bullet class, based on preexisting pygame sprite class"""
    def __init__(self, x, y):
        super(EnemyBullet, self).__init__()  # Allows class to inherit from pygame sprite class
        self.surf = pygame.image.load("./specification-4/resources/laserRed02.png")  # Load the image
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)  # Allows image to blend in with the background and makes it faster
        self.rect = self.surf.get_rect()
        # Starting location at the bottom of the enemy sprite
        self.rect.bottom = y
        self.rect.centerx = x
        # Speed
        self.speed_y = 6


    def update(self):
        """Updates enemy bullet object every frame"""
        # Moves bullet every frame, and stops processing it if it gets out of screen
        self.rect.move_ip(0, self.speed_y)
        if self.rect.top > screen_height:
            self.kill()


Arial = pygame.font.match_font('arial')


# This function draws given string on a screen
def write(surf, text, size, x, y):
    """Draws text given string, size and location"""
    font_size = pygame.font.Font(Arial, size)  # Sets the size
    text_surface = font_size.render(text, True, (255, 255, 255))  # Render text, sets color
    text_rect = text_surface.get_rect()  # Gets rectangles posistion
    text_rect.midtop = (x, y)  # Text position
    surf.blit(text_surface, text_rect)  # Push text


pygame.display.set_caption("Arterius") # Set the game title in the window
clock = pygame.time.Clock()  # Start the clock
result = 0 # Set the starting score
# Load the music
screen = pygame.display.set_mode([screen_width, screen_height]) # Sets the screen mode
pygame.mixer.music.load("./specification-4/resources/0595.ogg")
pygame.mixer.music.play(loops=-1)  # Loops sound indefinitely
move_up_sound = pygame.mixer.Sound("./specification-4/resources/phaserUp5.ogg")
move_down_sound = pygame.mixer.Sound("./specification-4/resources/phaserDown2.ogg")
collision_sound = pygame.mixer.Sound("./specification-4/resources/zapThreeToneDown.ogg")
shoot_sound = pygame.mixer.Sound("./specification-4/resources/laser4.ogg")

space = pygame.image.load("./specification-4/resources/starfield.png")  # Loads the background
# Add the events, set timers
add_meteor = pygame.USEREVENT + 1
# Since the last built in event is userevent,
# we can simply name it by adding a number
pygame.time.set_timer(add_meteor, 500)
add_enemy = pygame.USEREVENT + 2
pygame.time.set_timer(add_enemy, 2500)
# Add sprites to pygame groups
player = Player()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
meteors = pygame.sprite.Group()
enemybullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Run the game, menu loop sets the menu
menu = True
while menu:
    # Draw the background image
    screen.blit(space, space.get_rect())
    # Draw text
    write(screen, "Arterius", 80, screen_width / 2, screen_height / 4)
    write(screen, "To move use arrow keys, to shoot press space", 30,
              screen_width / 2, screen_height / 2)
    write(screen, "Press enter to continue", 22, screen_width / 2, screen_height * 3 / 4)
    pygame.display.flip()
    # True game loop
    for event in pygame.event.get():
        if event.type == KEYDOWN:  # If enter key is pressed the player is taken out of menu into the game
            if event.key == K_RETURN:
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:  # If player presses escape, they quit the game
                                running = False
                                menu = False

                            elif event.key == pygame.K_SPACE:
                                player.shoot()  # Calls shoot method from player

                        elif event.type == QUIT:
                            running = False  # If player presses X in the windows options they quit the game

                        # This part manages events - adding enemy spaceships and meteors
                        elif event.type == add_meteor:
                            new_meteor = Meteor()
                            meteors.add(new_meteor)
                            all_sprites.add(new_meteor)

                        elif event.type == add_enemy:
                            new_enemy = Enemy()
                            enemies.add(new_enemy)
                            all_sprites.add(new_enemy)
                            enemies.update()

                    pressed_keys = pygame.key.get_pressed()  # Gets updates for keyboard
                    # Update all the groups
                    player.update(pressed_keys)
                    bullets.update(pressed_keys)
                    meteors.update()
                    enemies.update()
                    enemybullets.update()
                    # Fill background with black
                    screen.fill((0, 0, 0))
                    # Push background image to the screen
                    screen.blit(space, space.get_rect())
                    # Draw all sprites
                    for sprite in all_sprites:
                        screen.blit(sprite.surf, sprite.rect)
                    # Lose conditions
                    if pygame.sprite.spritecollide(player, meteors, False, pygame.sprite.collide_circle) or (
                            pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_circle)) or (
                            pygame.sprite.spritecollide(player, enemybullets, False, pygame.sprite.collide_circle)):
                        # Ends running processes
                        player.kill()
                        shoot_sound.stop()
                        move_up_sound.stop()
                        move_down_sound.stop()
                        # Draw game over screen
                        collision_sound.play()
                        screen.blit(space, space.get_rect())
                        write(screen, "Game over", 120, screen_width / 2, screen_height / 4)
                        write(screen, "Press any key to play again", 50, screen_width / 2, screen_height * 3 / 4)
                        write(screen, "Your score was:" + " " + str(result), 40, screen_width / 3, screen_height / 3)
                        pygame.display.flip()
                        # Reinitializes the game
                        reset = True
                        while reset:
                            clock.tick(60)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                #  Starts the next game when player "unclicks" a key
                                if event.type == KEYUP:
                                    reset = False
                        all_sprites = pygame.sprite.Group()
                        meteors = pygame.sprite.Group()
                        bullets = pygame.sprite.Group()
                        enemies = pygame.sprite.Group()
                        enemybullets = pygame.sprite.Group()
                        player = Player()
                        all_sprites.add(player)
                        result = 0
                    # Scoring logic
                    meteors_shot_down = pygame.sprite.groupcollide(meteors, bullets, True, True)
                    enemies_down = pygame.sprite.groupcollide(enemies, bullets, True, True)
                    for meteor in meteors_shot_down:
                        result += 50
                    for enemy_down in enemies_down:
                        result += 50
                    # Draw score
                    write(screen, str(result), 20, 100, 10)

                    pygame.display.flip()
                    # Framerate
                    clock.tick(60)
            elif event.key == K_ESCAPE:
                pygame.quit()
        elif event.type == pygame.QUIT:
            pygame.quit()

# Stops the game
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()
