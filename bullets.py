"""
 Show how to fire bullets.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/PpdJjaiLX6A
"""
import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400

# --- Classes
 
 
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()

    def update(self):
        # Move the block one step down
        self.rect.y +=1

 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Update the player's position. """
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Set the player x position to the mouse x position
        self.rect.x = pos[0]
 
 
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
 
 
# --- Create the window
 
# Initialize Pygame
pygame.init()
 
screen = pygame.display.set_mode([screen_width, screen_height])

# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# --- Create the sprites
 
for i in range(50):
    # This represents a block
    block = Block(BLUE)
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(350)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player()
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Select the font to use, size, bold, italics
font = pygame.font.SysFont('comicsansms', 25, True, False)
# Render the text. "True" means anti-aliased text.
game_over_text = font.render("Game over!!!!", True, BLACK)

score = 0
player.rect.y = 370
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
 
    # --- Game logic
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
 
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
 
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)
 
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)


    block_player_list = pygame.sprite.spritecollide(player, block_list, True)
    if len(block_player_list) != 0:
        final_message = "Game Over !!!"
        done = True 

    for block in block_list:
        if block.rect.y >= screen_height:
            block.rect.y = 0

    if len(block_list) == 0:
        final_message = "You won!!!"
        done = True;
 
    # --- Draw a frame
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Draw all the spites
    all_sprites_list.draw(screen)

    # Write current score
    screen.blit(font.render("Score:" + str(score), True, BLACK), [10,10])

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)

# Clear the screen
screen.fill(WHITE)
 
screen.blit(font.render(final_message, True, BLACK), [350,200])
pygame.display.flip()
pygame.time.delay(3000)
 
pygame.quit()
