# Cybergenic Framework Tutorial
## Complete Beginner's Guide to Growing Self-Maintaining Software

Welcome! This tutorial will guide you through setting up and using the Cybergenic Framework - a revolutionary way to grow software like biological organisms instead of writing code manually.

---

## Table of Contents
1. [What You'll Need (Prerequisites)](#prerequisites)
2. [Understanding the Basics](#understanding-the-basics)
3. [Installation & Setup](#installation--setup)
4. [Your First Organism (PingPong Game Example)](#your-first-organism)
5. [Running Conception](#running-conception)
6. [Evolution and Growth](#evolution-and-growth)
7. [Monitoring Your Organism](#monitoring-your-organism)
8. [Understanding Commands](#understanding-commands)
9. [Troubleshooting](#troubleshooting)
10. [Next Steps](#next-steps)

---

## Prerequisites

Before you start, make sure you have these tools installed on your computer:

### Required Software

#### 1. **Python 3.8 or Higher**
Python is the programming language that runs the Cybergenic Framework.

**Check if you have Python:**
```bash
python --version
```
or
```bash
python3 --version
```

**If you don't have Python:**
- **Windows:** Download from [python.org](https://www.python.org/downloads/)
- **Mac:** Use Homebrew: `brew install python3`
- **Linux:** Use your package manager: `sudo apt-get install python3`

#### 2. **Git (Version Control)**
Git tracks changes to your organism as it evolves.

**Check if you have Git:**
```bash
git --version
```

**If you don't have Git:**
- Download from [git-scm.com](https://git-scm.com/downloads)
- Follow the installation wizard with default settings

#### 3. **Python Package: psutil**
This package helps monitor system resources (CPU, memory).

**Install psutil:**
```bash
pip install psutil
```
or
```bash
pip3 install psutil
```

### Optional but Recommended

#### 4. **Node.js & npm (for MCP Servers)**
MCP servers give AI agents enhanced capabilities like persistent memory.

**Check if you have Node.js:**
```bash
node --version
npm --version
```

**If you don't have Node.js:**
- Download from [nodejs.org](https://nodejs.org/) (LTS version recommended)
- npm comes bundled with Node.js

#### 5. **Claude Code CLI**
If you're using Claude Code, you already have this!

---

## Understanding the Basics

### What is Cybergenic?

Instead of writing code line by line, you:
1. Describe what you want to build (the "seed")
2. Run the framework
3. Watch your software "grow" through generations
4. The organism self-heals, self-optimizes, and adapts

### Key Concepts (Simplified)

**DNA.md** - The "genetic code" containing architectural rules for your project

**Proteins** - Complete classes (not functions) that do specific jobs

**Signals** - Events that proteins broadcast to communicate

**Agents** - AI assistants that build your organism:
- **Architect** (Smart/Sonnet) - Creates the DNA
- **Coordinator** (Smart/Sonnet) - Plans what to build
- **Synthesizers** (Fast/Haiku) - Build the actual code (8 specialized types)
- **Chaperone** (Fast/Haiku) - Checks code quality

**Self-Maintenance Systems** - Automatic systems that keep your organism healthy:
- **Apoptosis** - Removes broken code automatically
- **Homeostasis** - Balances resource usage
- **Immune System** - Blocks dangerous code
- **Metabolic Tracker** - Monitors costs

For more details, see [README.md](README.md) and [WORKFLOW.md](WORKFLOW.md).

---

## Installation & Setup

### Step 1: Get the Framework Files

Make sure you have these files in your project directory:

**Core Framework Files:**
```
your-project/
├── setup_cybergenic.py          # Setup script (you have this!)
├── immune_system.py              # Immune system
├── homeostasis.py                # Homeostasis controller
├── metabolic_tracker.py          # Cost tracker
├── apoptosis.py                  # Cell death system
├── signal_bus.py                 # Signal infrastructure
├── cybergen_orchestrator.py     # Main orchestrator
├── README.md                     # Overview document
├── WORKFLOW.md                   # How it works
└── COMMANDS.md                   # Command reference
```

### Step 2: Run the Setup Script

Open your terminal in the project directory and run:

```bash
python setup_cybergenic.py
```

or on some systems:

```bash
python3 setup_cybergenic.py
```

**What happens:**
The script will check your Python version and required packages, then create:

1. **Directory structure** for your organism
2. **11 AI agent definitions** (Architect, Coordinator, 8 Synthesizers, Chaperone)
3. **Tracking files** for signals, proteins, and self-maintenance
4. **MCP configuration** for enhanced AI capabilities
5. **Git repository** for version control
6. **Template seed file** for your project requirements

**Expected output:**
```
╔════════════════════════════════════════════════════════════════╗
║         CYBERGENIC FRAMEWORK SETUP                             ║
║  "Don't write code. Grow self-maintaining organisms"          ║
╚════════════════════════════════════════════════════════════════╝

[SETUP] Checking dependencies...
   ✓ Python 3.11
   ✓ psutil installed

[SETUP] Creating directory structure...
   ✓ Created .cybergenic/dna/
   ✓ Created .cybergenic/generations/
   ✓ Created .claude/agents/
   ✓ Created seed/documents/
   ... (more directories)

[SETUP] Creating tracking files...
   ✓ Created generation_counter.txt
   ✓ Created signal_log.json
   ... (more files)

[SETUP] Creating agent definitions...
   ✓ Created architect.md
   ✓ Created coordinator.md
   ✓ Created synthesizer_transform.md
   ✓ Created synthesizer_validate.md
   ... (8 synthesizers total)
   ✓ Created chaperone.md

   Total agents created: 11
   - 1 Architect (Sonnet 4.5)
   - 1 Coordinator (Sonnet 4.5)
   - 8 Specialized Synthesizers (Haiku 4)
   - 1 Chaperone (Haiku 4)

[SUCCESS] Cybergenic Framework initialized!
```

### Step 3: Verify the Directory Structure

Your project should now look like this:

```
your-project/
├── .cybergenic/                  # Framework data (created ✓)
│   ├── dna/                      # Will hold DNA.md
│   ├── generations/              # Generation history
│   ├── signals/                  # Signal logs
│   ├── proteins/                 # Synthesized proteins
│   ├── immune/                   # Immune system data
│   ├── metabolism/               # Cost tracking
│   ├── generation_counter.txt    # Starts at 0
│   ├── run_counter.txt           # Starts at 0
│   ├── signal_log.json           # Empty []
│   ├── signal_discovery.json     # Orphan tracker
│   ├── protein_registry.json     # Empty {}
│   ├── immune_memory.json        # Immune memory
│   ├── metabolic_costs.json      # Cost data
│   ├── homeostasis_state.json    # Balance settings
│   └── apoptosis_log.json        # Cell death log
│
├── .claude/                      # AI agent configs (created ✓)
│   ├── agents/                   # 11 agent definition files
│   ├── commands/                 # Command definitions
│   └── mcp.json                  # MCP configuration
│
├── seed/                         # Your project seed (created ✓)
│   ├── documents/                # Additional docs
│   ├── images/                   # Mockups/images
│   ├── requirements/             # Requirements files
│   └── requirements.md           # Main requirements (EDIT THIS!)
│
├── framework/                    # Optional patterns (created ✓)
├── output/                       # Generated code (created ✓)
│
├── setup_cybergenic.py           # Setup script
├── immune_system.py              # Self-maintenance files
├── homeostasis.py
├── metabolic_tracker.py
├── apoptosis.py
├── signal_bus.py
├── cybergen_orchestrator.py
│
└── .gitignore                    # Git exclusions (created ✓)
```

---

## Your First Organism

Let's create a simple PingPong game to learn how Cybergenic works!

### Step 4: Write Your Seed (Project Requirements)

Open the file `seed/requirements.md` in your text editor and replace its contents with:

```markdown
# PingPong Game Requirements

## Project Description
Build a simple 2D PingPong game where two paddles hit a ball back and forth.
The game should run in a terminal/console with ASCII graphics.

## Core Features
- **Two Paddles**: Left and right paddles that can move up and down
- **Ball**: A ball that bounces between paddles and walls
- **Physics**: Simple 2D physics for ball movement and collision
- **Scoring**: Track score when a player misses the ball
- **Controls**: Keyboard controls (W/S for left paddle, Up/Down arrows for right paddle)
- **Game Loop**: Continuous game loop with consistent frame rate

## Technical Requirements
- Programming Language: Python 3.8+
- Display: Terminal/console using ASCII characters
- Input: Keyboard input (non-blocking)
- Physics: Simple 2D vector physics
- Frame Rate: 30 FPS target

## Game Rules
1. Ball starts in center, moves in random direction
2. Paddles can move up/down to intercept ball
3. Ball bounces off top/bottom walls
4. Ball bounces off paddles with angle based on hit position
5. When ball goes past a paddle, opponent scores a point
6. Game continues until one player reaches 10 points

## Architecture Preferences
- Use object-oriented design (classes for Ball, Paddle, Game)
- Separate rendering from game logic
- Use signal-based communication between components
- Include collision detection system
- Self-monitoring for performance (frame rate, input lag)

## Success Criteria
- Game runs smoothly at 30 FPS
- Controls are responsive
- Physics feel realistic
- Score tracking works correctly
- Game can be restarted after completion
```

**Important:** The more detailed your requirements, the better the organism understands what to build!

### Optional: Add More Seed Materials

You can add additional materials to help the Architect understand your vision:

```bash
seed/
├── requirements.md              # Your main requirements (required)
├── documents/
│   └── game_design.md           # Detailed game design (optional)
├── images/
│   └── game_mockup.png          # Visual mockup (optional)
```

---

## Running Conception

Now let's "conceive" the organism - this is Generation 0 where the DNA is created.

### Step 5: Run Conception

In your terminal, if using Claude Code, type:

```bash
/cybergenrun
```

Or if running directly with Python:

```bash
python cybergen_orchestrator.py run
```

**What happens during Conception:**

1. **Architect Agent Wakes Up**
   - Reads your seed materials (`seed/requirements.md`)
   - Analyzes what you want to build
   - Thinks about architecture

2. **DNA Creation**
   - Creates `DNA.md` with Sacred Architectural Rules
   - Defines signal emission standards
   - Configures self-maintenance systems:
     - Apoptosis thresholds (when code should "die")
     - Homeostasis targets (CPU, memory limits)
     - Metabolic cost limits (API usage budgets)
     - Immune threat patterns (security rules)
   - Plans the technology stack
   - Designs module boundaries

3. **Saves DNA**
   - Writes DNA to `.cybergenic/dna/DNA.md`
   - Creates git checkpoint: "Generation 0: Conception complete"

**Expected output:**
```
[CYBERGEN] Starting Cybergenic Framework...
[GENERATION] Current generation: 0
[RUN] Run counter: 1

[FIRST RUN] Initiating Conception Phase...
[ARCHITECT] Invoking Architect agent...
[ARCHITECT] Reading seed materials from: seed/

[ARCHITECT] Analyzing requirements...
  ✓ Found: seed/requirements.md (PingPong Game)
  ✓ Project type: 2D Game
  ✓ Technology: Python 3.8+
  ✓ Complexity: Low-Medium

[ARCHITECT] Creating DNA.md...
  ✓ Sacred Architectural Rules defined
  ✓ Signal emission standards established
  ✓ Self-maintenance configured:
    - Apoptosis thresholds set
    - Homeostasis targets defined
    - Metabolic limits configured
    - Immune patterns established
  ✓ Technology stack chosen: Python + Terminal Display
  ✓ Module boundaries defined
  ✓ Generation roadmap created

[DNA] DNA.md created successfully!
[DNA] Location: .cybergenic/dna/DNA.md
[DNA] Size: 847 lines (under 1000 line limit ✓)

[GIT] Creating checkpoint...
[GIT] Commit: "Generation 0: Conception complete"

[SUCCESS] Conception phase complete!
[NEXT] Run /cybergenrun again to evolve Generation 1
```

### Step 6: Review Your DNA

Let's look at what the Architect created. Run:

```bash
/cybergendna
```

This displays your organism's DNA, which includes:

- **Project Description** - What you're building
- **Sacred Architectural Rules** - MUST be followed by all code
- **Signal Standards** - How components communicate
- **Self-Maintenance Config** - Automatic healing settings
- **Technology Stack** - Python, libraries, patterns
- **Module Structure** - How code is organized
- **Protein Capabilities** - Types of components needed
- **Generation Roadmap** - Plan for evolution

The DNA is typically 500-1000 lines and serves as the "genetic code" for your entire project.

---

## Evolution and Growth

Now the organism will grow through generations, building code that follows the DNA.

### Step 7: Evolve Generation 1

Run the framework again:

```bash
/cybergenrun
```

**What happens during Evolution:**

```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: SELF-MAINTENANCE CHECK                              │
└─────────────────────────────────────────────────────────────┘
  Checking homeostasis... ✓ All systems balanced
  Checking metabolic costs... ✓ No expensive proteins yet
  Checking apoptosis log... ✓ No dying proteins
  Checking immune system... ✓ Ready

┌─────────────────────────────────────────────────────────────┐
│ STEP 2: SIGNAL DISCOVERY                                    │
└─────────────────────────────────────────────────────────────┘
  Reading orphan signals... 0 orphans found (first generation)
  No proteins need replacement yet

┌─────────────────────────────────────────────────────────────┐
│ STEP 3: TRANSCRIPTION (DNA → RNA)                          │
└─────────────────────────────────────────────────────────────┘
  Coordinator reading DNA.md...
  Extracting Sacred Rules...
  Planning proteins to synthesize:
    1. Ball (Transform capability)
    2. Paddle (Transform capability)
    3. CollisionDetector (Validate capability)
    4. GameLoop (Coordinate capability)
    5. Renderer (Communicate capability)
    6. InputHandler (Communicate capability)
    7. ScoreKeeper (ManageState capability)

  Creating RNA work orders... ✓ 7 work orders created

┌─────────────────────────────────────────────────────────────┐
│ STEP 4: TRANSLATION (RNA → Protein)                        │
└─────────────────────────────────────────────────────────────┘
  Routing to specialized synthesizers:
    → Ball → synthesizer_transform
    → Paddle → synthesizer_transform
    → CollisionDetector → synthesizer_validate
    → GameLoop → synthesizer_coordinate
    → Renderer → synthesizer_communicate
    → InputHandler → synthesizer_communicate
    → ScoreKeeper → synthesizer_manage_state

  Synthesizing proteins (Haiku)...
    ✓ Ball synthesized (87 lines)
    ✓ Paddle synthesized (62 lines)
    ✓ CollisionDetector synthesized (134 lines)
    ✓ GameLoop synthesized (156 lines)
    ✓ Renderer synthesized (98 lines)
    ✓ InputHandler synthesized (71 lines)
    ✓ ScoreKeeper synthesized (45 lines)

┌─────────────────────────────────────────────────────────────┐
│ STEP 5: IMMUNE CHECK                                        │
└─────────────────────────────────────────────────────────────┘
  Scanning for threats...
    ✓ Ball - No threats detected
    ✓ Paddle - No threats detected
    ✓ CollisionDetector - No threats detected
    ✓ GameLoop - No threats detected
    ✓ Renderer - No threats detected
    ✓ InputHandler - No threats detected
    ✓ ScoreKeeper - No threats detected

  All proteins registered as "self" ✓

┌─────────────────────────────────────────────────────────────┐
│ STEP 6: VALIDATION (Chaperone)                             │
└─────────────────────────────────────────────────────────────┘
  Testing protein folding...
    ✓ Ball - All conformations valid
    ✓ Paddle - All conformations valid
    ✓ CollisionDetector - All conformations valid
    ✓ GameLoop - All conformations valid
    ✓ Renderer - All conformations valid
    ✓ InputHandler - All conformations valid
    ✓ ScoreKeeper - All conformations valid

  Verifying self-maintenance...
    ✓ All proteins have apoptosis logic
    ✓ All proteins emit signals
    ✓ All proteins track metabolic costs

┌─────────────────────────────────────────────────────────────┐
│ STEP 7: INTEGRATION                                         │
└─────────────────────────────────────────────────────────────┘
  Integrating proteins into modules...
    ✓ Created: output/modules/game_engine.py
    ✓ Created: output/modules/display.py
    ✓ Created: output/modules/input_system.py
    ✓ Created: output/proteins/ (7 protein files)

  Registering signal handlers...
    ✓ 7 proteins registered
    ✓ Signal bus configured

  Connecting to self-maintenance...
    ✓ Homeostasis monitoring enabled
    ✓ Metabolic tracking enabled
    ✓ Apoptosis monitoring enabled

┌─────────────────────────────────────────────────────────────┐
│ STEP 8: SIGNAL TRACKING                                    │
└─────────────────────────────────────────────────────────────┘
  Tracking signals emitted during synthesis:
    - BALL_CREATED (1x)
    - PADDLE_CREATED (2x)
    - COLLISION_DETECTED (orphan - no handler yet)
    - GAME_STARTED (orphan - no handler yet)
    - FRAME_RENDERED (orphan - no handler yet)

  New orphans detected: 3
  These will be handled in next generation if frequency > 10

┌─────────────────────────────────────────────────────────────┐
│ STEP 9: CHECKPOINT                                          │
└─────────────────────────────────────────────────────────────┘
  Creating git checkpoint...
  ✓ Committed: "Generation 1: 7 proteins synthesized"

[SUCCESS] Generation 1 complete!
[PROTEINS] 7 active proteins
[ORPHANS] 3 orphan signals detected
[NEXT] Run /cybergenrun to evolve Generation 2
```

### Step 8: Continue Evolving

The organism grows through multiple generations. Each generation:
- Handles orphan signals from previous runs
- Replaces proteins that died (apoptosis)
- Optimizes based on performance
- Adds new capabilities as needed

Run more generations:

```bash
/cybergenevolve 5
```

This evolves 5 generations automatically.

---

## Monitoring Your Organism

### Check Overall Status

```bash
/cybergenstatus
```

**Output:**
```
╔════════════════════════════════════════════════════════════════╗
║                    CYBERGENIC STATUS                           ║
╚════════════════════════════════════════════════════════════════╝

[GENERATION] Current: 3
[RUNS] Total: 4

[DNA] Status: Present
[DNA] Location: .cybergenic/dna/DNA.md
[DNA] Size: 847 lines
[DNA] Last Updated: 2025-10-18 14:23:45

[PROTEINS] Active: 12
[PROTEINS] Apoptotic: 1 (CollisionDetectorV1 - being replaced)
[PROTEINS] Total Synthesized: 13

[SIGNALS]
  ✓ Handled: 15
  ⚠ Orphans: 2 (low frequency)
  Coverage: 88%

[SELF-MAINTENANCE]
  ✓ Homeostasis: Balanced
  ✓ Metabolic Costs: Within limits
  ✓ Immune System: Active (0 threats)
  ✓ Apoptosis: 1 event (normal)
```

### Check Self-Maintenance Systems

```bash
/cybergenmaintenance
```

**Output:**
```
╔════════════════════════════════════════════════════════════════╗
║              SELF-MAINTENANCE SYSTEMS STATUS                   ║
╚════════════════════════════════════════════════════════════════╝

[HOMEOSTASIS] Resource Balancing
─────────────────────────────────────────────────────────────────
Metric              Current    Target    Deviation    Status
────────────────────────────────────────────────────────────────
CPU Load            0.58       0.70      -17%         ✓ OK
Memory Usage        0.61       0.80      -24%         ✓ OK
Error Rate          0.005      0.01      -50%         ✓ OK
API Cost/Hour       $0.42      $1.00     -58%         ✓ OK
Response Time       147ms      200ms     -27%         ✓ OK

[METABOLIC TRACKER] Resource Consumption
─────────────────────────────────────────────────────────────────
Protein              CPU (s)   Memory (MB)  API Tokens  Cost ($)
────────────────────────────────────────────────────────────────
GameLoop             0.234     12.4         0           $0.00
Renderer             0.187     8.7          0           $0.00
CollisionDetector    0.098     5.2          0           $0.00
InputHandler         0.045     3.1          0           $0.00
Ball                 0.023     1.8          0           $0.00
Paddle               0.021     1.6          0           $0.00
ScoreKeeper          0.012     0.9          0           $0.00

Total                0.620     33.7         0           $0.00

[APOPTOSIS] Programmed Cell Death
─────────────────────────────────────────────────────────────────
Recent Events: 1

Event #1
  Protein: CollisionDetectorV1
  Timestamp: 2025-10-18 14:31:22
  Reasons: excessive_errors_12
  Replacement: CollisionDetectorV2 (synthesized in Gen 3)

[IMMUNE SYSTEM] Threat Detection
─────────────────────────────────────────────────────────────────
Known Self: 12 proteins
Known Threats: 0 patterns
Threats Blocked: 0
Last Scan: 2025-10-18 14:35:10
Status: ✓ Healthy
```

### View All Proteins

```bash
/cybergenproteins
```

**Output:**
```
╔════════════════════════════════════════════════════════════════╗
║                     PROTEIN REGISTRY                           ║
╚════════════════════════════════════════════════════════════════╝

[ACTIVE PROTEINS] 12

1. Ball
   Capability: transform
   Conformations: update, reset, apply_spin
   Subscribes to: FRAME_UPDATE, COLLISION
   Emits: BALL_MOVED, EXTREME_VELOCITY
   Status: ✓ Active
   Health: 100% (0 errors, 1247 successful executions)

2. Paddle
   Capability: transform
   Conformations: move_up, move_down, reset
   Subscribes to: KEY_PRESSED, FRAME_UPDATE
   Emits: PADDLE_MOVED
   Status: ✓ Active
   Health: 100% (0 errors, 894 successful executions)

3. CollisionDetectorV2
   Capability: validate
   Conformations: check_ball_paddle, check_ball_wall
   Subscribes to: BALL_MOVED
   Emits: COLLISION, SCORE_EVENT
   Status: ✓ Active
   Health: 100% (0 errors, 1156 successful executions)

... (9 more proteins)

[APOPTOTIC PROTEINS] 1

CollisionDetectorV1 (died Generation 3)
  Reason: excessive_errors_12
  Replaced by: CollisionDetectorV2
```

### View Signal Activity

```bash
/cybergensignal
```

**Output:**
```
╔════════════════════════════════════════════════════════════════╗
║                   SIGNAL DISCOVERY STATUS                      ║
╚════════════════════════════════════════════════════════════════╝

[HANDLED SIGNALS] 15

Signal: BALL_MOVED
  Emitted by: Ball
  Handled by: CollisionDetectorV2, Renderer
  Frequency: 1247 times
  Status: ✓ Handled

Signal: COLLISION
  Emitted by: CollisionDetectorV2
  Handled by: Ball, ScoreKeeper
  Frequency: 89 times
  Status: ✓ Handled

... (13 more handled signals)

[ORPHAN SIGNALS] 2 (Need Handlers)

Signal: GAME_PAUSED
  Emitted by: GameLoop
  Handlers: None (orphan)
  Frequency: 3 times
  Priority: Low (frequency < 10)
  Suggestion: Will create PauseHandler in next generation if frequency increases

Signal: RENDER_LAG
  Emitted by: Renderer
  Handlers: None (orphan)
  Frequency: 7 times
  Priority: Medium
  Suggestion: Create PerformanceOptimizer if frequency reaches 10

[STATISTICS]
  Total Signals: 17
  Handled: 15 (88%)
  Orphans: 2 (12%)
  Avg Frequency: 147 emissions/signal
```

---

## Understanding Commands

Here's what each command does:

### Setup & Initialization
```bash
/cybergensetup
```
Creates the entire framework structure. Only run once per project.

### Running & Evolution
```bash
/cybergenrun
```
- **First run (Gen 0):** Creates DNA.md via Architect
- **Subsequent runs:** Evolves one generation (DNA→RNA→Protein)

```bash
/cybergenevolve 5
```
Evolves multiple generations automatically (replace 5 with desired number).

### Monitoring
```bash
/cybergenstatus
```
Shows current generation, proteins, signals, and system health.

```bash
/cybergenmaintenance
```
Detailed view of self-maintenance systems (homeostasis, metabolic, apoptosis, immune).

```bash
/cybergenproteins
```
Lists all proteins with their capabilities, signals, and health status.

```bash
/cybergensignal
```
Shows signal activity, orphans, and coverage statistics.

```bash
/cybergensignalstats
```
Detailed signal statistics and trends over generations.

### DNA Management
```bash
/cybergendna
```
Displays the current DNA.md (genetic code).

```bash
/cybergenDNA
```
Re-invokes Architect to update DNA.md based on:
- Current codebase
- Evolved proteins
- Orphan signal patterns
- Performance data

Use this after significant evolution to refine the architecture.

### Validation & Rollback
```bash
/cybergenvalidate
```
Runs Chaperone validation on all proteins to check for issues.

```bash
/cybergenrollback 3
```
Rolls back to Generation 3 (replace 3 with desired generation).

### Help & Information
```bash
/cybergenhelp
```
Shows command list and pre-run checklist.

```bash
/cybergenmcp
```
Displays MCP server configuration and status.

---

## Troubleshooting

### Problem: "No seed materials found"

**Solution:**
- Make sure `seed/requirements.md` exists and contains your project description
- Minimum requirement: A text file describing what you want to build
- Check that you're running commands from the correct directory

### Problem: "DNA.md not found"

**Solution:**
- Run `/cybergenrun` first to create DNA (this is Generation 0: Conception)
- DNA is created in `.cybergenic/dna/DNA.md`
- If it still fails, check setup completed successfully

### Problem: "Python module not found: psutil"

**Solution:**
```bash
pip install psutil
```
or
```bash
pip3 install psutil
```

### Problem: "Protein synthesis failed"

**Solution:**
- Check that all 11 agent files exist in `.claude/agents/`
- Verify you have access to Claude Sonnet 4.5 and Haiku 4 models
- Look at error messages for specific issues
- Check immune system logs: `cat .cybergenic/immune_memory.json`

### Problem: "Immune system rejecting all proteins"

**Solution:**
- Review `.cybergenic/immune_memory.json` for false positives
- The immune system learns from patterns - it may have learned incorrect threat patterns
- Check `immune_system.py` threat patterns if you have access to edit
- Try running `/cybergenDNA` to refresh configuration

### Problem: "All proteins dying (apoptosis)"

**Solution:**
- Check `.cybergenic/apoptosis_log.json` to see why proteins are dying
- Common reasons:
  - `excessive_errors` - Code has bugs
  - `low_success_rate` - Code fails too often
  - `unused` - Code hasn't run in 7+ days
- Review DNA.md apoptosis thresholds (might be too strict)
- Early generations often have higher error rates - this is normal

### Problem: "Many orphan signals"

**This is normal!**
- Orphan signals are discovered during runtime
- High-frequency orphans (>10 emissions) trigger new protein synthesis
- Each generation handles more orphans
- By Generation 5-10, most signals should have handlers

### Problem: "Commands not working in terminal"

**Solution:**
If using plain Python (not Claude Code):
```bash
python cybergen_orchestrator.py run        # Instead of /cybergenrun
python cybergen_orchestrator.py status     # Instead of /cybergenstatus
python cybergen_orchestrator.py evolve 5   # Instead of /cybergenevolve 5
```

---

## Next Steps

### Congratulations! You've grown your first organism!

Here's what to do next:

### 1. **Experiment with Different Seeds**

Try these project ideas:
- **Todo List App** - Simple CRUD application
- **Weather Dashboard** - Fetches and displays weather data
- **Chat Bot** - Simple conversational AI
- **File Organizer** - Sorts files by type/date
- **API Server** - REST API with endpoints

Each project will create different proteins and architectures!

### 2. **Monitor Health Over Time**

Run these commands regularly:
```bash
/cybergenstatus         # Overall health
/cybergenmaintenance    # Detailed systems
/cybergensignal         # Signal coverage
```

Watch how the organism self-optimizes and self-heals.

### 3. **Study the DNA**

Read your DNA.md to understand:
- What Sacred Rules were created
- How signal standards work
- Self-maintenance configurations
- Module architecture

This helps you write better seed requirements!

### 4. **Learn from Proteins**

Look at the generated proteins in `output/proteins/`:
- See how self-monitoring works
- Study signal emission patterns
- Understand apoptosis logic
- Learn conformational switching

### 5. **Advanced Techniques**

Once comfortable, try:
- **Custom threat patterns** in `immune_system.py`
- **Adjusting homeostasis targets** in `homeostasis.py`
- **Framework patterns** in `framework/` directory
- **Multi-generation experiments** with `/cybergenevolve 20`

### 6. **Read the Documentation**

- [README.md](README.md) - Deep dive into concepts
- [WORKFLOW.md](WORKFLOW.md) - How each generation works
- [COMMANDS.md](COMMANDS.md) - Complete command reference

### 7. **Understand the Workflow**

The [WORKFLOW.md](WORKFLOW.md) file shows exactly what happens during:
- Generation 0 (Conception)
- Generation 1+ (Evolution)
- Runtime (Self-Maintenance)
- Signal Discovery
- Apoptosis Events
- Immune Responses

This helps you understand why your organism makes certain decisions.

### 8. **Join the Community** (if available)

Share your organisms, learn from others, and contribute improvements!

---

## Tips for Success

### DO:
✓ **Start small** - Simple projects help you learn
✓ **Be detailed** - Better seed = better organism
✓ **Monitor often** - Use status commands frequently
✓ **Trust the process** - Early generations are messy
✓ **Let it evolve** - 10-20 generations show true potential
✓ **Read the signals** - They tell you what's needed
✓ **Use git** - Framework creates checkpoints automatically

### DON'T:
✗ **Rush evolution** - Let each generation complete
✗ **Panic about orphans** - They're discovered naturally
✗ **Fight apoptosis** - It removes bad code automatically
✗ **Ignore maintenance** - Check `/cybergenmaintenance` regularly
✗ **Edit generated code** - The organism maintains itself
✗ **Expect perfection** - Evolution takes time

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────┐
│                    CYBERGENIC QUICK REFERENCE               │
├─────────────────────────────────────────────────────────────┤
│ SETUP                                                       │
│   python setup_cybergenic.py    Setup framework            │
│   Edit seed/requirements.md     Add your project           │
│                                                              │
│ RUNNING                                                     │
│   /cybergenrun                   Run one generation        │
│   /cybergenevolve N              Run N generations         │
│                                                              │
│ MONITORING                                                  │
│   /cybergenstatus                Overall status            │
│   /cybergenmaintenance           Self-maintenance details  │
│   /cybergenproteins              List all proteins         │
│   /cybergensignal                Signal activity           │
│                                                              │
│ DNA MANAGEMENT                                              │
│   /cybergendna                   View DNA                  │
│   /cybergenDNA                   Update DNA                │
│                                                              │
│ TROUBLESHOOTING                                             │
│   /cybergenvalidate              Validate proteins         │
│   /cybergenrollback N            Rollback to generation N  │
│   /cybergenhelp                  Show help                 │
└─────────────────────────────────────────────────────────────┘
```

---

## Remember

**"Don't write code. Grow self-maintaining organisms through signal-driven evolution."**

You're not a programmer anymore - you're a gardener tending to a living software organism.

Have fun growing! 🌱

---

**Need more help?**
- Check [README.md](README.md) for concepts
- Check [WORKFLOW.md](WORKFLOW.md) for detailed processes
- Check [COMMANDS.md](COMMANDS.md) for all commands
- Review your DNA.md for project-specific rules
