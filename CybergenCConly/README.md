README.md
markdown# Cybergenic Framework

## Overview

The **Cybergenic Framework** is a revolutionary software development paradigm where applications literally "grow" from a seed specification through controlled evolutionary processes, mimicking biological development from embryo to mature organism with **self-healing, self-optimizing capabilities**.

**Core Principle:** "Don't write code. Grow self-maintaining organisms through signal-driven evolution."

---

##  Getting Started

**New to Cybergenic?** Start here:

1. **Read [Tutorial.md](Tutorial.md)** - Complete beginner's guide with a PingPong game example
2. **Understand the concepts** - Read this README for the "why" and "how"
3. **Study the workflow** - Check [WORKFLOW.md](WORKFLOW.md) to see what happens during evolution
4. **Run your first organism** - Follow the Quick Start section below

**Key Requirements:**
- Python 3.8+
- Git (recommended)
- psutil package (`pip install psutil`)

---

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

**How Routing Works:**
The Coordinator analyzes each RNA work order's capability type and routes it to the appropriate specialized synthesizer:
- Transform proteins → `synthesizer_transform.md`
- Validate proteins → `synthesizer_validate.md`
- ManageState proteins → `synthesizer_manage_state.md`
- Coordinate proteins → `synthesizer_coordinate.md`
- Communicate proteins → `synthesizer_communicate.md`
- Monitor proteins → `synthesizer_monitor.md`
- Decide proteins → `synthesizer_decide.md`
- Adapt proteins → `synthesizer_adapt.md`

This ensures each protein is synthesized by an agent with deep expertise in that capability type.

**Why Specialized Synthesizers?**
- **Better Code Quality**: Each synthesizer knows the patterns and anti-patterns for its capability
- **Fewer Errors**: Specialized knowledge reduces misfolding and validation failures
- **Consistent Patterns**: All Transform proteins follow Transform best practices
- **Faster Synthesis**: Specialized agents work more efficiently within their domain
- **Lower Apoptosis Rate**: Better initial quality means fewer proteins die and need replacement

**Specialized Synthesizers by Capability:**

Each synthesizer is optimized for a specific protein type, with specialized knowledge of patterns, best practices, and common pitfalls:

1. **Transform** (`synthesizer_transform.md`) - Data transformation proteins
   - Pure functions, immutability, composability
   - Format conversion, data mapping, filtering operations

2. **Validate** (`synthesizer_validate.md`) - Data validation proteins
   - Schema validation, business rules, constraint checking
   - Clear error messages, composable validation rules

3. **ManageState** (`synthesizer_manage_state.md`) - State management proteins
   - Thread safety, transactional support, audit trails
   - Game state, sessions, cache management, configuration

4. **Coordinate** (`synthesizer_coordinate.md`) - Multi-protein coordination proteins
   - Workflow orchestration, error handling, parallel execution
   - Request pipelines, multi-step processes, saga patterns

5. **Communicate** (`synthesizer_communicate.md`) - External I/O proteins
   - Retry logic, timeouts, circuit breakers, rate limiting
   - API clients, file I/O, database connections, message queues

6. **Monitor** (`synthesizer_monitor.md`) - System observation proteins
   - Low overhead, aggregation, threshold detection, trend analysis
   - Performance monitoring, health checks, resource tracking

7. **Decide** (`synthesizer_decide.md`) - Policy and decision-making proteins
   - Explainable decisions, deterministic logic, audit logging
   - Admission control, load balancing, feature flags, authorization

8. **Adapt** (`synthesizer_adapt.md`) - Interface adaptation proteins
   - Version handling, backward compatibility, semantic translation
   - Legacy adapters, protocol adapters, format converters

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
   - Creates all directories and tracking files
   - Generates 11 agent definitions:
     - 1 Architect (Sonnet 4.5)
     - 1 Coordinator (Sonnet 4.5)
     - 8 Specialized Synthesizers (Haiku 4)
     - 1 Chaperone (Haiku 4)
   - Initializes git repository
   - Creates MCP configuration (optional)
   - Generates `seed/requirements.md` template

2. **Add Seed**: Edit `seed/requirements.md` with your project description

3. **Conception**: Run `/cybergenrun` (creates DNA.md via Architect)

4. **Evolution**: Run `/cybergenrun` again to evolve generations

5. **Monitor**: Use `/cybergenstatus` and `/cybergenmaintenance` to observe

See [Tutorial.md](Tutorial.md) for a complete step-by-step beginner's guide.

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

## Documentation

This framework includes comprehensive documentation for different user levels:

- **[Tutorial.md](Tutorial.md)** - Complete beginner's guide with step-by-step instructions
  - Prerequisites and installation
  - Understanding the basics
  - PingPong game example (full walkthrough)
  - Monitoring and troubleshooting
  - Tips for success

- **[README.md](README.md)** (this file) - Overview and concepts
  - What makes Cybergenic revolutionary
  - Key concepts and architecture
  - Agent hierarchy and capabilities
  - Quick start guide

- **[WORKFLOW.md](WORKFLOW.md)** - Detailed generation lifecycle
  - What happens during Conception (Generation 0)
  - What happens during Evolution (Generation 1+)
  - Self-maintenance system workflows
  - Signal discovery process

- **[COMMANDS.md](COMMANDS.md)** - Complete command reference
  - All available commands
  - Command syntax and parameters
  - Usage examples

## MCP Tools (Optional)

Model Context Protocol servers provide enhanced capabilities:
- `@modelcontextprotocol/server-memory` - Persistent memory
- `@modelcontextprotocol/server-sequential-thinking` - Enhanced reasoning
- `@modelcontextprotocol/server-filesystem` - File access

MCP is optional but recommended for complex projects.

## Version

**Version: 7.0.0 - Specialized Synthesizers**
- Added 8 specialized synthesizers for capability-specific protein synthesis
- Enhanced routing logic in Coordinator
- Improved protein quality through specialized expertise
- Expanded documentation with Tutorial.md

Previous: 6.0.0 - Self-Maintaining Organisms

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