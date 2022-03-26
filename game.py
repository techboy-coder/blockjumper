import random
import pygame
import pygame.gfxdraw
from config import Config

config = Config()

class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((config.width, config.height))
        self.screen.fill(config.bg_color)
        self.clock = pygame.time.Clock()
        self.running = True
        self.config = config
        self.bg = pygame.Surface(self.screen.get_size(),pygame.SRCALPHA)
        self.bg.fill(self.config.bg_color)

        # Ground
        self.ground = Ground(self.screen, config)
        self.obstacles = []

        # Player
        self.player = Player(self.screen, config)
        self.player_lives = config.player_lives
        self.score = 0

    # Spawn obstacles every 1 to 4 seconds randomly using random.randint function
    def spawn_obstacles(self):
        r = random.randint(1, 3*self.config.fps//20)
        # r = random.randint(1, 3)
        if r == 1:
            # self.obstacles.append(Obstacle(self.screen, config))
            # Only spawn new obstacle if not too close to previous one
            if len(self.obstacles) == 0:
                self.obstacles.append(Obstacle(self.screen, config))
            elif self.obstacles[-1].rect.x < self.config.width - self.config.min_distance_between_obstacles:
                self.obstacles.append(Obstacle(self.screen, config))

            


    def run(self):
        config.obstacle_speed = config.obstacle_start_speed
        while self.running:
            self.clock.tick(config.fps)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                quit()
            if event.type == pygame.KEYDOWN:# and event.key == pygame.K_SPACE:
                self.player.jump()


            
    def update(self):
        self.spawn_obstacles()
        for obstacle in self.obstacles:
            obstacle.update()
        
        for o in range(len(self.obstacles)):
            try:
                if self.obstacles[o].destroy:
                    self.obstacles.pop(o)
            except:
                pass

        self.player.update()
        # Check if player collides with any obstacle
        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                self.player_lives -= 1
                print(self.player_lives)
                if self.player_lives == 0:
                    self.running = False
                else:
                    self.player.reset()
                    self.obstacles = []
                    # self.score = 0
        
        # Add score
        self.score += 1
        if int(self.score) == self.score and self.score != 0 and self.score % 80 == 0:
            config.obstacle_speed -= 0.4
        # self.player.jump_speed += 0.1
        # self.player.gravity += 0.0001
        # print(config.obstacle_speed)
        # print(self.player.jump_speed)
                    

    def show_score(self):
        # Font is fira code
        font = pygame.font.SysFont("Fira Code", self.config.font_size)
        text = font.render("Score: " + str(int(self.score)), True, self.config.font_color)
        text_rect = text.get_rect()
        text_rect.center = (100, 40)
        self.screen.blit(text, text_rect)
    
    def show_lives(self):
        font = pygame.font.SysFont("Fira Code", self.config.font_size)
        text = font.render("Lives: " + str(self.player_lives), True, self.config.font_color)
        text_rect = text.get_rect()
        text_rect.center = (self.config.width - 100, 40)
        self.screen.blit(text, text_rect)



    def draw(self):
        self.draw_background()
        self.ground.draw()
        for obstacle in self.obstacles:
            obstacle.draw()
        self.player.draw()
        self.show_score()
        self.show_lives()
        pygame.display.flip()
        

    def draw_background(self):
        self.screen.blit(self.bg, (0, 0))        


# Ground takes whole width of screen and height of ground_size
class Ground:
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config
        self.rect = pygame.Rect(0, config.height - config.ground_size, config.width, config.ground_size)
        self.color = config.ground_color
        self.draw()
        

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


# Obstacles are squares moving right to left
class Obstacle:
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config
        # Rect is square starting at right side of screen on ground
        self.rect = pygame.Rect(config.width, config.height - config.ground_size - config.obstacle_size, config.obstacle_size, config.obstacle_size)
        self.color = config.obstacle_color
        self.speed = config.obstacle_speed
        self.draw()
        self.destroy = False

    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        draw_rounded_rect(self.screen, self.rect, self.color, self.config.obstacle_size//8)

    def update(self):
        self.rect.x += self.speed
        # If obstacle goes off screen, destroy it
        if self.rect.x < - self.config.obstacle_size:
            self.destroy = True

# Player is a square
# Starts on ground on config.player_start_distance_from_wall
# Player can only jump if it is on the ground
# Player.x stays constant and cannot change
# Player.y can change
# Player speed is config.player_speed and is jumping speed
# Gravity is config.player_gravity and pulls player down when it is not on the ground
# Player can only jump if it is on the ground
class Player:
    def __init__(self, screen, config):
        self.screen = screen
        self.config = config
        self.rect = pygame.Rect(config.player_start_distance_from_wall, config.height - config.ground_size - config.player_size, config.player_size, config.player_size)
        self.color = config.player_color
        self.speed = config.player_speed
        # Gravity affects player.jump_speed
        self.gravity = config.player_gravity
        self.jump_speed = config.player_jump_speed
        self.is_jumping = False
        self.is_double_jumping = False


    def init_position(self):
        self.rect.x = self.config.player_start_distance_from_wall
        self.rect.y = self.config.height - self.config.ground_size - self.config.player_size

    def check_if_collides_and_return_bool(self, obstacles):
        return any(self.rect.colliderect(obstacle.rect) for obstacle in obstacles)
    
    def update(self):
        # Gravity affects player.jump_speed
        self.rect.y -= self.jump_speed
        self.jump_speed -= self.gravity
        # Stop player from falling through ground
        if self.rect.y > self.config.height - self.config.ground_size - self.config.player_size:
            # Put player back on ground
            self.init_position()
            # Stop player from jumping
            self.is_jumping = False
            self.is_double_jumping = False

    def jump(self):
        # Player can only jump if it is on the ground and not already jumping
        if self.rect.y >= self.config.height - self.config.ground_size - self.config.obstacle_size - self.config.player_size and not self.is_jumping:
            self.is_jumping = True
            self.jump_speed = self.config.player_jump_speed
        
        # Player can only double jump if it is jumping
        if self.is_jumping and not self.is_double_jumping:
            self.is_double_jumping = True
            self.jump_speed = self.config.player_jump_speed
        
        else:
            self.stop_jumping()

    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        draw_rounded_rect(self.screen, self.rect, self.color, self.config.player_size//7)
    
    def stop_jumping(self):
        self.is_jumping = False
        self.jump_speed = -self.config.player_jump_speed * 2
        self.is_double_jumping = False

    
    def reset(self):
        self.init_position()
        self.stop_jumping()
    



def draw_rounded_rect(surface, rect, color, corner_radius):
    ''' Draw a rectangle with rounded corners.
    Would prefer this: 
        pygame.draw.rect(surface, color, rect, border_radius=corner_radius)
    but this option is not yet supported in my version of pygame so do it ourselves.

    We use anti-aliased circles to make the corners smoother
    '''
    if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
        raise ValueError(f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

    # need to use anti aliasing circle drawing routines to smooth the corners
    pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
    pygame.gfxdraw.aacircle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

    pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.top+corner_radius, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.left+corner_radius, rect.bottom-corner_radius-1, corner_radius, color)
    pygame.gfxdraw.filled_circle(surface, rect.right-corner_radius-1, rect.bottom-corner_radius-1, corner_radius, color)

    rect_tmp = pygame.Rect(rect)

    rect_tmp.width -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)

    rect_tmp.width = rect.width
    rect_tmp.height -= 2 * corner_radius
    rect_tmp.center = rect.center
    pygame.draw.rect(surface, color, rect_tmp)


def draw_bordered_rounded_rect(surface, rect, color, border_color, corner_radius, border_thickness):
    if corner_radius < 0:
        raise ValueError(f"border radius ({corner_radius}) must be >= 0")

    rect_tmp = pygame.Rect(rect)
    center = rect_tmp.center

    if border_thickness:
        if corner_radius <= 0:
            pygame.draw.rect(surface, border_color, rect_tmp)
        else:
            draw_rounded_rect(surface, rect_tmp, border_color, corner_radius)

        rect_tmp.inflate_ip(-2*border_thickness, -2*border_thickness)
        inner_radius = corner_radius - border_thickness + 1
    else:
        inner_radius = corner_radius

    if inner_radius <= 0:
        pygame.draw.rect(surface, color, rect_tmp)
    else:
        draw_rounded_rect(surface, rect_tmp, color, inner_radius)