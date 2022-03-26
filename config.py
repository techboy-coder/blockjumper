import pygame

class Config:
    def __init__(self) -> None:
        self.width = 800
        self.height = 600

        self.fps = 60
        self.title = "Dino Game"

        self.bg_color = pygame.Color("#ffffff55")
        self.ground_color = pygame.Color("#212529")
        self.player_color = pygame.Color("#5463FF")
        self.solid_color = pygame.Color("#ECECEC")
        # self.obstacle_color = pygame.Color("#284b63")
        self.obstacle_color = pygame.Color("#FF1818")

        self.player_gravity = 0.9
        self.ground_size = 120
        self.player_size = 60
        self.player_speed = 5
        self.obstacle_size = 40
        self.obstacle_start_speed = -4
        self.obstacle_speed = self.obstacle_start_speed
        self.player_start_distance_from_left = 100
        self.player_lives = 3
        self.min_distance_between_obstacles = 350 + self.obstacle_size
        self.player_jump_speed = 24

        self.font_size = 30
        self.font_color = pygame.Color("#000000")
        self.score_width = 100
        self.score_height = 50

        self.player_start_distance_from_wall = self.player_size + 100
        

    def increase_obstacle_speed(self):
        self.obstacle_speed -= 0.3

        

        
    