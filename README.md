# Temple Run Game 🏃‍♂️

A fun and exciting endless runner game built with Python and Pygame. Navigate through lanes, avoid obstacles, collect coins, and try to achieve the highest score!

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Controls](#game-controls)
- [Game Mechanics](#game-mechanics)
- [Project Structure](#project-structure)
- [Step-by-Step Development Guide](#step-by-step-development-guide)

## ✨ Features

- **Three-Lane Movement System**: Navigate between left, middle, and right lanes
- **Dynamic Obstacles**: Avoid randomly spawned red obstacles
- **Collectible Coins**: Gather gold coins for bonus points
- **Scoring System**: 
  - +5 points for each obstacle passed
  - +10 points for each coin collected
- **Progressive Difficulty**: Game speeds up as you progress
- **High Score Tracking**: Your best score is saved during session
- **Game States**: Menu, Playing, Paused, and Game Over screens
- **Smooth Physics**: Gravity and jumping mechanics for realistic movement

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/sahasra09k-spec/temple-run.git
cd temple-run
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pygame==2.5.2
pip install numpy==1.24.3
```

### Step 3: Run the Game
```bash
python main.py
```

## 🎮 How to Play

1. **Start Menu**: Press SPACE to start the game
2. **Stay Alive**: Avoid red obstacles by moving between lanes
3. **Collect Coins**: Grab gold coins for bonus points
4. **Beat Your Score**: The game gets progressively harder!
5. **Game Over**: When you hit an obstacle, your game ends
6. **Restart**: Press SPACE to play again or ESC for menu

## 🕹️ Game Controls

| Key | Action |
|-----|--------|
| **LEFT ARROW** | Move to left lane |
| **RIGHT ARROW** | Move to right lane |
| **UP ARROW** | Jump |
| **P** | Pause/Resume game |
| **ESC** | Return to main menu |
| **SPACE** | Start game / Restart after game over |

## 🔧 Game Mechanics

### Player
- **Width**: 40 pixels | **Height**: 60 pixels (Green color)
- **Jump Power**: 15 units
- **Gravity**: 0.6 units per frame
- **Lanes**: 3 lanes at positions (100, 380, 660)

### Obstacles
- **Width**: 60 pixels | **Height**: 60 pixels (Red color)
- **Speed**: 5 pixels per frame (increases with difficulty)
- **Spawn Rate**: Starts at every 60 frames, decreases as game progresses
- **Points**: +5 for each obstacle passed

### Coins
- **Width**: 30 pixels | **Height**: 30 pixels (Gold color)
- **Speed**: 5 pixels per frame
- **Spawn Chance**: 40% when obstacle spawns
- **Points**: +10 per coin collected

### Difficulty Progression
- Spawn rate decreases by 1 frame each spawn cycle (minimum 30 frames)
- Game becomes faster and more challenging as you progress
- No level caps - infinite escalation!

## 📁 Project Structure

```
temple-run/
│
├── main.py                 # Main game file with all game logic
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 💻 Step-by-Step Development Guide

### Step 1: Project Setup
Create a new directory and initialize a Git repository:
```bash
mkdir temple-run
cd temple-run
git init
```

### Step 2: Install Pygame
Pygame is the library we use for graphics and input handling:
```bash
pip install pygame==2.5.2
```

### Step 3: Create Requirements File
```bash
echo "pygame==2.5.2" > requirements.txt
echo "numpy==1.24.3" >> requirements.txt
```

### Step 4: Create Game Classes

#### 4.1 Initialize Pygame
```python
import pygame
pygame.init()
```

#### 4.2 Define Game Constants
- Screen dimensions: 800x600
- FPS: 60 frames per second
- Color constants for visuals
- Physics constants (gravity, jump power)

#### 4.3 Create Player Class
Features:
- Position and velocity tracking
- Lane-based movement (left, middle, right)
- Jump mechanics with gravity
- Collision detection

#### 4.4 Create Obstacle Class
Features:
- Downward movement
- Collision boundary
- Off-screen detection

#### 4.5 Create Coin Class
Features:
- Similar to obstacles but collectible
- Off-screen detection
- Bonus point system

### Step 5: Create Game Class
Main game controller with:
- Screen management
- Game state handling (Menu, Playing, Paused, Game Over)
- Input processing
- Game loop
- Rendering system
- Spawn mechanism

### Step 6: Implement Game States

#### Menu State
- Display game title
- Show instructions
- Display high score
- Wait for SPACE to start

#### Playing State
- Update player position
- Spawn and update obstacles/coins
- Check collisions
- Update score
- Track high score

#### Paused State
- Freeze game
- Show pause message
- Allow resume with 'P'

#### Game Over State
- Display final score
- Show high score
- Allow restart or return to menu

### Step 7: Add Game Loop
```python
while running:
    handle_events()
    update()
    draw()
    tick(FPS)
```

### Step 8: Run and Test
```bash
python main.py
```

## 🎯 Game Flow Diagram

```
START
  ↓
MENU (Wait for SPACE)
  ↓
PLAYING
  ├─→ Player moves/jumps
  ├─→ Obstacles spawn
  ├─→ Coins spawn
  ├─→ Check collisions
  │
  ├─→ Hit Obstacle? → GAME OVER
  │
  ├─→ Collected Coin? → Score +10
  │
  └─→ Passed Obstacle? → Score +5
  
GAME OVER
  ├─→ Press SPACE → PLAYING (restart)
  └─→ Press ESC → MENU
```

## 🔍 Code Highlights

### Player Update with Gravity
```python
def update(self, obstacles, coins):
    self.vel_y += GRAVITY
    self.rect.y += self.vel_y
    # ... collision checks
```

### Lane-Based Movement
```python
lane_positions = [100, 380, 660]
self.rect.x = lane_positions[self.lane]
```

### Dynamic Difficulty
```python
if self.spawn_rate > 30:
    self.spawn_rate -= 1
```

## 🐛 Troubleshooting

### Game Won't Start
- Ensure Python 3.7+ is installed
- Verify pygame is installed: `pip list | grep pygame`
- Try: `pip install --upgrade pygame`

### Game Runs But Window is Black
- Check your screen resolution
- Ensure display drivers are updated
- Try running in windowed mode

### High CPU Usage
- Close background applications
- Check if FPS is correctly set to 60
- Ensure GPU drivers are updated

## 📊 Scoring Guide

| Action | Points |
|--------|--------|
| Pass an obstacle | +5 |
| Collect a coin | +10 |
| Hit obstacle | Game Over |

## 🎨 Customization Ideas

1. **Change Colors**: Modify RGB tuples in constants
2. **Adjust Difficulty**: Change `GRAVITY` or `PLAYER_JUMP_POWER`
3. **Add Sound**: Integrate pygame.mixer for SFX
4. **Add Animations**: Use sprite sheets
5. **Add Power-ups**: Create temporary abilities
6. **Add Levels**: Implement level progression
7. **Add Enemies**: Create moving obstacles
8. **Add Settings**: Add volume, difficulty selection

## 📚 Learning Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python OOP Concepts](https://docs.python.org/3/tutorial/classes.html)
- [Game Development Basics](https://www.gamedev.net/)

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as an educational game development project.

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🎮 Have Fun Playing!

Enjoy the game and try to beat your high score! 🏆
