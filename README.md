# Cybergenic
Grow applications instead of coding them. This framework uses biological evolution principles to create self-healing, self-optimizing software that discovers its own architecture through runtime signals. Reduces maintenance to zero and AI costs by 70-80%.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

README.md
Cybergenic Framework

## Overview

The **Cybergenic Framework** is a revolutionary software development paradigm where applications literally "grow" from a seed specification through controlled evolutionary processes, mimicking biological development from embryo to mature organism with **self-healing, self-optimizing capabilities**.

**Core Principle:** "Don't write code. Grow self-maintaining organisms through signal-driven evolution."

## What Makes This Revolutionary

### 1. Biological Development Model
Applications grow through stages like real organisms:
- **Conception:** Architect creates DNA.md with architectural rules
- **Transcription:** Sonnet reads DNA, creates RNA work orders
- **Translation:** Haiku synthesizes proteins (complete classes)
- **Validation:** Chaperones check folding, immune system checks threats
- **Integration:** Proteins assembled into functional modules
- **Evolution:** Each generation builds on previous, driven by signals

### 2. Signal-Driven Architecture
- Every component emits signals for significant events
- Orphan signals (no handlers) are tracked automatically
- High-frequency orphans trigger adaptive protein synthesis
- Architecture emerges from actual runtime behavior

### 3. Self-Maintenance Systems

#### Apoptosis (Programmed Cell Death)
- Proteins monitor their own health (error rates, usage, success rate)
- Bad proteins self-destruct automatically
- Emit replacement requests
- No manual cleanup needed

#### Homeostasis (Automatic Balancing)
- Continuously monitors: CPU load, memory, error rates, API costs
- Applies negative feedback when deviation exceeds thresholds
- Proteins switch conformations in response
- System self-optimizes in real-time

#### Metabolic Cost Tracking
- Tracks resource consumption per protein (CPU, memory, API tokens)
- Identifies expensive proteins
- Triggers optimization signals
- Budget-aware evolution

#### Immune System (Threat Detection)
- Distinguishes "self" (trusted code) from "non-self" (threats)
- Scans all new code for malicious patterns
- Learns from past threats (immune memory)
- Automatic quarantine of dangerous code

## Key Concepts

### The Central Dogma
```
DNA (Framework + Sacred Rules)
  ↓ TRANSCRIPTION (by Sonnet)
RNA (Work Orders with specs)
  ↓ TRANSLATION (by Haiku)
PROTEIN (Complete Class with conformations)
  ↓ IMMUNE CHECK
VALIDATED PROTEIN
  ↓ RUNTIME
SIGNAL EMISSION + SELF-MONITORING
  ↓
HOMEOSTASIS + APOPTOSIS + METABOLISM
  ↓
ORPHAN SIGNAL DETECTION
  ↓
ADAPTIVE SYNTHESIS (next generation)
```

### Proteins are Classes, Not Functions

A protein is a complete class with:
- **Multiple conformational states** (different methods for different conditions)
- **Active site** (public interface that responds to signals)
- **Self-monitoring** (tracks errors, usage, health)
- **Apoptosis logic** (can self-destruct when broken)
- **Signal emission** (broadcasts events to ecosystem)

Example:
```python
class PhysicsIntegrator:  # The protein
    def __init__(self):
        self.conformation = "euler"
        self.error_count = 0
        
    def _integrate_euler(self, obj, dt):  # Fast conformation
        ...
    
    def _integrate_verlet(self, obj, dt):  # Stable conformation
        ...
    
    def integrate(self, obj, dt, signal=None):  # Active site
        if signal == "HIGH_LOAD":
            return self._integrate_euler(obj, dt)
        else:
            return self._integrate_verlet(obj, dt)
```

### Agent Hierarchy

| Agent | Model | Role | Reads DNA? | Count |
|-------|-------|------|------------|-------|
| **Architect** | Sonnet 4.5 | Creates DNA.md | Creates it | 1 |
| **Coordinator** | Sonnet 4.5 | Transcribes DNA→RNA, routes to specialized synthesizers | Yes | 1 |
| **Specialized Synthesizers** | Haiku 4 | Translate RNA→Protein (8 specialized types) | No | 8 |
| **Chaperone** | Haiku 4 | Validates folding | No | 1 |

**Total: 11 Agents**

**Specialized Synthesizers by Capability:**
- Transform - Data transformation proteins
- Validate - Data validation proteins
- ManageState - State management proteins
- Coordinate - Multi-protein coordination proteins
- Communicate - External I/O proteins
- Monitor - System observation proteins
- Decide - Policy and decision-making proteins
- Adapt - Interface adaptation proteins

**Self-Maintenance Systems** (Automated):
- Immune System
- Homeostasis Controller
- Metabolic Tracker
- Apoptosis Manager

## Folder Structure
```
project/
├── .cybergenic/
│   ├── dna/
│   │   ├── DNA.md                      # Genetic code (Sacred Rules)
│   │   └── DNA.md.backup               # Backup of previous DNA
│   ├── generations/                    # Generation snapshots
│   ├── context/                        # Context data (gitignored)
│   ├── signals/                        # Signal logs
│   ├── proteins/                       # Synthesized proteins
│   ├── immune/                         # Immune system data
│   ├── metabolism/                     # Metabolic cost data
│   ├── generation_counter.txt          # Current generation number
│   ├── run_counter.txt                 # Total runs
│   ├── signal_log.json                 # All signals emitted
│   ├── signal_discovery.json           # Orphan signal tracking
│   ├── protein_registry.json           # All proteins catalog
│   ├── immune_memory.json              # Known threats
│   ├── metabolic_costs.json            # Cost tracking per protein
│   ├── homeostasis_state.json          # Current homeostasis state
│   └── apoptosis_log.json              # Apoptosis events
│
├── .claude/
│   ├── agents/
│   │   ├── architect.md                # Architect agent (Sonnet 4.5)
│   │   ├── coordinator.md              # Coordinator agent (Sonnet 4.5)
│   │   ├── synthesizer_transform.md    # Transform protein synthesizer (Haiku 4)
│   │   ├── synthesizer_validate.md     # Validate protein synthesizer (Haiku 4)
│   │   ├── synthesizer_manage_state.md # State management synthesizer (Haiku 4)
│   │   ├── synthesizer_coordinate.md   # Coordination synthesizer (Haiku 4)
│   │   ├── synthesizer_communicate.md  # Communication synthesizer (Haiku 4)
│   │   ├── synthesizer_monitor.md      # Monitoring synthesizer (Haiku 4)
│   │   ├── synthesizer_decide.md       # Decision synthesizer (Haiku 4)
│   │   ├── synthesizer_adapt.md        # Adaptation synthesizer (Haiku 4)
│   │   └── chaperone.md                # Chaperone validator (Haiku 4)
│   ├── commands/
│   │   └── cybergen_commands.md        # Command definitions
│   └── mcp.json                        # MCP server configuration (optional)
│
├── seed/
│   ├── documents/                      # Seed documentation
│   ├── images/                         # Seed images
│   └── requirements/                   # Seed requirements
│
├── framework/
│   ├── templates/                      # Framework templates
│   ├── patterns/                       # Architectural patterns
│   └── rules/                          # Framework rules
│
├── output/
│   ├── proteins/                       # Generated protein files
│   ├── modules/                        # Integrated modules
│   ├── tests/                          # Generated tests
│   └── docs/                           # Generated documentation
│
├── cybergen_orchestrator.py            # Main orchestrator
├── immune_system.py                    # Immune system implementation
├── homeostasis.py                      # Homeostasis controller
├── metabolic_tracker.py                # Metabolic cost tracker
├── apoptosis.py                        # Apoptosis system
├── signal_bus.py                       # Signal bus implementation
└── README.md                           # This file
```

## Core Files (Required)

These Python files implement the self-maintenance systems and must be present:

- **`immune_system.py`** - Threat detection and quarantine
- **`homeostasis.py`** - Resource balancing through feedback loops
- **`metabolic_tracker.py`** - Cost tracking and optimization
- **`apoptosis.py`** - Programmed cell death for proteins
- **`signal_bus.py`** - Signal emission and subscription
- **`cybergen_orchestrator.py`** - Main orchestration logic
- **`setup_cybergenic.py`** - Framework setup script

The setup script (`setup_cybergenic.py`) creates the directory structure and configuration files.

## Protein Capability Space

Proteins can have these capabilities:

1. **Transform** - Pure data transformation (input → output)
2. **Validate** - Check data integrity
3. **Manage State** - Handle mutable state safely
4. **Coordinate** - Orchestrate other proteins
5. **Communicate** - External I/O (API, files, databases)
6. **Monitor** - Observe and report metrics
7. **Decide** - Apply rules and policies
8. **Adapt** - Translate between interfaces

## Benefits

### For Developers
- **70-80% cost reduction** vs manual AI coding (hierarchical model usage)
- **No manual maintenance** - organisms self-heal
- **Automatic optimization** - homeostasis handles resource management
- **Security built-in** - immune system validates all code
- **Expertise encoded** in reusable frameworks

### For the Ecosystem
- **Knowledge becomes reproducible** through frameworks
- **Natural selection** improves framework quality
- **Community-driven evolution** of best practices
- **Lowered barrier** to entry for complex domains

### For the Organism
- **Self-healing** - bad proteins self-destruct and get replaced
- **Self-optimizing** - automatically adjusts to load/cost/errors
- **Self-defending** - immune system blocks threats
- **Adaptive** - discovers needed capabilities from signals

## Quick Start

1. **Setup**: Run `python setup_cybergenic.py` or `/cybergensetup`
   - Creates all directories, tracking files, and agent definitions
   - Initializes git repository
   - Creates MCP configuration
   - Generates `seed/requirements.md` template

2. **Add Seed**: Edit `seed/requirements.md` with your project description

3. **Conception**: Run `/cybergenrun` (creates DNA.md via Architect)

4. **Evolution**: Run `/cybergenrun` again to evolve generations

5. **Monitor**: Use `/cybergenstatus` and `/cybergenmaintenance` to observe

See [SETUP.md](SETUP.md) for detailed instructions.

## Commands

- `/cybergensetup` - Initialize framework
- `/cybergenrun` - Execute conception or evolution
- `/cybergenstatus` - Show organism status
- `/cybergenmaintenance` - Show self-maintenance systems status
- `/cybergenevolve N` - Evolve N generations
- `/cybergendna` - View DNA.md
- `/cybergenproteins` - List all proteins
- `/cybergensignal` - View signal discovery status

See [COMMANDS.md](COMMANDS.md) for complete command reference.

## MCP Tools (Optional)

Model Context Protocol servers provide enhanced capabilities:
- `@modelcontextprotocol/server-memory` - Persistent memory
- `@modelcontextprotocol/server-sequential-thinking` - Enhanced reasoning
- `@modelcontextprotocol/server-filesystem` - File access

MCP is optional but recommended for complex projects.

## Version

Version: 6.0.0 - Self-Maintaining Organisms
Last Updated: October 2025
Status: Production Ready

---

**"Don't write code. Grow self-maintaining organisms through signal-driven evolution."**


## License
This project is licensed under AGPL v3 for open source use.
Commercial licenses available - contact sesassa68@gmail.com for pricing.

This software is available under two licenses:
1. AGPL v3 (see LICENSE-AGPL)
2. Commercial License (contact for terms)




## License
This project is licensed under AGPL v3 for open source use.
Commercial licenses available - contact sesassa68@gmail.com for pricing.

This software is available under two licenses:
1. AGPL v3 (see LICENSE-AGPL)
2. Commercial License (contact for terms)
