"""
Game Configuration File
Modify these values to customize your Temple Run game
"""

# ============================================
# SCREEN SETTINGS
# ============================================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
GAME_TITLE = "Temple Run"

# ============================================
# PLAYER SETTINGS
# ============================================
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_JUMP_POWER = 15
PLAYER_COLOR = (0, 255, 0)  # GREEN
PLAYER_START_X = 380
PLAYER_START_Y = 450

# ============================================
# PHYSICS SETTINGS
# ============================================
GRAVITY = 0.6
MAX_FALL_SPEED = 20

# ============================================
# OBSTACLE SETTINGS
# ============================================
OBSTACLE_WIDTH = 60
OBSTACLE_HEIGHT = 60
OBSTACLE_COLOR = (255, 0, 0)  # RED
OBSTACLE_SPEED = 5
OBSTACLE_SPAWN_RATE = 60  # Frames between spawns
OBSTACLE_MIN_SPAWN_RATE = 30  # Minimum spawn rate (difficulty cap)
OBSTACLE_POINTS = 5

# ============================================
# COIN SETTINGS
# ============================================
COIN_WIDTH = 30
COIN_HEIGHT = 30
COIN_COLOR = (255, 215, 0)  # GOLD
COIN_SPEED = 5
COIN_SPAWN_PROBABILITY = 0.4  # 40% chance when obstacle spawns
COIN_POINTS = 10

# ============================================
# LANE SETTINGS
# ============================================
NUM_LANES = 3
LANE_POSITIONS = [100, 380, 660]  # X coordinates for each lane
GROUND_HEIGHT = 100

# ============================================
# COLOR PALETTE
# ============================================
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GOLD = (255, 215, 0)
COLOR_BROWN = (139, 69, 19)
COLOR_GRAY = (128, 128, 128)
COLOR_DARK_GRAY = (64, 64, 64)

# ============================================
# DIFFICULTY SETTINGS
# ============================================
INITIAL_DIFFICULTY = 1.0  # Multiplier for obstacle speed
DIFFICULTY_INCREASE_RATE = 0.01  # Increase per obstacle passed
MAX_DIFFICULTY = 2.0  # Cap on difficulty multiplier

# ============================================
# AUDIO SETTINGS (Future use)
# ============================================
ENABLE_SOUND = False
MASTER_VOLUME = 0.8
MUSIC_VOLUME = 0.6
SFX_VOLUME = 0.8

# ============================================
# UI SETTINGS
# ============================================
FONT_SIZE_LARGE = 72
FONT_SIZE_MEDIUM = 48
FONT_SIZE_SMALL = 36
FONT_FAMILY = None  # None uses default font

# ============================================
# GAME SPEED SETTINGS
# ============================================
DIFFICULTY_INCREASE_INTERVAL = 10  # Obstacles passed before speed increase
SPEED_MULTIPLIER_INCREMENT = 0.05  # How much speed increases

# ============================================
# SCORING SETTINGS
# ============================================
POINTS_PER_OBSTACLE = 5
POINTS_PER_COIN = 10
BONUS_MULTIPLIER = 1.0  # Multiply points based on difficulty

# ============================================
# DEBUG SETTINGS
# ============================================
DEBUG_MODE = False
SHOW_COLLISION_BOXES = False
SHOW_FPS = False
SHOW_LANE_MARKERS = True
