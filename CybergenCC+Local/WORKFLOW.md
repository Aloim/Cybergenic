markdown# Cybergenic Framework Workflow

## Complete Generation Lifecycle

### Generation 0: Conception
```
User provides Seed → Architect (Opus/Sonnet 4.5) invoked
  ↓
Architect analyzes:
  - Seed materials (requirements, docs, assets)
  - Framework patterns (if selected)
  ↓
Architect creates DNA.md:
  - Project description
  - Sacred Architectural Rules
  - Signal emission standards
  - Self-maintenance configuration:
    * Apoptosis thresholds
    * Homeostasis set points
    * Metabolic cost limits
    * Immune threat patterns
  - Technology stack
  - Generation roadmap
  ↓
Architect emits signals:
  - DNA_CREATED
  - ARCHITECTURE_DEFINED
  - SELF_MAINTENANCE_CONFIGURED
  ↓
Git checkpoint: "Generation 0: Conception complete"
```

### Generation 1+: Evolution with Self-Maintenance
```
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: SELF-MAINTENANCE CHECK                              │
├─────────────────────────────────────────────────────────────┤
│ Homeostasis:        Check CPU, memory, errors, costs       │
│   ↓ If deviation > 10%: Emit corrective signals            │
│                                                              │
│ Metabolic Tracker:  Identify expensive proteins             │
│   ↓ If avg_cost > threshold: Emit PROTEIN_TOO_EXPENSIVE    │
│                                                              │
│ Apoptosis:          Scan all proteins for health           │
│   ↓ For each protein:                                       │
│       - Check error_count > threshold                       │
│       - Check last_execution > 7 days                       │
│       - Check success_rate < 50%                            │
│   ↓ If unhealthy: Initiate apoptosis                       │
│       - Emit APOPTOSIS_INITIATED                            │
│       - Emit PROTEIN_REPLACEMENT_NEEDED                     │
│                                                              │
│ Immune System:      Report status                           │
│   ↓ Known self: X proteins                                  │
│   ↓ Known threats: Y patterns                               │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: SIGNAL DISCOVERY                                    │
├─────────────────────────────────────────────────────────────┤
│ Read signal_discovery.json                                  │
│   ↓ Orphan signals (emitted but not handled):              │
│       - EXTREME_VELOCITY: 47 emissions                      │
│       - NETWORK_ERROR: 23 emissions                         │
│   ↓ Calculate priorities (frequency × severity)             │
│                                                              │
│ Read apoptosis_log.json                                     │
│   ↓ Dying proteins need replacements:                       │
│       - NetworkClient (12 errors)                           │
│                                                              │
│ Generate protein suggestions:                               │
│   ↓ For orphan signals:                                     │
│       - VelocityLimiter (handles EXTREME_VELOCITY)          │
│       - NetworkErrorHandler (handles NETWORK_ERROR)         │
│   ↓ For apoptosis:                                          │
│       - NetworkClientV2 (replacement with better logic)     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: TRANSCRIPTION (DNA → RNA)                          │
├─────────────────────────────────────────────────────────────┤
│ Sonnet (Coordinator) reads DNA.md                           │
│   ↓ Extracts Sacred Rules relevant to this generation       │
│   ↓ Reviews orphan signal suggestions                       │
│   ↓ Reviews apoptosis replacement needs                     │
│                                                              │
│ For each protein to synthesize:                             │
│   ↓ Create RNA work order specifying:                       │
│       - Protein name & purpose                              │
│       - Conformational states (methods)                     │
│       - Active site (public interface)                      │
│       - Signals to respond to (subscribe)                   │
│       - Signals to emit (broadcast)                         │
│       - Self-maintenance requirements:                      │
│         * error_count tracking                              │
│         * apoptosis threshold                               │
│         * metabolic cost hooks                              │
│       - Capability type                                     │
│       - Constraints from DNA                                │
│                                                              │
│ Emit signals:                                               │
│   - RNA_WORK_ORDER_CREATED (for each)                      │
│   - ORPHAN_HANDLER_PLANNED                                  │
│   - REPLACEMENT_PROTEIN_PLANNED                             │
│   - TRANSCRIPTION_COMPLETE                                  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 4: TRANSLATION (RNA → Protein)                        │
├─────────────────────────────────────────────────────────────┤
│ For each RNA work order:                                    │
│   ↓ Coordinator routes to SPECIALIZED Haiku Synthesizer    │
│       based on capability type:                             │
│       - Transform → synthesizer_transform                   │
│       - Validate → synthesizer_validate                     │
│       - ManageState → synthesizer_manage_state              │
│       - Coordinate → synthesizer_coordinate                 │
│       - Communicate → synthesizer_communicate               │
│       - Monitor → synthesizer_monitor                       │
│       - Decide → synthesizer_decide                         │
│       - Adapt → synthesizer_adapt                           │
│                                                              │
│   ↓ Specialized Haiku synthesizes complete class:           │
│       - Haiku NEVER sees DNA.md                             │
│       - Haiku receives complete RNA work order              │
│       - Synthesizer optimized for this capability type      │
│                                                              │
│   ↓ Synthesizer creates protein with:                       │
│       class ProteinName:                                    │
│         def __init__(self):                                 │
│           self.error_count = 0                              │
│           self.last_execution = now()                       │
│           self.apoptosis_threshold = 10                     │
│                                                              │
│         def _conformation_1(self): ...                      │
│         def _conformation_2(self): ...                      │
│                                                              │
│         def active_site(self, data, signal=None):           │
│           # Switch conformations based on signal            │
│           # Track execution                                 │
│           # Emit signals                                    │
│           # Check if should_die()                           │
│                                                              │
│         def should_die(self) -> bool:                       │
│           # Apoptosis decision logic                        │
│                                                              │
│         def initiate_apoptosis(self):                       │
│           # Self-destruct and request replacement           │
│                                                              │
│   ↓ Emit: PROTEIN_SYNTHESIZED                              │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 5: IMMUNE CHECK                                        │
├─────────────────────────────────────────────────────────────┤
│ Immune System receives synthesized protein code             │
│   ↓ Compute signature (SHA-256)                             │
│   ↓ Check if recognized self                                │
│       - If yes: Allow deployment                            │
│       - If no: Scan for threats                             │
│                                                              │
│ Threat scanning:                                            │
│   ↓ Check for dangerous patterns:                           │
│       - eval(), exec(), __import__                          │
│       - os.system(), subprocess                             │
│       - while True: without break                           │
│       - SQL injection patterns                              │
│       - Path traversal                                      │
│   ↓ Check against immune memory (known threats)             │
│                                                              │
│ If threats found:                                           │
│   ↓ Quarantine protein                                      │
│   ↓ Add to immune memory                                    │
│   ↓ Emit: THREAT_DETECTED, THREAT_QUARANTINED              │
│   ↓ Reject deployment                                       │
│                                                              │
│ If clean:                                                   │
│   ↓ Register as self                                        │
│   ↓ Emit: IMMUNE_CHECK_PASSED                              │
│   ↓ Allow to proceed                                        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 6: VALIDATION (Chaperone checks folding)              │
├─────────────────────────────────────────────────────────────┤
│ Chaperone (Haiku validator) receives protein                │
│   ↓ Test all conformational states                          │
│   ↓ Verify active site responds to signals                  │
│   ↓ Verify signal emission implemented                      │
│   ↓ Verify self-monitoring present:                         │
│       - error_count, last_execution variables               │
│       - should_die() method                                 │
│       - initiate_apoptosis() method                         │
│       - metabolic_tracker calls                             │
│   ↓ Check constraints from RNA                              │
│   ↓ Run unit tests on each conformation                     │
│                                                              │
│ If correctly folded:                                        │
│   ↓ Emit: FOLDED_CORRECTLY                                 │
│   ↓ Forward to integration                                  │
│                                                              │
│ If misfolded:                                               │
│   ↓ Emit: MISFOLD (with diagnostics)                       │
│   ↓ Request re-synthesis or escalate                        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 7: INTEGRATION                                         │
├─────────────────────────────────────────────────────────────┤
│ Sonnet collects validated proteins                          │
│   ↓ Register signal handlers:                               │
│       protein.subscribe_to(signals)                         │
│   ↓ Connect to self-maintenance:                            │
│       homeostasis.register(protein)                         │
│       metabolic_tracker.register(protein)                   │
│   ↓ Enable apoptosis self-monitoring                        │
│   ↓ Integrate into modules                                  │
│   ↓ Add coordination code                                   │
│   ↓ Validate against DNA Sacred Rules                       │
│                                                              │
│ Update registries:                                          │
│   ↓ signal_discovery.json: mark orphans as handled          │
│   ↓ protein_registry.json: register new proteins            │
│                                                              │
│ Emit signals:                                               │
│   - SIGNAL_HANDLER_REGISTERED (for each)                   │
│   - SELF_MAINTENANCE_ENABLED                                │
│   - PROTEIN_INTEGRATED                                      │
│   - MODULE_READY                                            │
│   - ORPHAN_SIGNAL_HANDLED                                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 8: SIGNAL TRACKING UPDATE                             │
├─────────────────────────────────────────────────────────────┤
│ Review all signals emitted this generation                  │
│   ↓ Identify new orphan signals                             │
│   ↓ Calculate signal frequencies                            │
│   ↓ Update signal_discovery.json                            │
│                                                              │
│ Statistics:                                                 │
│   - Orphans handled: X                                      │
│   - New orphans detected: Y                                 │
│   - Remaining orphans: Z                                    │
│   - Signal coverage: W%                                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 9: CHECKPOINT                                          │
├─────────────────────────────────────────────────────────────┤
│ Git commit all changes                                      │
│ Save all state files                                        │
│ Increment generation counter                                │
│ Emit: GENERATION_COMPLETE, CHECKPOINT_CREATED              │
└─────────────────────────────────────────────────────────────┘
```

## Runtime: Self-Maintenance in Action

### Homeostasis Feedback Loop
```
[Continuous Monitoring]
  ↓
Measure CPU load: 85%
Target: 70%
Deviation: +15% (exceeds 10% threshold)
  ↓
Homeostasis emits: HIGH_LOAD signal
  ↓
All proteins receive signal via SignalBus
  ↓
Proteins switch conformations:
  - PhysicsIntegrator → euler (fast)
  - CollisionDetector → approximate (fast)
  - Renderer → low_quality (fast)
  ↓
CPU load drops to 72%
  ↓
Within threshold - balance achieved
  ↓
Continue monitoring...
```

### Apoptosis Event
```
[Protein Execution]
  ↓
NetworkClient.connect() fails
error_count: 11 (threshold: 10)
  ↓
should_die() returns True
  ↓
initiate_apoptosis() called
  ↓
Cleanup resources
  ↓
Emit: APOPTOSIS_INITIATED
Data: {protein: NetworkClient, reason: "excessive_errors_11"}
  ↓
Emit: PROTEIN_REPLACEMENT_NEEDED
Data: {protein: NetworkClient, capabilities: ["communicate"]}
  ↓
Mark self as apoptotic
  ↓
[Next Generation]
Sonnet sees replacement request
  ↓
Creates NetworkClientV2 with improved error handling
  ↓
NetworkClientV2 deployed
Old NetworkClient removed
```

### Orphan Signal Discovery
```
[Generation 1]
PhysicsIntegrator.integrate() runs
  ↓
Detects velocity > 1000
  ↓
Emits: EXTREME_VELOCITY
  ↓
SignalBus: No handlers registered (orphan!)
  ↓
signal_discovery.json updated:
  EXTREME_VELOCITY: count=1
  ↓
[Continues for 46 more times this generation]
  ↓
End of generation: EXTREME_VELOCITY count=47
  ↓
[Generation 2]
Signal Discovery: EXTREME_VELOCITY is high-priority (>10)
  ↓
Suggests: VelocityLimiter protein
  ↓
Sonnet creates RNA for VelocityLimiter
  ↓
Haiku synthesizes VelocityLimiter
  ↓
VelocityLimiter deployed, subscribes to EXTREME_VELOCITY
  ↓
[Generation 3]
PhysicsIntegrator emits EXTREME_VELOCITY
  ↓
VelocityLimiter.handle() called automatically
  ↓
Velocity clamped
  ↓
Emit: VELOCITY_CLAMPED (new orphan signal!)
  ↓
Cycle continues...
```

## Key Workflows

### DNA Update Flow
```
User runs: /cybergenDNA
  ↓
Architect re-analyzes:
  - Current seed materials
  - Evolved codebase
  - Protein registry
  - Orphan signal patterns
  - Apoptosis events
  ↓
Updates DNA.md:
  - Refine Sacred Rules based on what worked
  - Update self-maintenance thresholds
  - Adjust generation roadmap
  - Compress if needed (<1000 lines)
  ↓
Backup old DNA → DNA.md.backup
  ↓
Save new DNA.md
  ↓
Git commit
```

### Immune Response to Threat
```
Haiku synthesizes MaliciousProtein
  ↓
Contains: eval(user_input)
  ↓
Immune System scans code
  ↓
Pattern match: "eval(" → code_injection
  ↓
Threat detected
  ↓
Quarantine protein (don't deploy)
  ↓
Add to immune_memory.json
  ↓
Emit: THREAT_DETECTED, THREAT_QUARANTINED
  ↓
Notify Sonnet: synthesis failed
  ↓
[Later attempt with similar pattern]
Immune memory recognizes immediately
  ↓
Instant rejection (learned defense)
```

## Signal Flow Diagram
```
┌──────────────┐
│   Protein A  │───┐
└──────────────┘   │
                   │ emits SIGNAL_X
┌──────────────┐   │
│   Protein B  │───┤
└──────────────┘   │
                   ▼
              ┌─────────────┐
              │ SignalBus   │
              └─────────────┘
                   │
        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼
   ┌─────────┐ ┌─────────┐ ┌──────────────┐
   │Protein C│ │Protein D│ │OrphanTracker │
   │(handles)│ │(handles)│ │(no handler!) │
   └─────────┘ └─────────┘ └──────────────┘
                                  │
                                  ▼
                          [Next Generation]
                          Synthesize handler
```

---

**The organism grows, heals, optimizes, and defends itself autonomously.**

SETUP.md
markdown# Cybergenic Framework Setup Guide

## Prerequisites

- Python 3.8+
- Git
- Claude Code CLI (optional but recommended)
- Node.js & npm (for MCP servers, optional)

## Step-by-Step Setup

### Step 1: Initialize Directory Structure

Run the setup command in your project directory:
```bash
/cybergensetup
```

This creates:
```
.cybergenic/              # Core framework data
  ├── dna/                # DNA.md storage
  ├── generations/        # Generation history
  ├── signals/            # Signal logs
  ├── proteins/           # Protein storage
  ├── immune/             # Immune system data
  └── metabolism/         # Cost tracking

.claude/                  # Claude agent configs
  ├── agents/             # Agent definitions
  └── commands/           # Command definitions

seed/                     # Your project seed
  ├── documents/
  ├── images/
  └── requirements/

framework/                # Framework templates (optional)

output/                   # Generated code
  ├── proteins/
  ├── modules/
  └── tests/
```

### Step 2: Create Self-Maintenance System Files

The setup command should create these Python files automatically. If not, create them manually:

**Required files:**
- `immune_system.py` - Threat detection
- `homeostasis.py` - Resource balancing
- `metabolic_tracker.py` - Cost tracking
- `apoptosis.py` - Programmed cell death
- `signal_bus.py` - Signal infrastructure
- `cybergen_orchestrator.py` - Main orchestrator

These files implement the self-maintenance systems and should not need modification.

### Step 3: Configure MCP Servers (Optional)

If you want enhanced AI capabilities:

Create `.claude/mcp.json`:
```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "."]
    }
  }
}
```

Servers auto-install when Claude Code starts.

Verify with:
```bash
/cybergenmcp
```

### Step 4: Add Your Seed Materials

Place your project requirements in the `seed/` directory:
```bash
seed/
  ├── requirements.md         # Project requirements
  ├── documents/
  │   ├── design_doc.md
  │   └── api_spec.md
  ├── images/
  │   └── mockups.png
  └── requirements/
      └── features.txt
```

**Minimum required:** A requirements file describing what you want to build.

### Step 5: Run Conception

Execute the first run to create DNA.md:
```bash
/cybergenrun
```

This invokes the Architect to:
- Analyze your seed materials
- Create DNA.md with Sacred Rules
- Configure self-maintenance systems
- Design initial architecture

Output:
```
[FIRST RUN] Initiating Conception Phase...
[DNA] Invoking Architect for DNA synthesis...
[SUCCESS] DNA.md created successfully
[GENOME] Sacred Rules + Self-Maintenance Config encoded
```

### Step 6: Review DNA.md

Check the generated DNA:
```bash
/cybergendna
```

The DNA.md contains:
- Project description
- Sacred Architectural Rules
- Signal emission standards
- Apoptosis thresholds
- Homeostasis set points
- Technology stack decisions
- Generation roadmap

### Step 7: Evolve First Generation

Run evolution:
```bash
/cybergenrun
```

This will:
1. Check self-maintenance systems
2. Discover orphan signals
3. Create RNA work orders
4. Synthesize proteins
5. Validate with immune system and chaperones
6. Integrate proteins
7. Track new signals

### Step 8: Monitor Organism

Check status:
```bash
/cybergenstatus
```

Shows:
- Current generation
- Active proteins
- Orphan signals
- Self-maintenance system health

Detailed self-maintenance status:
```bash
/cybergenmaintenance
```

Shows:
- Homeostasis metrics
- Metabolic costs per protein
- Apoptosis events
- Immune system status

### Step 9: Continue Evolution

Evolve multiple generations:
```bash
/cybergenevolve 5
```

Or evolve one at a time:
```bash
/cybergenrun
/cybergenrun
/cybergenrun
```

### Step 10: Manage Organism

View proteins:
```bash
/cybergenproteins
```

View signals:
```bash
/cybergensignal
```

Update DNA based on evolution:
```bash
/cybergenDNA
```

Rollback if needed:
```bash
/cybergenrollback 3
```

## Verification Checklist

After setup, verify:

- [ ] `.cybergenic/` directory exists
- [ ] Git repository initialized
- [ ] Python self-maintenance files present
- [ ] Seed materials added
- [ ] `/cybergenrun` executes without errors
- [ ] DNA.md created in `.cybergenic/dna/`
- [ ] `/cybergenstatus` shows organism info
- [ ] `/cybergenmaintenance` shows self-maintenance systems

## Troubleshooting

### "No seed materials found"
- Add at least one file to `seed/` directory
- Minimum: `seed/requirements.md` with project description

### "DNA.md not found"
- Run `/cybergenrun` first (conception phase)
- Check `.cybergenic/dna/DNA.md` was created

### "Protein synthesis failed"
- Check agent definitions in `.claude/agents/`
- Verify Haiku/Sonnet models accessible
- Check immune system logs for threats

### "Immune system rejecting all proteins"
- Review `immune_memory.json` for false positives
- Check threat patterns in `immune_system.py`
- May need to adjust threat detection sensitivity

### "Apoptosis killing all proteins"
- Check thresholds in DNA.md
- Review `apoptosis_log.json` for reasons
- Proteins may have legitimate high error rates during early evolution

## Advanced Configuration

### Adjust Homeostasis Set Points

Edit in DNA.md or directly in code:
```python
self.set_points = {
    "cpu_load": 0.7,           # Target 70%
    "memory_usage": 0.8,       # Target 80%
    "error_rate": 0.01,        # Target 1%
    "api_cost_per_hour": 1.0   # Target $1/hour
}
```

### Adjust Apoptosis Thresholds

Edit in DNA.md:
```markdown
### RULE: [CRITICAL] Apoptosis Configuration

Default thresholds:
- max_error_count: 10
- max_unused_days: 7
- min_success_rate: 0.5
```

### Add Custom Threat Patterns

Edit `immune_system.py`:
```python
self.threat_patterns = [
    # Add your patterns
    ("dangerous_function(", "custom_threat"),
]
```

### Adjust Metabolic Cost Thresholds

Edit in `metabolic_tracker.py`:
```python
self.thresholds = {
    'cpu_seconds': 0.1,
    'memory_mb': 100,
    'api_tokens': 10000,
    'cost_usd': 0.01
}
```

## Next Steps

1. **Let it evolve**: Run `/cybergenevolve 10` and observe
2. **Monitor health**: Regularly check `/cybergenmaintenance`
3. **Watch signals**: Use `/cybergensignal` to see emerging needs
4. **Update DNA**: Run `/cybergenDNA` after significant evolution
5. **Experiment**: Try different seed materials

## Tips

- **Start small**: Simple projects evolve faster and teach you the system
- **Watch apoptosis**: High apoptosis rate means proteins are struggling
- **Monitor orphans**: Many orphans mean the organism needs capabilities
- **Trust the process**: Early generations are messy, later ones stabilize
- **Use checkpoints**: Git checkpoints let you rollback failed experiments
- **Read the signals**: Signal logs tell you what the organism needs

---

**Your self-maintaining organism is ready to grow!**