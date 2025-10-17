COMMANDS.md
markdown# Cybergenic Framework Commands

## Documentation Reading Philosophy

**IMPORTANT:** Each Cybergenic command operates with full awareness of the framework's documentation and state. Commands are not simple scripts—they are intelligent agents that:

1. **Read relevant documentation** before executing to understand context and philosophy
2. **Access state files** in `.cybergenic/` to understand the organism's current condition
3. **Reference the 4 core documentation files** as needed:
   - **[README.md](README.md)** - Framework overview, core concepts, and philosophy
   - **[SETUP.md](SETUP.md)** - Detailed setup instructions and configuration
   - **[WORKFLOW.md](WORKFLOW.md)** - Complete generation lifecycle and self-maintenance workflows
   - **[COMMANDS.md](COMMANDS.md)** - Command reference and usage patterns

4. **Access framework directories** intelligently:
   - `seed/` - Project requirements and source materials
   - `framework/` - Optional framework templates and patterns
   - `output/` - Evolved codebase and generated proteins
   - `.cybergenic/` - All organism state and tracking files
   - `.claude/` - Agent definitions and MCP configuration

Each command below lists its **Required Documentation Reading** to ensure proper execution. This is not optional—commands should actively read and understand these files to function correctly within the Cybergenic philosophy.

---

## Setup Commands

### /cybergensetup

**Purpose:** Initialize the complete Cybergenic Framework structure

**Required Documentation Reading:**
This command should read and reference the following documentation files:
- [README.md](README.md) - For understanding the framework overview, core concepts, and folder structure
- [SETUP.md](SETUP.md) - For detailed setup steps, prerequisites, and verification checklist
- [WORKFLOW.md](WORKFLOW.md) - For understanding the complete generation lifecycle and self-maintenance systems
- [COMMANDS.md](COMMANDS.md) - For command reference and usage patterns

**What it does:**

1. **Directory Structure Creation:**
   - Creates `.cybergenic/` with subdirectories:
     - `dna/` - DNA.md storage and backups
     - `generations/` - Generation history snapshots
     - `context/` - Context data (gitignored)
     - `signals/` - Signal emission logs
     - `proteins/` - Synthesized protein storage
     - `immune/` - Immune system data and threat logs
     - `metabolism/` - Metabolic cost tracking data

   - Creates `.claude/` with subdirectories:
     - `agents/` - Agent definitions (Architect, Coordinator, Synthesizer, Chaperone)
     - `commands/` - Command definitions for all cybergen commands

   - Creates `seed/` with subdirectories:
     - `documents/` - Project documentation
     - `images/` - Images and mockups
     - `requirements/` - Requirements files

   - Creates `framework/` with subdirectories:
     - `templates/` - Framework templates (optional)
     - `patterns/` - Architectural patterns (optional)
     - `rules/` - Framework rules (optional)

   - Creates `output/` with subdirectories:
     - `proteins/` - Generated protein files
     - `modules/` - Integrated modules
     - `tests/` - Generated tests
     - `docs/` - Generated documentation

2. **Tracking Files Initialization:**
   - `generation_counter.txt` - Set to 0
   - `run_counter.txt` - Set to 0
   - `signal_log.json` - Empty signal log
   - `signal_discovery.json` - Empty orphan signal tracker
   - `protein_registry.json` - Empty protein catalog
   - `immune_memory.json` - Empty threat database
   - `metabolic_costs.json` - Empty cost tracker
   - `homeostasis_state.json` - Initial homeostasis configuration
   - `apoptosis_log.json` - Empty apoptosis event log

3. **Self-Maintenance System Files:**
   Creates Python implementation files:
   - `immune_system.py` - Threat detection and quarantine system
   - `homeostasis.py` - Resource balancing controller with negative feedback loops
   - `metabolic_tracker.py` - Cost tracking and optimization triggers
   - `apoptosis.py` - Programmed cell death system for proteins
   - `signal_bus.py` - Signal emission and subscription infrastructure
   - `cybergen_orchestrator.py` - Main orchestration logic coordinating all systems

4. **Git Repository:**
   - Initializes Git repository if not already present
   - Creates `.gitignore` with appropriate exclusions:
     - `.cybergenic/context/` (context data)
     - `__pycache__/`
     - `*.pyc`
     - `.env`

5. **Agent Definitions:**
   Creates agent configuration files in `.claude/agents/`:
   - `architect.md` - Architect agent (Opus 4/Sonnet 4.5) for DNA synthesis
   - `coordinator.md` - Coordinator agent (Sonnet 4.5) for transcription (DNA→RNA)
   - `synthesizer.md` - Synthesizer agent (Haiku 4) for translation (RNA→Protein)
   - `chaperone.md` - Chaperone agent (Haiku 4) for protein validation

6. **MCP Configuration (Optional):**
   - Creates `.claude/mcp.json` with optional MCP server configurations:
     - `@modelcontextprotocol/server-memory` - Persistent memory
     - `@modelcontextprotocol/server-sequential-thinking` - Enhanced reasoning
     - `@modelcontextprotocol/server-filesystem` - File access

**Usage:**
```bash
/cybergensetup
```

**Output:**
```
[SETUP] Initializing Cybergenic Framework...

[DIRECTORIES] Creating structure...
  ✓ .cybergenic/ (dna, generations, context, signals, proteins, immune, metabolism)
  ✓ .claude/ (agents, commands)
  ✓ seed/ (documents, images, requirements)
  ✓ framework/ (templates, patterns, rules)
  ✓ output/ (proteins, modules, tests, docs)

[TRACKING] Initializing state files...
  ✓ generation_counter.txt (0)
  ✓ run_counter.txt (0)
  ✓ signal_log.json
  ✓ signal_discovery.json
  ✓ protein_registry.json
  ✓ immune_memory.json
  ✓ metabolic_costs.json
  ✓ homeostasis_state.json
  ✓ apoptosis_log.json

[SELF-MAINTENANCE] Creating system files...
  ✓ immune_system.py (threat detection)
  ✓ homeostasis.py (resource balancing)
  ✓ metabolic_tracker.py (cost tracking)
  ✓ apoptosis.py (programmed cell death)
  ✓ signal_bus.py (signal infrastructure)
  ✓ cybergen_orchestrator.py (main orchestrator)

[AGENTS] Creating agent definitions...
  ✓ architect.md (DNA synthesis - Opus 4/Sonnet 4.5)
  ✓ coordinator.md (Transcription - Sonnet 4.5)
  ✓ synthesizer.md (Translation - Haiku 4)
  ✓ chaperone.md (Validation - Haiku 4)

[GIT] Initializing repository...
  ✓ Git repository initialized
  ✓ .gitignore created

[MCP] Creating MCP configuration (optional)...
  ✓ .claude/mcp.json created

[SUCCESS] Cybergenic Framework initialized!

Next steps:
1. Add seed materials to /seed/ (minimum: requirements.md)
2. Review documentation in README.md, SETUP.md, WORKFLOW.md
3. Run /cybergenrun to begin conception
4. Use /cybergenhelp for detailed guidance

For detailed setup instructions, see SETUP.md
For workflow understanding, see WORKFLOW.md
```

**Prerequisites:**
- Python 3.8+ installed
- Git installed and configured
- Sufficient disk space for evolution history
- (Optional) Node.js & npm for MCP servers

**Post-Setup Verification:**
Run these commands to verify setup:
```bash
ls .cybergenic    # Should show all subdirectories
ls .claude/agents # Should show 4 agent files
git status        # Should show initialized repository
/cybergenstatus   # Should show initial state
```

---

## Core Commands

### /cybergenrun

**Purpose:** Execute the growth process (conception or evolution)

**Required Documentation Reading:**
This command should read and reference:
- [README.md](README.md) - For the Central Dogma and core concepts
- [WORKFLOW.md](WORKFLOW.md) - For detailed generation lifecycle (Conception and Evolution phases)
- `.cybergenic/dna/DNA.md` - The organism's genetic code (read by Coordinator during transcription)
- `seed/` directory files - Project requirements (read during Conception)

**Behavior:**
- **First run (counter=0):** Runs Conception with Architect
  - Reads ALL files in `seed/` directory (documents, images, requirements)
  - Reads `README.md` to understand framework philosophy
  - Creates DNA.md with Sacred Rules
  - Configures self-maintenance systems
  - Sets up signal standards

- **Subsequent runs:** Evolves next generation
  - Reads `DNA.md` for Sacred Rules and architecture
  - Reads `WORKFLOW.md` for self-maintenance system workflows
  - Checks self-maintenance systems
  - Discovers orphan signals
  - Transcribes DNA → RNA
  - Synthesizes proteins
  - Validates and integrates

**Usage:**
```bash
/cybergenrun
```

**Output (First run):**
```
[FIRST RUN] Initiating Conception Phase...
[DNA] Invoking Architect for DNA synthesis...
[SUCCESS] DNA.md created successfully
[GENOME] Sacred Rules + Self-Maintenance Config encoded
```

**Output (Subsequent):**
```
[GENERATION 3] Self-Maintaining Signal-Driven Evolution
[STEP 1: SELF-MAINTENANCE CHECK]
   [HOMEOSTASIS] CPU: 0.72 (target: 0.70)
   [APOPTOSIS] 1 protein dying: NetworkClient
[STEP 2: SIGNAL DISCOVERY]
   Orphan signals: 12
   Replacements needed: 1
[STEP 3: TRANSCRIPTION]
   ✓ Generated 4 RNA work orders
[STEP 4: TRANSLATION]
   Ribosome 1/4: VelocityLimiter
   [IMMUNE] ✓ Check passed
   [CHAPERONE] ✓ Folded correctly
...
[GENERATION 3 COMPLETE]
   Active proteins: 15 (+2 from generation 2)
   System health: GOOD
```

---

### /cybergenstatus

**Purpose:** Show current organism status

**Required Documentation Reading:**
- [WORKFLOW.md](WORKFLOW.md) - For understanding self-maintenance system states
- `.cybergenic/` state files - All tracking files (counters, logs, registries)

**What it shows:**
- Run count and current generation
- DNA presence
- Active protein count
- Signal discovery statistics
- Self-maintenance system status (brief)

**Usage:**
```bash
/cybergenstatus
```

**Output:**
```
[CYBERGENIC ORGANISM STATUS]
   Run Count: 5
   Current Generation: 4
   DNA Present: True
   Active Proteins: 15

[SIGNAL DISCOVERY]
   Orphan Signals: 8
   Handled Signals: 23
   High-Priority Orphans: 2

[SELF-MAINTENANCE SYSTEMS]
   Homeostasis: CPU: 0.72, Memory: 0.65
   Metabolic Tracker: 2 expensive proteins
   Apoptosis: 1 event total
   Immune System: 15 known self, 0 threats
```

---

### /cybergenmaintenance

**Purpose:** Show detailed self-maintenance systems status

**Required Documentation Reading:**
- [README.md](README.md) - For self-maintenance systems overview
- [WORKFLOW.md](WORKFLOW.md) - For detailed self-maintenance workflows (Homeostasis, Apoptosis, Metabolic, Immune)
- `.cybergenic/homeostasis_state.json` - Current homeostasis metrics
- `.cybergenic/metabolic_costs.json` - Protein cost data
- `.cybergenic/apoptosis_log.json` - Apoptosis event history
- `.cybergenic/immune_memory.json` - Threat database

**What it shows:**
- Homeostasis: All metrics with deviations
- Metabolic: Top expensive proteins with costs
- Apoptosis: Event history and reasons
- Immune: Known self, known threats, patterns

**Usage:**
```bash
/cybergenmaintenance
```

**Output:**
```
[SELF-MAINTENANCE SYSTEMS DETAILED STATUS]

[HOMEOSTASIS CONTROLLER]
   Set Points:
      cpu_load: 0.72 (target: 0.70, deviation: +2.9%) [OK]
      memory_usage: 0.65 (target: 0.80, deviation: -18.8%) [OK]
      error_rate: 0.008 (target: 0.01, deviation: -20.0%) [OK]

[METABOLIC COST TRACKER]
   Total proteins tracked: 15
   Expensive proteins: 2
   Total executions: 1,547

   Expensive Proteins:
      AIDecisionMaker:
         CPU: 0.112s, Memory: 45.2MB
         Cost: $0.68 total
         Executions: 89

[APOPTOSIS SYSTEM]
   Total apoptosis events: 1
   Reason breakdown:
      excessive_errors_11: 1
   Last event: NetworkClient (2025-10-17T14:23:15)

[IMMUNE SYSTEM]
   Known self proteins: 15
   Known threats: 0
   Threat patterns monitored: 8
```

---

## Generation Management

### /cybergenevolve N

**Purpose:** Evolve N generations

**Required Documentation Reading:**
- [WORKFLOW.md](WORKFLOW.md) - Complete generation lifecycle
- All documentation required by `/cybergenrun` command

**Usage:**
```bash
/cybergenevolve 5
```

**What it does:**
- Runs the evolution process N times
- Each generation follows full lifecycle (see `/cybergenrun`)
- Shows progress for each generation

**Output:**
```
Evolving 5 generations...

[GENERATION 4] ...
[GENERATION 4 COMPLETE]

[GENERATION 5] ...
[GENERATION 5 COMPLETE]

...

All 5 generations complete!
```

---

### /cybergenrollback N

**Purpose:** Rollback to generation N

**Required Documentation Reading:**
- [WORKFLOW.md](WORKFLOW.md) - Checkpoint system
- `.cybergenic/generations/` directory - Generation snapshots
- Git history - For generation commits

**Usage:**
```bash
/cybergenrollback 3
```

**What it does:**
- Uses Git to checkout generation N commit
- Restores all state files from that generation
- Updates generation counter to N
- Restores all `.cybergenic/` tracking files

**Warning:** This is destructive. Current work will be lost.

---

## DNA Management

### /cybergendna

**Purpose:** Display current DNA.md with Sacred Rules

**Required Documentation Reading:**
- `.cybergenic/dna/DNA.md` - The organism's complete genetic code

**Usage:**
```bash
/cybergendna
```

**Output:**
Shows the complete DNA.md file contents.

---

### /cybergenDNA

**Purpose:** Update DNA.md based on current organism state

**Required Documentation Reading:**
This command should read and analyze:
- [README.md](README.md) - Framework philosophy and Sacred Rules concepts
- [WORKFLOW.md](WORKFLOW.md) - DNA Update Flow workflow
- `seed/` directory - All original seed materials
- `output/` directory - All evolved codebase
- `.cybergenic/protein_registry.json` - All proteins catalog
- `.cybergenic/signal_discovery.json` - Orphan signal patterns
- `.cybergenic/apoptosis_log.json` - Apoptosis events for learning
- `.cybergenic/dna/DNA.md` - Current DNA for comparison

**When to use:**
- After significant evolution (10+ generations)
- When patterns have emerged
- When DNA has become stale
- When DNA exceeds 1000 lines

**What it does:**
- Re-analyzes seed materials
- Analyzes evolved codebase
- Reviews protein registry
- Reviews orphan signal patterns
- Reviews apoptosis events
- Updates Sacred Rules
- Compresses if needed

**Usage:**
```bash
/cybergenDNA
```

**Output:**
```
[DNA UPDATE] Re-analyzing organism state...
[STATUS] Current Generation: 12
[ANALYSIS] Scanning codebase... Found 47 code files
[OPUS] Invoking Architect for DNA re-synthesis...
[SUCCESS] DNA.md updated!
   Old size: 867 lines
   New size: 743 lines
   Reduced by 124 lines (14.3%)
```

---

## Monitoring Commands

### /cybergenproteins

**Purpose:** List all synthesized proteins with details

**Required Documentation Reading:**
- [README.md](README.md) - For understanding proteins as classes concept
- [WORKFLOW.md](WORKFLOW.md) - For protein synthesis workflow (Translation step)
- `.cybergenic/protein_registry.json` - Complete protein catalog

**Usage:**
```bash
/cybergenproteins
```

**Output:**
```
[PROTEIN REGISTRY] Synthesized Proteins

   Protein: PhysicsIntegrator
   Generation: 1
   Status: active
   Conformational States:
      - euler
      - verlet
      - rk4
   Handles: HIGH_LOAD, PRECISION_REQUIRED
   Emits: PHYSICS_COMPLETE, INTEGRATION_FAILED

   Protein: VelocityLimiter
   Generation: 3
   Status: active
   Conformational States:
      - clamp
      - dampen
   Handles: EXTREME_VELOCITY
   Emits: VELOCITY_CLAMPED, VELOCITY_REJECTED

...

Total: 15 active proteins
```

---

### /cybergensignal

**Purpose:** Show detailed signal discovery status

**Required Documentation Reading:**
- [README.md](README.md) - Signal-Driven Architecture concept
- [WORKFLOW.md](WORKFLOW.md) - Signal Discovery and Orphan Signal Discovery workflows
- `.cybergenic/signal_log.json` - All emitted signals
- `.cybergenic/signal_discovery.json` - Orphan signal tracking

**Usage:**
```bash
/cybergensignal
```

**Output:**
```
[SIGNAL DISCOVERY SYSTEM]

[OVERVIEW]
   Total Orphan Signals: 8
   Total Handled Signals: 23
   Average Orphan Frequency: 12.3 emissions

[HIGH-PRIORITY ORPHANS]

   NETWORK_TIMEOUT
      Emissions: 34
      First seen: Gen 2
      Severity: high
      Recent context: {"url": "api.example.com", "timeout": 5}

   DATABASE_SLOW_QUERY
      Emissions: 18
      First seen: Gen 3
      Severity: medium

[SIGNAL COVERAGE]
   Coverage: 74.2% (23/31 signals handled)
```

---

### /cybergenmcp

**Purpose:** Display MCP server configuration and status

**Required Documentation Reading:**
- [README.md](README.md) - MCP Tools section
- [SETUP.md](SETUP.md) - MCP configuration instructions
- `.claude/mcp.json` - MCP server configuration

**Usage:**
```bash
/cybergenmcp
```

**Output:**
```
[MCP] Model Context Protocol Status

[CONFIG] .claude/mcp.json
[SERVERS] 3 configured

  Server: memory
    Command: npx
    Args: -y @modelcontextprotocol/server-memory
    Status: Will auto-install via npx

  Server: sequential-thinking
    Command: npx
    Args: -y @modelcontextprotocol/server-sequential-thinking
    Status: Will auto-install via npx

How agents use MCP tools:
  - Architect: memory, sequential-thinking for planning
  - Coordinator: memory for pattern recall
```

---

## Validation Commands

### /cybergenvalidate

**Purpose:** Run chaperone validation suite on all proteins

**Required Documentation Reading:**
- [WORKFLOW.md](WORKFLOW.md) - Validation (Chaperone checks folding) step
- [README.md](README.md) - Proteins are Classes concept
- `.cybergenic/protein_registry.json` - All proteins to validate
- `output/proteins/` directory - Actual protein code files

**Usage:**
```bash
/cybergenvalidate
```

**What it does:**
- Tests all active proteins
- Validates conformational states
- Checks signal emission
- Verifies self-maintenance hooks
- Reports any issues

**Output:**
```
[VALIDATION] Running chaperone suite on 15 proteins...

PhysicsIntegrator: ✓ PASS
VelocityLimiter: ✓ PASS
NetworkClient: ✗ FAIL
   Error: Missing signal emission: RETRY_ATTEMPTED
   Recommendation: Re-synthesize

...

Results: 14 passed, 1 failed
```

---

## Help Command

### /cybergenhelp

**Purpose:** Show help and pre-flight checklist

**Required Documentation Reading:**
This command should read and present information from:
- [README.md](README.md) - Complete framework overview
- [SETUP.md](SETUP.md) - Setup instructions and checklist
- [WORKFLOW.md](WORKFLOW.md) - Complete workflows
- [COMMANDS.md](COMMANDS.md) - All command documentation
- [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) - Comprehensive guide (if available)

**Usage:**
```bash
/cybergenhelp
```

**Output:**
Shows complete help documentation including:
- Pre-flight checklist
- Command list
- Workflow overview
- Sacred Rules explanation
- DNA.md philosophy
- Self-maintenance system overview
- Tips and best practices

---

## Command Workflow Examples

### Initial Setup
```bash
/cybergensetup
# Add seed materials
/cybergenhelp
/cybergenrun  # Conception
```

### Development Cycle
```bash
/cybergenrun       # Evolve generation
/cybergenstatus    # Check status
/cybergensignal    # See what's needed
/cybergenevolve 3  # Evolve more
/cybergenmaintenance  # Check health
```

### Maintenance
```bash
/cybergenproteins     # See all proteins
/cybergenvalidate     # Validate health
/cybergenDNA          # Update DNA if needed
/cybergenmaintenance  # Monitor systems
```

### Troubleshooting
```bash
/cybergenstatus          # What's wrong?
/cybergenmaintenance     # System health?
/cybergensignal          # Missing capabilities?
/cybergenrollback 5      # Go back if needed
```

---

## Command Quick Reference

| Command | Purpose | Use When |
|---------|---------|----------|
| `/cybergensetup` | Initialize | Starting new project |
| `/cybergenrun` | Evolve | Every development cycle |
| `/cybergenstatus` | Status | Want quick overview |
| `/cybergenmaintenance` | Health check | Monitoring organism |
| `/cybergenevolve N` | Multi-evolve | Want rapid evolution |
| `/cybergendna` | View DNA | Understanding rules |
| `/cybergenDNA` | Update DNA | After major evolution |
| `/cybergenproteins` | List proteins | See what exists |
| `/cybergensignal` | Signal status | Find gaps |
| `/cybergenvalidate` | Validate | Check integrity |
| `/cybergenrollback N` | Rollback | Need to undo |
| `/cybergenmcp` | MCP status | Check tools |
| `/cybergenhelp` | Help | Need guidance |

---

**Remember:** Commands are designed to be run frequently. The organism needs regular evolution cycles t