# Ping Pong Game - Seed Specification

## Project Overview
A classic 2D Ping Pong (Pong) game with physics simulation, AI opponent, and multiplayer support. This specification will serve as the seed for growing a self-maintaining game organism through the Cybergenic Framework.

## Core Requirements

### 1. Game Mechanics
- **Ball Physics**
  - Ball starts at center, moves in random direction
  - Constant velocity with angle-based reflection
  - Speed increases slightly after each paddle hit (max speed cap)
  - Ball resets to center after scoring

- **Paddle Control**
  - Two paddles: left (Player 1) and right (Player 2/AI)
  - Vertical movement only (constrained to screen bounds)
  - Smooth acceleration and deceleration
  - Collision detection with ball

- **Scoring System**
  - Point awarded when ball passes opponent's paddle
  - First to 11 points wins (win by 2 if tied at 10-10)
  - Display current score for both players
  - Game over screen with winner announcement

### 2. Game Modes

#### Single Player (vs AI)
- AI difficulty levels: Easy, Medium, Hard
- AI reaction time varies by difficulty
- AI prediction of ball trajectory
- Slight randomness to make AI beatable

#### Two Player (Local)
- Player 1: W/S keys or Arrow Up/Down
- Player 2: Arrow Up/Down keys
- Both players on same keyboard

#### Two Player (Network) - Future Enhancement
- Host/Join game lobby
- Real-time synchronization
- Latency compensation

### 3. Visual Requirements

#### Graphics
- Minimalist retro aesthetic
- White paddles and ball on black background
- Dotted center line
- Score display at top center
- Optional: particle effects on ball hit

#### Screen Resolution
- Default: 800x600 pixels
- Scalable/resizable window
- Maintain aspect ratio
- Responsive UI elements

### 4. Audio Requirements
- Ball hit paddle sound (different pitch for each paddle)
- Ball hit wall sound
- Score point sound
- Game over sound
- Background music (optional, toggleable)
- Volume controls

### 5. User Interface

#### Main Menu
- Start Game (mode selection)
- Options (audio, controls, difficulty)
- High Scores
- Exit

#### In-Game HUD
- Score display
- FPS counter (debug mode)
- Pause menu (ESC key)
- "Press SPACE to start" before each point

#### Pause Menu
- Resume
- Restart
- Options
- Return to Main Menu

## Technical Architecture

### Protein Capabilities Needed

1. **PhysicsIntegrator** (Transform)
   - Calculate ball position and velocity
   - Handle collision detection
   - Apply physics rules (reflection, acceleration)

2. **InputHandler** (Communicate)
   - Capture keyboard input
   - Map keys to paddle movements
   - Handle menu navigation

3. **AIController** (Decide)
   - Calculate paddle target position
   - Predict ball trajectory
   - Apply difficulty-based behavior

4. **RenderEngine** (Communicate)
   - Draw game objects to screen
   - Handle screen updates and refresh
   - Manage visual effects

5. **AudioManager** (Communicate)
   - Load and play sound effects
   - Manage music playback
   - Control volume levels

6. **ScoreKeeper** (Manage State)
   - Track player scores
   - Determine win conditions
   - Persist high scores

7. **GameStateManager** (Coordinate)
   - Manage game states (menu, playing, paused, game over)
   - Coordinate between proteins
   - Handle game loop timing

8. **CollisionDetector** (Validate)
   - Check ball-paddle intersections
   - Check ball-wall collisions
   - Return collision data

9. **ConfigManager** (Manage State)
   - Load/save game settings
   - Manage difficulty settings
   - Handle player preferences

## Performance Requirements

### Frame Rate
- Target: 60 FPS
- Minimum acceptable: 30 FPS
- Fixed timestep for physics calculations

### Resource Constraints
- Memory: < 100 MB
- CPU: Single core, < 20% usage
- Startup time: < 2 seconds

### Homeostasis Triggers
- If FPS drops below 45, reduce particle effects
- If input lag detected, increase input polling rate
- If rendering slow, simplify graphics

## Signal Requirements

### Game Signals to Emit
- `BALL_HIT_PADDLE` - Ball collides with paddle
- `BALL_HIT_WALL` - Ball collides with top/bottom wall
- `SCORE_POINT` - Player scores a point
- `GAME_START` - Game begins
- `GAME_PAUSE` - Game paused
- `GAME_RESUME` - Game resumed
- `GAME_OVER` - Game ends with winner
- `AI_DIFFICULTY_CHANGE` - AI difficulty adjusted
- `SETTINGS_CHANGE` - User changes settings
- `FRAME_RATE_DROP` - Performance degradation detected

### Signal Handlers Needed
- Audio system listens for collision/score signals
- Particle system listens for ball hit signals
- UI updates on score/game state changes
- Homeostasis responds to performance signals

## Physics Specifications

### Ball Properties
- Radius: 8 pixels
- Initial speed: 300 pixels/second
- Speed increase per hit: 5%
- Maximum speed: 600 pixels/second
- Reflection: angle of incidence = angle of reflection
- Spin effect: paddle movement influences ball angle

### Paddle Properties
- Width: 15 pixels
- Height: 80 pixels
- Max speed: 400 pixels/second
- Acceleration: 1500 pixels/second²
- Deceleration: 2000 pixels/second²

### Collision Rules
- Ball-paddle: Reflect ball angle based on hit position
  - Center hit: minimal angle change
  - Edge hit: sharper angle (max ±60°)
- Ball-wall: Perfect horizontal reflection
- Ball-goal: Stop ball, award point, reset

## Testing Requirements

### Unit Tests Needed
- Physics calculations (ball trajectory, collision)
- AI decision making at various difficulties
- Score tracking and win conditions
- Input handling and key mapping

### Integration Tests
- Complete game loop execution
- State transitions (menu → game → game over)
- Audio-visual synchronization
- Save/load functionality

### Apoptosis Conditions
- Physics protein fails consistency checks → regenerate
- AI protein makes invalid moves → regenerate
- Render protein causes crashes → regenerate
- Audio protein has excessive errors → regenerate

## Implementation Priority

### Phase 1: Core Mechanics (Generation 1)
1. Basic ball physics
2. Paddle movement
3. Collision detection
4. Simple scoring
5. Basic rendering

### Phase 2: Game Flow (Generation 2)
1. Menu system
2. Game state management
3. Win conditions
4. Pause functionality

### Phase 3: AI & Polish (Generation 3)
1. AI opponent implementation
2. Audio system
3. Visual effects
4. Settings/options

### Phase 4: Advanced Features (Generation 4+)
1. High score persistence
2. Multiple difficulty levels
3. Network multiplayer (future)
4. Achievements/stats

## Success Metrics

### Functional Success
- Game runs at target FPS
- All game modes functional
- No game-breaking bugs
- Collision detection accurate

### Self-Maintenance Success
- Proteins self-heal from errors
- Homeostasis maintains performance
- Orphan signals discovered and handled
- Metabolic costs within budget

### User Experience Success
- Responsive controls (< 16ms input lag)
- Smooth gameplay
- Intuitive UI
- Engaging AI opponent

## Platform & Technology

### Primary Target
- Platform: Windows/Linux/Mac
- Language: Python
- Graphics: Pygame or similar 2D library
- Audio: Pygame mixer

### Dependencies
- Python 3.8+
- Pygame 2.0+
- NumPy (for physics calculations)

## Configuration Files Needed

### game_config.json
```json
{
  "screen_width": 800,
  "screen_height": 600,
  "target_fps": 60,
  "ball_speed": 300,
  "paddle_speed": 400,
  "ai_difficulty": "medium",
  "audio_enabled": true,
  "music_volume": 0.7,
  "sfx_volume": 0.8
}
```

## Notes for Framework Evolution

This specification should guide the Cybergenic Framework to:
1. Generate appropriate proteins for each capability
2. Establish signal pathways for game events
3. Implement self-monitoring for performance
4. Create tests that verify game behavior
5. Allow evolutionary improvements based on runtime signals

The game should "grow" organically, with each generation adding sophistication while maintaining core functionality through self-healing mechanisms.

---

**Seed Version:** 1.0
**Created:** October 2025
**Framework:** Cybergenic v6.0.0
**Status:** Ready for Conception
