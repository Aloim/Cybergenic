# Cybergenic Framework
Grow applications instead of coding them. This framework uses biological evolution principles to create self-healing, self-optimizing software that discovers its own architecture through runtime signals. The Cybergenic Framework is an agentic orchestration setup with various helper scripts designed for Claude Code projects to generate code or entire applications through evolutionary processes rather than traditional manual development.

The core concept is inspired by the Mixture of Experts architecture from machine learning (https://en.wikipedia.org/wiki/Mixture_of_experts), but extends far beyond simple model routing into a comprehensive evolutionary system. While traditional Mixture of Experts focuses on routing inputs to specialized neural network models, Cybergenic applies this principle to actual code generation and evolution, adding layers of biological sophistication including self-maintenance systems, architectural growth, and lifecycle management.

Instead of writing code directly, developers define architectural DNA containing rules and patterns. The system then generates multiple protein variants (complete code classes) for each capability, which compete against each other using real production signals. Through a two-stage selection process involving simulation filtering and regulatory competition, the system identifies winning variants based on actual performance data such as success rates, response times, and resource efficiency. The framework includes self-maintenance systems like apoptosis for automatic removal of failing code, homeostasis for resource balancing, an immune system for threat detection, and metabolic tracking for cost optimization. As the application matures, it can crystallize winning variants into optimized single-path code, removing competition infrastructure and producing a lean production-ready application that has been proven through real evolutionary pressure rather than guesswork.


---

## IMPORTANT NOTICE

**This project is currently Work In Progress (WIP).**

Agentic workflows and autonomous code generation are **not yet as reliable as they should be**. Expect:
- Incomplete generations
- Occasional failures in protein synthesis
- Self-maintenance systems still being refined
- Bugs and unexpected behavior

**Use at your own risk. This is experimental software.**

What helps is during the 1st Generation run (or generally immediately after you start the generation) prompt them something like this as reminder "Use the proper cybergenic workflow using multiple Haiku agents, Split the Tasks down with Sonnet for those. Make Sure to Send Signals After each task"

---

## Installation & Version Information

### Two Versions Available

#### 1. ClaudeCode Version (Recommended - Stable)

**Status**: Working - Ready to use

**Requirements**:
- Claude Max subscription (required for Claude Code access)
- Python 3.8 or higher
- Git

**Installation**:
1. Download or clone this repository
2. Copy **all contents** (including `.claude/` and `.cybergenic/` folders) to your project root directory
3. Your project structure should look like:
```
   your-project/
   ├── .claude/
   ├── .cybergenic/
   ├── seed/
   ├── output/
   └── [your other project files]
```
4. Run `/cybergensetup` in Claude Code to initialize(restart Claudecode if the command doesnt appear)

#### 2. Local LLM Version (Experimental)

**Status**: Work In Progress - DO NOT USE YET

This version is designed for better control using local LLMs (Ollama, LM Studio, etc.) together with claudecode but is currently incomplete and non-functional.


**Current status**: Under active development. Not ready for testing.

---

### Which Version Should I Use?

- **Want to try it now?** → Use the **ClaudeCode version**


---

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Cybergenic Framework

## Overview

<img width="833" height="1966" alt="cybergenic_evolution_cycle" src="https://github.com/user-attachments/assets/1643ce83-bc50-4abb-a79c-b25254e8d50b" /><img width="2450" height="2760" alt="cybergenic_complete_workflow" src="https://github.com/user-attachments/assets/4c9975b4-cb96-4471-ae3b-e5b5a709670b" />
<img width="1947" height="1553" alt="cybergenic_protein_analogy" src="https://github.com/user-attachments/assets/0e7908ea-bca5-4069-8e74-cec6b0be2cbc" />



The **Cybergenic Framework** is a revolutionary software development paradigm where applications literally "grow" from a seed specification through controlled evolutionary processes, mimicking biological development from embryo to mature organism with **self-healing, self-optimizing capabilities**.

**Core Principle:** "Don't write code. Grow self-maintaining organisms through signal-driven evolution."

---

##  Getting Started

**New to Cybergenic?** Start here:

1. **Read [Tutorial.md]** - Complete beginner's guide with a PingPong game example
2. **Understand the concepts** - Read this README for the "why" and "how"
3. **Study the workflow** - Check [WORKFLOW.md] to see what happens during evolution
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
- **Potential 70-80% cost reduction in future versions** vs manual AI coding (hierarchical model usage)
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

See [Tutorial.md] for a complete step-by-step beginner's guide.

## Commands

- `/cybergensetup` - Initialize framework
- `/cybergenrun` - Execute conception or evolution
- `/cybergenstatus` - Show organism status
- `/cybergenmaintenance` - Show self-maintenance systems status
- `/cybergenevolve N` - Evolve N generations
- `/cybergendna` - View DNA.md
- `/cybergenproteins` - List all proteins
- `/cybergensignal` - View signal discovery status

See [COMMANDS.md] for complete command reference.

## Documentation

This framework includes comprehensive documentation for different user levels:

- **[Tutorial.md]** - Complete beginner's guide with step-by-step instructions
  - Prerequisites and installation
  - Understanding the basics
  - PingPong game example (full walkthrough)
  - Monitoring and troubleshooting
  - Tips for success

- **[README.md]** (this file) - Overview and concepts
  - What makes Cybergenic revolutionary
  - Key concepts and architecture
  - Agent hierarchy and capabilities
  - Quick start guide

- **[WORKFLOW.md]** - Detailed generation lifecycle
  - What happens during Conception (Generation 0)
  - What happens during Evolution (Generation 1+)
  - Self-maintenance system workflows
  - Signal discovery process

- **[COMMANDS.md]** - Complete command reference
  - All available commands
  - Command syntax and parameters
  - Usage examples

## MCP Tools (Optional)

Model Context Protocol servers provide enhanced capabilities:
- `@modelcontextprotocol/server-memory` - Persistent memory
- `@modelcontextprotocol/server-sequential-thinking` - Enhanced reasoning
- `@modelcontextprotocol/server-filesystem` - File access

MCP is optional but recommended for complex projects.


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
