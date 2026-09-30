import pygame
import random
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GRAVITY = 0.6
PLAYER_JUMP_POWER = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3
    PAUSED = 4

class Player(pygame.sprite.Sprite):
    """Player class representing the character in the game"""
    def __init__(self, x, y):
        super().__init__()
        self.width = 40
        self.height = 60
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Physics
        self.vel_y = 0
        self.vel_x = 0
        self.on_ground = False
        self.lane = 1  # 0: left, 1: middle, 2: right
        
    def update(self, obstacles, coins):
        """Update player position and handle collisions"""
        # Apply gravity
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        
        # Ground collision
        if self.rect.bottom >= SCREEN_HEIGHT - 100:
            self.rect.bottom = SCREEN_HEIGHT - 100
            self.vel_y = 0
            self.on_ground = True
        else:
            self.on_ground = False
        
        # Lane-based horizontal movement
        lane_positions = [100, 380, 660]
        self.rect.x = lane_positions[self.lane]
        
        # Obstacle collision
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                return False  # Player hit obstacle - game over
        
        # Coin collection
        for coin in coins:
            if self.rect.colliderect(coin.rect):
                coins.remove(coin)
                return 'coin'
        
        return True  # Player is safe
    
    def jump(self):
        """Make player jump"""
        if self.on_ground:
            self.vel_y = -PLAYER_JUMP_POWER
            self.on_ground = False
    
    def move_left(self):
        """Move player to left lane"""
        if self.lane > 0:
            self.lane -= 1
    
    def move_right(self):
        """Move player to right lane"""
        if self.lane < 2:
            self.lane += 1
    
    def draw(self, screen):
        """Draw player on screen"""
        screen.blit(self.image, self.rect)

class Obstacle(pygame.sprite.Sprite):
    """Obstacle class - represents enemies/blocks to avoid"""
    def __init__(self, x, y, lane):
        super().__init__()
        self.width = 60
        self.height = 60
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lane = lane
        self.speed = 5
    
    def update(self):
        """Update obstacle position"""
        self.rect.y += self.speed
    
    def is_off_screen(self):
        """Check if obstacle is off screen"""
        return self.rect.top > SCREEN_HEIGHT
    
    def draw(self, screen):
        """Draw obstacle on screen"""
        screen.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    """Coin class - represents collectible items"""
    def __init__(self, x, y, lane):
        super().__init__()
        self.width = 30
        self.height = 30
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GOLD)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lane = lane
        self.speed = 5
    
    def update(self):
        """Update coin position"""
        self.rect.y += self.speed
    
    def is_off_screen(self):
        """Check if coin is off screen"""
        return self.rect.top > SCREEN_HEIGHT
    
    def draw(self, screen):
        """Draw coin on screen"""
        screen.blit(self.image, self.rect)

class Game:
    """Main game class"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Temple Run")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
        
        self.reset_game()
    
    def reset_game(self):
        """Reset game variables"""
        self.state = GameState.MENU
        self.player = Player(380, SCREEN_HEIGHT - 200)
        self.obstacles = []
        self.coins = []
        self.score = 0
        self.high_score = 0
        self.spawn_timer = 0
        self.spawn_rate = 60  # Spawn obstacle every 60 frames
        self.game_over_message = ""
    
    def spawn_obstacles_and_coins(self):
        """Spawn obstacles and coins at random intervals"""
        self.spawn_timer += 1
        
        if self.spawn_timer >= self.spawn_rate:
            self.spawn_timer = 0
            
            # Spawn obstacle
            lane = random.randint(0, 2)
            lane_positions = [100, 380, 660]
            obstacle = Obstacle(lane_positions[lane], -60, lane)
            self.obstacles.append(obstacle)
            
            # Occasionally spawn coin
            if random.random() > 0.6:
                coin_lane = random.randint(0, 2)
                coin = Coin(lane_positions[coin_lane], -30, coin_lane)
                self.coins.append(coin)
            
            # Increase difficulty
            if self.spawn_rate > 30:
                self.spawn_rate -= 1
    
    def draw_menu(self):
        """Draw main menu"""
        self.screen.fill(BROWN)
        
        title = self.font_large.render("TEMPLE RUN", True, GOLD)
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(title, title_rect)
        
        start_text = self.font_medium.render("Press SPACE to Start", True, WHITE)
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
        self.screen.blit(start_text, start_rect)
        
        instructions = self.font_small.render("LEFT/RIGHT arrows to move", True, WHITE)
        inst_rect = instructions.get_rect(center=(SCREEN_WIDTH // 2, 400))
        self.screen.blit(instructions, inst_rect)
        
        jump_inst = self.font_small.render("UP arrow to jump", True, WHITE)
        jump_rect = jump_inst.get_rect(center=(SCREEN_WIDTH // 2, 450))
        self.screen.blit(jump_inst, jump_rect)
        
        if self.high_score > 0:
            high_score_text = self.font_small.render(f"High Score: {self.high_score}", True, GOLD)
            hs_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, 500))
            self.screen.blit(high_score_text, hs_rect)
    
    def draw_game(self):
        """Draw game screen"""
        # Background
        self.screen.fill(BROWN)
        
        # Draw ground
        pygame.draw.rect(self.screen, GRAY, (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100))
        
        # Draw lane markers
        pygame.draw.line(self.screen, WHITE, (250, 0), (250, SCREEN_HEIGHT), 2)
        pygame.draw.line(self.screen, WHITE, (530, 0), (530, SCREEN_HEIGHT), 2)
        
        # Draw game objects
        self.player.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
        for coin in self.coins:
            coin.draw(self.screen)
        
        # Draw score
        score_text = self.font_medium.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
    
    def draw_game_over(self):
        """Draw game over screen"""
        self.screen.fill(BLACK)
        
        game_over_text = self.font_large.render("GAME OVER", True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(game_over_text, game_over_rect)
        
        score_text = self.font_medium.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, 250))
        self.screen.blit(score_text, score_rect)
        
        high_score_text = self.font_medium.render(f"High Score: {self.high_score}", True, GOLD)
        hs_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, 350))
        self.screen.blit(high_score_text, hs_rect)
        
        restart_text = self.font_small.render("Press SPACE to Restart or ESC for Menu", True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, 450))
        self.screen.blit(restart_text, restart_rect)
    
    def draw_paused(self):
        """Draw paused screen"""
        pause_text = self.font_large.render("PAUSED", True, GOLD)
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(pause_text, pause_rect)
        
        resume_text = self.font_small.render("Press P to Resume", True, WHITE)
        resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        self.screen.blit(resume_text, resume_rect)
    
    def handle_events(self):
        """Handle player input and events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state != GameState.MENU:
                        self.state = GameState.MENU
                
                if self.state == GameState.MENU:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                        self.state = GameState.PLAYING
                
                elif self.state == GameState.PLAYING:
                    if event.key == pygame.K_UP:
                        self.player.jump()
                    elif event.key == pygame.K_LEFT:
                        self.player.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right()
                    elif event.key == pygame.K_p:
                        self.state = GameState.PAUSED
                
                elif self.state == GameState.GAME_OVER:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                        self.state = GameState.PLAYING
                
                elif self.state == GameState.PAUSED:
                    if event.key == pygame.K_p:
                        self.state = GameState.PLAYING
        
        return True
    
    def update(self):
        """Update game logic"""
        if self.state == GameState.PLAYING:
            # Update player
            result = self.player.update(self.obstacles, self.coins)
            
            if result is False:
                # Collision with obstacle
                self.state = GameState.GAME_OVER
                if self.score > self.high_score:
                    self.high_score = self.score
            elif result == 'coin':
                # Coin collected
                self.score += 10
            
            # Update obstacles
            for obstacle in self.obstacles[:]:
                obstacle.update()
                if obstacle.is_off_screen():
                    self.obstacles.remove(obstacle)
                    self.score += 5
            
            # Update coins
            for coin in self.coins[:]:
                coin.update()
                if coin.is_off_screen():
                    self.coins.remove(coin)
            
            # Spawn new obstacles and coins
            self.spawn_obstacles_and_coins()
    
    def draw(self):
        """Draw the current game state"""
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over()
        elif self.state == GameState.PAUSED:
            self.draw_game()
            self.draw_paused()
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
