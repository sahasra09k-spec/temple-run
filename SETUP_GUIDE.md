# Temple Run - Complete Setup & Development Guide 🎮

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Quick Start (5 minutes)](#quick-start-5-minutes)
3. [Detailed Setup](#detailed-setup)
4. [Understanding the Code](#understanding-the-code)
5. [Running the Game](#running-the-game)
6. [Customization Guide](#customization-guide)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### What You Need:
- **Python 3.7 or higher** - Download from [python.org](https://www.python.org/downloads/)
- **pip** - Usually comes with Python (verify with `pip --version`)
- **A text editor or IDE** - VS Code, PyCharm, or Sublime Text
- **Git** (optional but recommended)

### Check Your Python Installation:
```bash
python --version
pip --version
```

Both commands should show version numbers. If not, reinstall Python.

---

## Quick Start (5 minutes)

### Option 1: Using Git
```bash
# Clone the repository
git clone https://github.com/sahasra09k-spec/temple-run.git
cd temple-run

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

### Option 2: Manual Setup
```bash
# Create project directory
mkdir temple-run
cd temple-run

# Install Pygame
pip install pygame==2.5.2

# Create main.py and config.py files (copy from repository)

# Run the game
python main.py
```

---

## Detailed Setup

### Step 1: Install Python
**Windows:**
- Download from python.org
- Run installer
- ✅ Check "Add Python to PATH"
- Click Install

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### Step 2: Create Project Directory
```bash
mkdir temple-run
cd temple-run
```

### Step 3: Set Up Virtual Environment (Recommended)
A virtual environment keeps your project dependencies isolated.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You'll see `(venv)` in your terminal when active.

### Step 4: Install Pygame
```bash
pip install pygame==2.5.2
pip install numpy==1.24.3
```

Verify installation:
```bash
python -c "import pygame; print(pygame.version.ver)"
```

### Step 5: Create Project Files
Create these files in your `temple-run` directory:

**File 1: main.py** - Copy the complete code from the repository
**File 2: config.py** - Copy the complete code from the repository
**File 3: requirements.txt** - Already provided

### Step 6: Run the Game
```bash
python main.py
```

A 800x600 window should appear with the game menu.

---

## Understanding the Code

### Project Structure
```
temple-run/
├── main.py           # Main game file (500+ lines)
├── config.py         # Configuration constants
├── requirements.txt  # Dependencies
├── SETUP_GUIDE.md   # This file
└── README.md         # Game documentation
```

### Core Classes

#### 1. **Player Class**
```python
class Player(pygame.sprite.Sprite):
    """Controls player character"""
    - Position tracking (x, y)
    - Velocity (vel_x, vel_y)
    - Lane system (0, 1, 2)
    - Jump mechanics
    - Collision detection
```

**Key Methods:**
- `update()` - Updates position, applies gravity
- `jump()` - Makes player jump
- `move_left()` / `move_right()` - Changes lanes

#### 2. **Obstacle Class**
```python
class Obstacle(pygame.sprite.Sprite):
    """Moving obstacles to avoid"""
    - Position and size
    - Downward velocity
    - Collision detection
```

**Key Methods:**
- `update()` - Moves obstacle downward
- `is_off_screen()` - Removes when off-screen

#### 3. **Coin Class**
```python
class Coin(pygame.sprite.Sprite):
    """Collectible items for points"""
    - Similar to obstacles
    - Awards points when collected
```

#### 4. **Game Class**
```python
class Game:
    """Main game controller"""
    - Screen management
    - Game state handling
    - Input processing
    - Rendering
    - Game loop
```

**Key Methods:**
- `run()` - Main game loop
- `update()` - Game logic each frame
- `draw()` - Render game graphics
- `handle_events()` - Process keyboard input
- `spawn_obstacles_and_coins()` - Create game objects

### Game Flow

```
START
  ↓
Initialize Pygame → Create Game Instance
  ↓
Display Menu
  ↓
Wait for User Input (SPACE to start)
  ↓
GAME LOOP (runs at 60 FPS):
  ├─ Process Input (arrow keys, P for pause)
  ├─ Update Game State
  │  ├─ Move player
  │  ├─ Move obstacles/coins
  │  ├─ Check collisions
  │  └─ Update score
  ├─ Render Graphics
  └─ Repeat...
  ↓
Game Over → Show Score
  ↓
ESC returns to menu or SPACE to restart
```

---

## Running the Game

### Launch the Game
```bash
python main.py
```

### Screen Appears?
✅ **Success!** You should see:
- Brown background
- Green player character
- "TEMPLE RUN" title
- Instructions

### Troubleshooting Launch Issues

**Error: "No module named 'pygame'"**
```bash
pip install pygame --upgrade
```

**Error: "pygame.error: No available video device"**
- Close and reopen terminal
- Restart your computer
- Check GPU drivers

**Game window won't display**
- Try running from terminal to see errors
- Check monitor is connected
- Update graphics drivers

---

## Customization Guide

### 1. Change Game Speed
**File: config.py**
```python
# Increase obstacle speed
OBSTACLE_SPEED = 7  # Default: 5

# Make gravity stronger (jump feels shorter)
GRAVITY = 0.8  # Default: 0.6

# Make jump higher
PLAYER_JUMP_POWER = 20  # Default: 15
```

### 2. Change Colors
**File: config.py**
```python
# Player color (RGB format)
PLAYER_COLOR = (255, 0, 255)  # Change to magenta

# Obstacle color
OBSTACLE_COLOR = (255, 165, 0)  # Change to orange

# Coin color
COIN_COLOR = (128, 0, 255)  # Change to purple
```

### 3. Adjust Difficulty
**File: config.py**
```python
# How long between obstacles spawn
OBSTACLE_SPAWN_RATE = 40  # Default: 60 (lower = harder)

# Minimum spawn rate (hardest)
OBSTACLE_MIN_SPAWN_RATE = 20  # Default: 30

# Coin spawn chance
COIN_SPAWN_PROBABILITY = 0.2  # Default: 0.4 (lower = fewer coins)
```

### 4. Change Scoring
**File: config.py**
```python
POINTS_PER_OBSTACLE = 10  # Default: 5
POINTS_PER_COIN = 25      # Default: 10
```

### 5. Change Screen Size
**File: config.py**
```python
SCREEN_WIDTH = 1024   # Default: 800
SCREEN_HEIGHT = 768   # Default: 600

# Update lane positions proportionally
LANE_POSITIONS = [150, 500, 850]
```

### 6. Add Custom Player Size
**File: config.py**
```python
PLAYER_WIDTH = 50    # Default: 40
PLAYER_HEIGHT = 70   # Default: 60
```

### 7. Change Ground Height
**File: config.py**
```python
GROUND_HEIGHT = 150  # Default: 100 (increase for more playing space)
```

### Example: Making the Game Harder
```python
# config.py changes for hard mode:
OBSTACLE_SPAWN_RATE = 30
OBSTACLE_MIN_SPAWN_RATE = 15
COIN_SPAWN_PROBABILITY = 0.2
GRAVITY = 0.8
```

---

## Troubleshooting

### Issue: Game Runs Slow
**Solution 1:** Close background apps
```bash
# Check system resources
# Windows: Task Manager
# Mac: Activity Monitor
# Linux: htop
```

**Solution 2:** Lower FPS temporarily
```python
# In config.py
FPS = 30  # Default: 60
```

**Solution 3:** Reduce visual complexity
```python
# In config.py
SHOW_LANE_MARKERS = False
DEBUG_MODE = False
```

### Issue: Game Window is Freezing
**Cause:** Graphics driver issue
**Solution:**
- Update GPU drivers
- Reinstall Pygame: `pip install --upgrade --force-reinstall pygame`
- Try different Python version

### Issue: Keyboard Input Not Responding
**Cause:** Pygame event queue not processing
**Solution:**
- Click on game window to focus it
- Try running as administrator (Windows)
- Restart the application

### Issue: Score Not Increasing
**Cause:** Check collision detection
**Solution:**
1. Verify obstacles are spawning (should appear on screen)
2. Check that you're passing them completely
3. See if debug mode shows collision boxes

### Issue: Game Crashes on Startup
**Solution - Step 1:** Check Python version
```bash
python --version  # Should be 3.7 or higher
```

**Solution - Step 2:** Reinstall dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

**Solution - Step 3:** Check for syntax errors
```bash
python -m py_compile main.py
```

---

## Advanced Customization

### Add Custom Font
```python
# In main.py, modify font initialization:
self.font_large = pygame.font.Font('path/to/font.ttf', 72)
```

### Enable Debug Mode
```python
# In config.py
DEBUG_MODE = True
SHOW_COLLISION_BOXES = True
SHOW_FPS = True
```

### Create Different Difficulty Levels
```python
# In config.py - add difficulty presets
DIFFICULTY_PRESET = 'medium'  # Options: 'easy', 'medium', 'hard'

# Then in main.py:
if config.DIFFICULTY_PRESET == 'hard':
    config.OBSTACLE_SPAWN_RATE = 20
    config.GRAVITY = 1.0
```

---

## Performance Optimization Tips

### 1. Use Sprite Groups Efficiently
The game already does this with pygame.sprite.Sprite

### 2. Limit Spawn Rate
Fewer simultaneous objects = better performance
```python
# Limit max obstacles on screen
if len(self.obstacles) > 10:
    return  # Don't spawn more
```

### 3. Use Pygame Clock
Already implemented - `self.clock.tick(FPS)`

### 4. Batch Rendering
Group similar objects for efficient drawing

---

## Next Steps for Enhancement

1. **Add Sound Effects**
   - Jump sound
   - Coin collection sound
   - Game over sound

2. **Add Graphics/Sprites**
   - Character sprites
   - Obstacle sprites
   - Coin animations

3. **Add Levels**
   - Different themes per level
   - Progressive difficulty curve

4. **Add Power-ups**
   - Shield (temp immunity)
   - Speed boost
   - Score multiplier

5. **Save High Scores**
   - Use file I/O to save/load scores
   - Create leaderboard

6. **Add Animations**
   - Sprite movement animations
   - Particle effects
   - Screen transitions

---

## Getting Help

### Common Resources
- **Pygame Docs:** https://www.pygame.org/docs/
- **Python Docs:** https://docs.python.org/3/
- **Stack Overflow:** Tag questions with `pygame` and `python`

### Debug Techniques
1. Add `print()` statements to track variables
2. Use `SHOW_COLLISION_BOXES = True` to visualize hitboxes
3. Run in terminal to see error messages
4. Use a debugger like `pdb`

---

## Quick Reference

### Start Game
```bash
python main.py
```

### Change Settings
Edit `config.py` before running

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### Deactivate Virtual Environment
```bash
deactivate
```

---

## Success Checklist ✅

- [ ] Python 3.7+ installed
- [ ] Pygame installed (`pip install pygame`)
- [ ] main.py downloaded/created
- [ ] config.py downloaded/created
- [ ] Game runs without errors (`python main.py`)
- [ ] Menu displays correctly
- [ ] Can start game with SPACE
- [ ] Can move with arrow keys
- [ ] Game over occurs when hitting obstacle
- [ ] Score increases properly

---

**Congratulations! You now have a fully functional Temple Run game!** 🎉

For questions or issues, refer to the README.md or check the Pygame documentation.

Happy Gaming! 🏃‍♂️💨
