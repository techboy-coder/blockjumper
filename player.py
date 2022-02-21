# import pygame
# # # Player is a class that represents a player in the game.
# # # Player can only jump if it is on the ground.
# # # Player cannot move left and right
# # # Player can jump
# # # Player class
# # class Player(pygame.sprite.Sprite):
# #     # Constructor function
# #     def __init__(self, x, y):
# #         # Call the parent's constructor
# #         super().__init__()
# #         # Set height, width
# #         self.image = pygame.Surface([15, 15])

# #         # Color the surface cyan
# #         self.image.fill((0, 255, 255))
# #         # Set the position of the player
# #         self.rect = self.image.get_rect()
# #         self.rect.x = x
# #         self.rect.y = y
# #         # Set speed vector
# #         self.change_y = 0