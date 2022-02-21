# Game inspired by chrome dino game
# Pygame Show sqaure on screen
import pygame
# Initialize pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((800, 600))
# Set the title of the window
pygame.display.set_caption("Pygame Show Square")

# Config
GroundHeight = 100
PlayerSize = 70
Gravity = 1
JumpUp = -17
FPS = 60
PlayerColor = pygame.Color("#e71d36")
GroundColor = pygame.Color("#011627")
PlayerToLeft = 200
# Background Color
BackgroundColor = pygame.Color("#fdfffc55")
# Background surface
background = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
background.fill(BackgroundColor)

# Show ground a blue ground function
def showGround():
    # Draw ground
    pygame.draw.rect(screen, GroundColor, (0, screen.get_height() - GroundHeight, screen.get_width(), GroundHeight))

# Player is a class that represents a player in the game.

class Player(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self):
        # Call the parent's constructor
        super().__init__()
        # Set height, width
        self.image = pygame.Surface([PlayerSize, PlayerSize])
        # Color the surface cyan
        self.image.fill(PlayerColor)
        # Set the position of the player
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2 - PlayerToLeft
        self.rect.y = screen.get_height() - GroundHeight - PlayerSize
        self.change_y = 0

        # Jumping
        self.isJumping = False
        self.hasDoubleJumped = False


    # Jump
    def jump(self):
        # If player hasn't doubled jumped or jumped then jump
        if not self.isJumping and not self.hasDoubleJumped:
            self.isJumping = True
            self.change_y = JumpUp

        
        # If player has jumped but not doubled then double jump
        elif self.isJumping and not self.hasDoubleJumped:
            self.hasDoubleJumped = True
            self.change_y = JumpUp
        
                
        
    
    # Draw the player
    def draw(self):
        screen.blit(self.image, self.rect)

    # Update the player
    def update(self):
        # Move player down
        self.change_y += Gravity
        self.rect.y += self.change_y
        # If player is on the ground then reset double jump
        if self.rect.y >= screen.get_height() - GroundHeight - PlayerSize:
            self.isJumping = False
            self.hasDoubleJumped = False
            self.rect.y = screen.get_height() - GroundHeight - PlayerSize
            self.change_y = 0
        
# Obstacle is a class that represents an obstacle in the game.


# Create a player
player = Player()


# Main loop
running = True
clock = pygame.time.Clock()
while running:
    # Event handling
    for event in pygame.event.get():
        # Quit the game
        if event.type == pygame.QUIT:
            running = False
        # Jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Show background
    screen.blit(background, (0, 0))
    # Show ground
    showGround()
    # Update the player
    player.update()
    # Draw the player
    player.draw()
    # Update the screen
    pygame.display.flip()
    # Set the FPS
    clock.tick(FPS)
# Quit pygame
pygame.quit()
# Exit the program
exit()