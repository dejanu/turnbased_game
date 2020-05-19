
import pygame
pygame.init()


class Player(pygame.sprite.Sprite):
    '''This class represents the player'''
    def __init__(self, width, height):
        '''call the base (Sprite) constructor class'''
        super().__init__()

        # Create the hero
        self.image = pygame.image.load("hero.png")
        self.rect = self.image.get_rect()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screenDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)
pygame.display.set_caption('Hero Battle')

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = ( 0, 255,   0)
BLUE = ( 0,   0, 255)


heroImg = pygame.image.load('hero.png')
def hero(x = SCREEN_WIDTH * 0.5 , y = SCREEN_HEIGHT * 0.5 ):
    screenDisplay.blit(heroImg, (x,y))

beastImg = pygame.image.load('beast.png')
def beast(x = SCREEN_WIDTH * 0.25, y = SCREEN_HEIGHT * 0.25):
    screenDisplay.blit(beastImg, (x,y))

p = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
# List that contains all sprites in the game
active_sprites_list = pygame.sprite.Group()
# Add the sprites to the list of objects
active_sprites_list.add(p)

running = True
while running:

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Game logic goes here
    active_sprites_list.update()

    # Fill the background with white aka screenDisplay.fill((255, 255, 255))
    screenDisplay.fill(WHITE)

    
    # Draw characters
    #hero()
    
    # Draw sprites at once all/refresh the position of the player
    active_sprites_list.draw(screenDisplay)
    #screenDisplay.blit(p.image, p.rect)
 
   
    #pygame.display.flip()
    pygame.display.update()

# Done! Time to quit.
#pygame.quit()