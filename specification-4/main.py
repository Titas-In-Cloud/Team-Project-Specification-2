import pygame
from pygame.locals import (
   K_UP,
   K_DOWN,
   K_LEFT,
   K_RIGHT,
   K_ESCAPE,
   KEYDOWN,
   QUIT,
)


pygame.init()
screen_width = 1920
screen_height = 1080

# Set up the drawing window
screen = pygame.display.set_mode([screen_width, screen_height])

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

   # Fill the background with white
   screen.fill((255, 255, 255))

   surf = pygame.Surface((1500, 1000))
   surf.fill((0, 0, 0))
   rect = surf.get_rect()
   screen.blit(surf, (0, 0))

   # Draw a solid blue circle in the center
   img = pygame.image.load('./resources/98c.jpg')
   screen.blit(img, (0, 0))

   # Flip the display
   pygame.display.flip()

# Done! Time to quit.
pygame.quit()
