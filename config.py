import pygame

class Config:
    def __init__(self) -> None:
        self.width = 800
        self.height = 600

        self.fps = 60
        self.title = "Dino Game"

        self.bg_color = pygame.Color("#e6e8e666")
        self.ground_color = pygame.Color("#080708")
        self.player_color = pygame.Color("#ffb703")
        self.solid_color = pygame.Color("#d9d9d9")
        # self.obstacle_color = pygame.Color("#284b63")
        self.obstacle_color = pygame.Color("#df2935")

        self.gravity = 0.5
        self.ground_size = 80
        self.player_size = 50
        self.obstacle_size = 60
        self.obstacle_speed = -6
        self.player_start_distance_from_left = 100
        self.player_start_lives = 3
        self.min_distance_between_obstacles = 70 + self.obstacle_size
        self.player_jump_speed = -10

        self.font_size = 30
        self.font_color = pygame.Color("#ffffff")
        self.score_width = 100
        self.score_height = 50
        

    def increase_obstacle_speed(self):
        self.obstacle_speed -= 0.3

        

        
    