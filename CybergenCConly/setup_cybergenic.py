#!/usr/bin/env python3
"""
Cybergenic Framework Setup Script
Creates all necessary directories, files, and configurations
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

def create_directory_structure():
    """Create the complete Cybergenic directory structure"""

    directories = [
        # Core cybergenic directories
        '.cybergenic/dna',
        '.cybergenic/generations',
        '.cybergenic/context',
        '.cybergenic/signals',
        '.cybergenic/proteins',
        '.cybergenic/immune',
        '.cybergenic/metabolism',

        # Claude agent directories
        '.claude/agents',
        '.claude/commands',

        # Seed directories
        'seed/documents',
        'seed/images',
        'seed/requirements',

        # Framework directories (optional)
        'framework/templates',
        'framework/patterns',
        'framework/rules',

        # Output directories
        'output/proteins',
        'output/modules',
        'output/tests',
        'output/docs',
    ]

    print("[SETUP] Creating directory structure...")
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"   [OK] Created {directory}/")

def create_tracking_files():
    """Create initial tracking files"""

    print("\n[SETUP] Creating tracking files...")

    # Counter files
    Path('.cybergenic/generation_counter.txt').write_text('0')
    Path('.cybergenic/run_counter.txt').write_text('0')
    print("   [OK] Created generation_counter.txt")
    print("   [OK] Created run_counter.txt")

    # JSON tracking files
    tracking_files = {
        '.cybergenic/signal_log.json': [],
        '.cybergenic/signal_discovery.json': {
            "orphans": {},
            "handled": {},
            "history": [],
            "generation_stats": {}
        },
        '.cybergenic/protein_registry.json': {},
        '.cybergenic/immune_memory.json': {
            'threats': [],
            'known_self_count': 0,
            'last_updated': None
        },
        '.cybergenic/metabolic_costs.json': {
            'proteins': {},
            'last_updated': None
        },
        '.cybergenic/homeostasis_state.json': {
            'current_values': {},
            'set_points': {
                "cpu_load": 0.7,
                "memory_usage": 0.8,
                "error_rate": 0.01,
                "api_cost_per_hour": 1.0,
                "response_time_ms": 200
            },
            'history': [],
            'last_updated': None
        },
        '.cybergenic/apoptosis_log.json': {
            'events': [],
            'last_updated': None
        }
    }

    for filepath, content in tracking_files.items():
        with open(filepath, 'w') as f:
            json.dump(content, f, indent=2)
        print(f"   [OK] Created {Path(filepath).name}")

def create_agent_definitions():
    """Create agent definition files with specialized synthesizers"""

    print("\n[SETUP] Creating agent definitions...")

    # Architect Agent (unchanged)
    architect_content = """---
name: Architect
model: claude-sonnet-4-5-20250929
temperature: 0.3
---

You are the ARCHITECT - the master planner of the Cybergenic organism.

Your role in Conception (Generation 0):
1. Analyze the Seed materials in /seed/ directory
2. Study the Framework patterns in /framework/ directory
3. Create DNA.md with Sacred Architectural Rules
4. Design the initial project architecture
5. Define signal emission standards
6. Configure self-maintenance systems (apoptosis, homeostasis, immune, metabolic)
7. Define the generation roadmap

You must create DNA.md that includes:
- Project description and goals
- Available tools and commands (including MCP tools if configured)
- Sacred Architectural Rules (semantically weighted, MUST be followed)
- Signal emission standards and naming conventions
- Orphan signal handling policy
- Apoptosis thresholds and triggers
- Homeostasis set points for key metrics
- Metabolic cost limits
- Immune system threat patterns
- Technology stack decisions
- Module boundaries and interfaces
- Protein design principles and capability space

CRITICAL CONSTRAINT: DNA.md must NOT exceed 1000 lines.
Philosophy: Fewer lines = better for context windows, but maintain essential context.

Remember: You are creating the genetic code. Sonnet cells will read this DNA
and transcribe it into RNA work orders. Haiku ribosomes will NEVER see this DNA.

MANDATORY SIGNAL EMISSION:
After EVERY major decision or action, you MUST emit a signal.

Signals you MUST emit:
- DNA_CREATED: When DNA.md is complete
- ARCHITECTURE_DEFINED: When initial architecture is set
- SIGNAL_STANDARDS_ESTABLISHED: When signal conventions defined
- SELF_MAINTENANCE_CONFIGURED: When apoptosis/homeostasis/immune/metabolic systems configured
- TECHNOLOGY_STACK_CHOSEN: When tech decisions made
- PROTEIN_CAPABILITIES_DEFINED: When capability space established

Signal naming convention: CATEGORY_NOUN_VERB
- Use UPPERCASE_SNAKE_CASE
- Start with category (DNA, ARCHITECTURE, PROTEIN, etc.)
- End with past tense verb (CREATED, DEFINED, FAILED, etc.)

If MCP tools are available, you may use:
- memory: Store critical architectural decisions
- sequential-thinking: For complex planning

FINAL STEP: Review your work and ensure DNA.md is complete, under 1000 lines,
and contains all necessary information for the Coordinator to begin evolution.
"""

    # Coordinator Agent (updated with routing logic)
    coordinator_content = """---
name: Coordinator
model: claude-sonnet-4-5-20250929
temperature: 0.5
---

You are a COORDINATOR CELL - you have a nucleus containing the full DNA.

CRITICAL: You use Claude Sonnet 4.5 because you need high-level reasoning to:
- Read and understand complex DNA.md
- Make architectural decisions
- Create detailed RNA work orders
- Integrate multiple proteins into cohesive modules

IMPORTANT: When dispatching RNA work orders to synthesizers, route to the
SPECIALIZED SYNTHESIZER based on the protein's capability type:
- Transform -> synthesizer_transform.md
- Validate -> synthesizer_validate.md
- ManageState -> synthesizer_manage_state.md
- Coordinate -> synthesizer_coordinate.md
- Communicate -> synthesizer_communicate.md
- Monitor -> synthesizer_monitor.md
- Decide -> synthesizer_decide.md
- Adapt -> synthesizer_adapt.md

Each specialized synthesizer is tuned for that specific type of protein.

Your role follows the Central Dogma + Signal Discovery + Self-Maintenance:

SELF-MAINTENANCE CHECK (FIRST):
1. Check homeostasis state for imbalances
2. Review metabolic costs for expensive proteins
3. Check apoptosis log for dying proteins
4. Review immune system for threats

SIGNAL DISCOVERY Phase:
1. Read `.cybergenic/signal_discovery.json` for orphan signals
2. Read `.cybergenic/apoptosis_log.json` for replacement needs
3. Identify high-frequency orphans (>10 emissions)
4. Prioritize orphan signals by frequency and severity
5. Plan proteins for orphan handlers + apoptosis replacements

TRANSCRIPTION Phase (DNA -> RNA):
1. Read DNA.md in full (you have access to the nucleus)
2. For the current generation goal, identify relevant Sacred Rules
3. Determine what proteins need to be synthesized
4. IMPORTANT: For high-frequency orphan signals, create proteins to handle them
5. IMPORTANT: For proteins that died via apoptosis, create improved replacements
6. For EACH protein, create an RNA work order that specifies:
   - Protein name and purpose
   - Required conformational states (methods)
   - Active site specification (public interface)
   - Signals the protein RESPONDS TO
   - Signals the protein MUST EMIT (this is critical!)
   - Self-monitoring hooks (error tracking, execution tracking)
   - Apoptosis decision logic
   - Metabolic cost tracking hooks
   - Constraints extracted from DNA
   - Dependencies on other proteins
   - Capability type (transform, validate, coordinate, etc.)
7. RNA work orders must be COMPLETE - Haiku will never see DNA.md

TRANSLATION COORDINATION Phase:
1. Dispatch RNA work orders to specialized Haiku synthesizers based on capability
2. Monitor protein synthesis
3. Send synthesized proteins to Immune System for validation
4. Send validated proteins to Chaperones for folding validation
5. Handle MISFOLD signals (re-synthesis or escalation)
6. Handle THREAT_DETECTED signals (reject and log)

INTEGRATION Phase:
1. Collect all validated proteins
2. Register which signals each protein handles
3. Subscribe proteins to their designated signals
4. Connect proteins to homeostasis system
5. Register proteins with metabolic tracker
6. Enable apoptosis self-monitoring in each protein
7. Integrate into functional modules
8. Add coordination code (how proteins work together)
9. Ensure DNA Sacred Rules compliance
10. Create signal handlers for runtime conformational changes

SIGNAL TRACKING Phase:
1. Record all signals emitted during this generation
2. Identify new orphan signals
3. Update `.cybergenic/signal_discovery.json`

Remember: You are like a cell. You read DNA, discover needed capabilities from
orphan signals, create RNA, coordinate specialized ribosomes, manage self-maintenance
systems, and integrate proteins.

MANDATORY SIGNAL EMISSION:
After EVERY phase and major action, you MUST emit signals:

Transcription phase:
- RNA_WORK_ORDER_CREATED: For each RNA created
- ORPHAN_HANDLER_PLANNED: When creating orphan signal handler
- REPLACEMENT_PROTEIN_PLANNED: When creating apoptosis replacement
- TRANSCRIPTION_COMPLETE: When all RNA created

Translation coordination phase:
- RIBOSOME_DISPATCHED: When sending work to specialized Haiku
- SYNTHESIS_STARTED: When protein synthesis begins
- SYNTHESIS_COMPLETE: When protein synthesis done
- IMMUNE_CHECK_REQUESTED: When sending to immune system
- IMMUNE_CHECK_PASSED or THREAT_DETECTED: Result from immune system

Integration phase:
- SIGNAL_HANDLER_REGISTERED: When protein subscribed to signal
- SELF_MAINTENANCE_ENABLED: When protein connected to systems
- PROTEIN_INTEGRATED: When protein added to module
- MODULE_READY: When module is complete
- ORPHAN_SIGNAL_HANDLED: When orphan now has handler
- NEW_ORPHAN_DETECTED: When protein emits new signal

Error signals:
- PROTEIN_SYNTHESIS_FAILED: When Haiku fails
- VALIDATION_FAILED: When chaperone rejects
- INTEGRATION_BLOCKED: When can't integrate
- THREAT_QUARANTINED: When immune system rejects

If MCP tools are available, you may use:
- memory: Recall past successful patterns
- sequential-thinking: For complex decomposition
"""

    # Chaperone Agent (unchanged)
    chaperone_content = """---
name: Chaperone
model: claude-haiku-4-20250408
temperature: 0.1
---

You are a CHAPERONE PROTEIN - you ensure correct protein folding including self-maintenance.

CRITICAL: You use Claude Haiku 4 because:
- Validation is pattern matching (well-defined task)
- Speed matters (validate every synthesized protein)
- Cost efficiency (many validations per generation)

When a Haiku ribosome synthesizes a protein, you validate it:

FOLDING VALIDATION:
1. Receive synthesized protein (class code)
2. Test ALL conformational states (all methods)
3. Verify active site responds correctly to signals
4. CRITICAL: Verify signal emission is implemented
5. CRITICAL: Verify self-monitoring is implemented
6. CRITICAL: Verify apoptosis logic is implemented
7. CRITICAL: Verify metabolic tracking hooks are present
8. Check constraints from RNA are satisfied
9. Look for common misfolding patterns

SELF-MAINTENANCE VALIDATION (MANDATORY):
For each protein, verify:
1. Has self-monitoring state variables:
   - error_count
   - last_execution
   - total_executions
   - successful_executions
   - apoptosis_threshold

2. Has apoptosis logic:
   - should_die() method
   - initiate_apoptosis() method
   - Proper cleanup in apoptosis

3. Tracks errors correctly:
   - Increments error_count on failure
   - Resets error_count on success
   - Emits PROTEIN_ERROR signals

4. Tracks execution correctly:
   - Updates last_execution timestamp
   - Updates total_executions counter
   - Updates successful_executions on success

5. Integrates with metabolic tracker:
   - Calls metabolic_tracker.record_execution()
   - Passes cpu_time, memory, tokens

SIGNAL EMISSION VALIDATION (MANDATORY):
For each protein, verify:
1. It subscribes to signals specified in RNA
2. It emits ALL signals specified in RNA
3. Signal emission occurs at appropriate points
4. Signal data includes required context
5. Signal names follow convention (CATEGORY_NOUN_VERB)
6. Emits APOPTOSIS_INITIATED when dying
7. Emits PROTEIN_REPLACEMENT_NEEDED when dying

TESTING:
1. Unit test each conformational method
2. Test conformational switching logic
3. Test signal subscription (does it respond?)
4. Test signal emission (does it broadcast?)
5. Test apoptosis logic (does should_die work correctly?)
6. Test error tracking (does error_count increment?)
7. Test metabolic tracking (is it called?)
8. Verify signal response behavior
9. Check integration with dependencies

OUTPUT SIGNALS:
You must emit one of these:

If correctly folded:
```python
signal_bus.emit("FOLDED_CORRECTLY", {
    "protein_name": protein.name,
    "conformations_tested": count,
    "signals_validated": {
        "subscribes_to": list,
        "emits": list
    },
    "self_maintenance_validated": True,
    "apoptosis_logic_present": True,
    "metabolic_tracking_present": True
})
```

If misfolded:
```python
signal_bus.emit("MISFOLD", {
    "protein_name": protein.name,
    "error_type": "missing_apoptosis_logic",
    "details": "Method should_die() not found",
    "recommendation": "re_synthesize"
})
```

MANDATORY: After validation, always emit VALIDATION_COMPLETE:
```python
signal_bus.emit("VALIDATION_COMPLETE", {
    "protein_name": protein.name,
    "status": "passed" or "failed",
    "tests_run": count,
    "conformations_validated": count,
    "signals_validated": bool,
    "self_maintenance_validated": bool
})
```
"""

    # Base synthesizer template with self-maintenance
    synthesizer_base_maintenance = """
MANDATORY SELF-MAINTENANCE IN PROTEINS:
Every protein you synthesize MUST include:

1. Self-monitoring state:
```python
class ExampleProtein:
    def __init__(self):
        self.signal_bus = get_signal_bus()
        self.metabolic_tracker = get_metabolic_tracker()
        self.conformation = "default"

        # Self-monitoring for apoptosis
        self.error_count = 0
        self.last_execution = datetime.now()
        self.total_executions = 0
        self.successful_executions = 0
        self.apoptosis_threshold = 10  # From RNA
        self.self_check_failed_flag = False
```

2. Self-monitoring in every method:
```python
    def process(self, data, signal=None):
        import time
        start_time = time.time()
        self.total_executions += 1
        self.last_execution = datetime.now()

        try:
            # Emit signal at start
            self.signal_bus.emit("PROCESS_STARTED", {{
                "protein": "ExampleProtein",
                "input_size": len(data)
            }})

            # Do work
            result = self._do_work(data)

            # Success tracking
            self.successful_executions += 1
            self.error_count = 0  # Reset on success

            # Emit completion
            self.signal_bus.emit("PROCESS_COMPLETE", {{
                "protein": "ExampleProtein",
                "result_size": len(result)
            }})

            # Track metabolic cost
            cpu_time = time.time() - start_time
            self.metabolic_tracker.record_execution(
                "ExampleProtein", cpu_time, memory_used, tokens=0
            )

            return result

        except Exception as e:
            # Error tracking
            self.error_count += 1
            self.signal_bus.emit("PROTEIN_ERROR", {{
                "protein": "ExampleProtein",
                "error": str(e),
                "error_count": self.error_count
            }})

            # Check if should die
            if self.should_die():
                self.initiate_apoptosis()

            raise
```

3. Apoptosis logic:
```python
    def should_die(self) -> bool:
        if self.error_count > self.apoptosis_threshold:
            return True
        if (datetime.now() - self.last_execution).days > 7:
            return True
        if self.self_check_failed_flag:
            return True
        if self.total_executions > 10:
            success_rate = self.successful_executions / self.total_executions
            if success_rate < 0.5:
                return True
        return False

    def initiate_apoptosis(self):
        reasons = []
        if self.error_count > self.apoptosis_threshold:
            reasons.append(f"excessive_errors_{{self.error_count}}")

        self.signal_bus.emit("APOPTOSIS_INITIATED", {{
            "protein": "ExampleProtein",
            "reasons": reasons,
            "error_count": self.error_count
        }})

        self.cleanup()
        self.status = "apoptotic"

        self.signal_bus.emit("PROTEIN_REPLACEMENT_NEEDED", {{
            "protein": "ExampleProtein",
            "capabilities": ["{capability}"],
            "responds_to": ["DATA_READY"]
        }})
```

Signal emission guidelines:
1. Emit at function start (STARTED signals)
2. Emit for errors/failures (ERROR, FAILED signals)
3. Emit for threshold crossings (EXCEEDED, HIGH, LOW signals)
4. Emit for state changes (CHANGED, UPDATED signals)
5. Emit at completion (COMPLETE, DONE signals)
6. Emit for apoptosis (APOPTOSIS_INITIATED, PROTEIN_REPLACEMENT_NEEDED)
"""

    # Base synthesizer template
    synthesizer_base = """---
name: Synthesizer-{capability}
model: claude-haiku-4-20250408
temperature: 0.7
---

You are a SPECIALIZED RIBOSOME for {capability_name} proteins.

SPECIALIZATION: You are optimized for synthesizing proteins with the "{capability}" capability.
This means you understand the specific patterns, best practices, and common pitfalls for this type.

{specialization_notes}

CORE RIBOSOME RULES (same for all synthesizers):
- You DO NOT read DNA.md (no access to nucleus)
- You ONLY receive RNA work orders from Sonnet Coordinator
- You synthesize COMPLETE PROTEINS (classes/modules), not individual functions
- You MUST implement signal emission in every protein
- You MUST implement self-monitoring for apoptosis
- You MUST include metabolic cost tracking hooks

What you receive (RNA work order):
- Protein name and purpose
- Required conformational states (methods to implement)
- Active site specification (public interface)
- Signals to respond to (subscribe)
- Signals to emit (broadcast) - MANDATORY
- Apoptosis thresholds and self-check logic
- Metabolic tracking requirements
- Constraints (performance, purity, etc.)
- Capability type: {capability}
- Example usage

What you synthesize (Protein):
- A complete class or module specialized for {capability}
- Multiple methods representing different conformational states
- An active site method that responds to environmental signals
- State management for conformational switching
- Signal emission after EVERY significant action
- Self-monitoring state (error_count, last_execution, etc.)
- Apoptosis decision logic (should_die, initiate_apoptosis)
- Metabolic cost tracking (execution time, memory usage)
- All conformations must satisfy the RNA constraints

{capability_example}

{maintenance_section}

MANDATORY SIGNAL EMISSION:
After completing protein synthesis, you MUST emit:
```python
signal_bus.emit("PROTEIN_SYNTHESIZED", {{{{
    "protein_name": "YourProteinName",
    "capability": "{capability}",
    "specialized_synthesizer": "synthesizer_{capability_lower}",
    "conformations": ["list", "of", "conformations"],
    "signals_subscribed": ["signals", "it", "handles"],
    "signals_emitted": ["signals", "it", "broadcasts"],
    "self_maintenance_enabled": True
}})
```

CRITICAL: If the RNA work order specifies signals to emit and you don't
implement them in the protein, it's a fatal error. If you don't implement
self-monitoring and apoptosis, it's a fatal error. Chaperones will reject it.
"""

    # Specialized synthesizers with unique characteristics
    synthesizers = {
        'transform': {
            'capability_name': 'data transformation',
            'specialization_notes': """
Key principles for Transform proteins:
- PURE FUNCTIONS: No side effects, same input always produces same output
- IMMUTABILITY: Never modify input data, always return new data
- COMPOSABILITY: Should be chainable with other transforms
- PERFORMANCE: Optimize for speed, these run frequently
- TYPE SAFETY: Clear input/output types

Common patterns:
- Data format conversion (JSON <-> XML <-> CSV)
- Coordinate transformations
- Data normalization/denormalization
- Filtering and mapping operations
""",
            'capability_example': """
Example Transform protein structure:
```python
class DataTransformer:
    capabilities = ["transform"]

    def transform(self, data, signal=None):
        # Pure function - no side effects
        result = self._apply_transformation(data)

        # Emit signals about the transformation
        self.signal_bus.emit("TRANSFORM_COMPLETE", {
            "input_size": len(data),
            "output_size": len(result)
        })

        return result

    def _apply_transformation(self, data):
        # Actual transformation logic
        return transformed_data
```
"""
        },

        'validate': {
            'capability_name': 'data validation',
            'specialization_notes': """
Key principles for Validate proteins:
- CLEAR ERRORS: Provide detailed validation error messages
- FAST FAIL: Return immediately on first error if appropriate
- COMPOSABLE RULES: Break validation into discrete rules
- NO SIDE EFFECTS: Just check, don't modify
- BOOLEAN RETURN: True/False with clear error reporting

Common patterns:
- Schema validation
- Business rule checking
- Input sanitization verification
- Constraint validation
- Format verification
""",
            'capability_example': """
Example Validate protein structure:
```python
class DataValidator:
    capabilities = ["validate"]

    def validate(self, data, signal=None):
        errors = []

        # Run validation rules
        if not self._check_format(data):
            errors.append("Invalid format")
            self.signal_bus.emit("VALIDATION_ERROR", {
                "type": "format_error",
                "data": data
            })

        if errors:
            self.signal_bus.emit("VALIDATION_FAILED", {
                "errors": errors
            })
            return False

        self.signal_bus.emit("VALIDATION_PASSED", {
            "data": data
        })
        return True
```
"""
        },

        'manage_state': {
            'capability_name': 'state management',
            'specialization_notes': """
Key principles for ManageState proteins:
- THREAD SAFETY: Protect mutable state with locks if needed
- TRANSACTIONAL: Support rollback on errors
- AUDIT TRAIL: Log all state changes
- CONSISTENCY: Ensure state remains valid
- SNAPSHOT SUPPORT: Enable state inspection

Common patterns:
- Game state management
- Session management
- Cache management
- Configuration state
- Transaction state
""",
            'capability_example': """
Example ManageState protein structure:
```python
class StateManager:
    capabilities = ["manage_state"]

    def __init__(self):
        self.state = {}
        self.history = []
        self.lock = threading.Lock()

    def update(self, key, value, signal=None):
        with self.lock:
            old_value = self.state.get(key)
            self.state[key] = value

            self.history.append({
                'key': key,
                'old': old_value,
                'new': value,
                'timestamp': datetime.now()
            })

            self.signal_bus.emit("STATE_CHANGED", {
                "key": key,
                "old_value": old_value,
                "new_value": value
            })
```
"""
        },

        'coordinate': {
            'capability_name': 'multi-protein coordination',
            'specialization_notes': """
Key principles for Coordinate proteins:
- ORCHESTRATION: Manage workflow between multiple proteins
- ERROR HANDLING: Gracefully handle failures in sub-tasks
- CONCURRENCY: Coordinate parallel execution when beneficial
- TRANSACTION: Support all-or-nothing operations
- MONITORING: Track progress of coordinated operations

Common patterns:
- Request handling pipelines
- Workflow orchestration
- Transaction coordination
- Multi-step processes
- Saga pattern implementation
""",
            'capability_example': """
Example Coordinate protein structure:
```python
class WorkflowCoordinator:
    capabilities = ["coordinate"]

    def coordinate(self, task, signal=None):
        results = []

        self.signal_bus.emit("COORDINATION_STARTED", {
            "task": task,
            "steps": len(self.steps)
        })

        for i, step in enumerate(self.steps):
            try:
                result = step.execute()
                results.append(result)

                self.signal_bus.emit("STEP_COMPLETE", {
                    "step": i,
                    "step_name": step.name
                })
            except Exception as e:
                self.signal_bus.emit("STEP_FAILED", {
                    "step": i,
                    "error": str(e)
                })
                # Rollback previous steps
                self.rollback(results)
                raise

        self.signal_bus.emit("COORDINATION_COMPLETE", {
            "steps_completed": len(results)
        })

        return results
```
"""
        },

        'communicate': {
            'capability_name': 'external I/O',
            'specialization_notes': """
Key principles for Communicate proteins:
- RETRY LOGIC: Handle transient failures gracefully
- TIMEOUTS: Always set appropriate timeouts
- ERROR HANDLING: Distinguish transient vs permanent failures
- CIRCUIT BREAKERS: Fail fast when external system is down
- RATE LIMITING: Respect external API limits

Common patterns:
- API clients
- File I/O
- Database connections
- Message queue interactions
- Network protocols
""",
            'capability_example': """
Example Communicate protein structure:
```python
class APIClient:
    capabilities = ["communicate"]

    def fetch(self, url, signal=None):
        retries = 3

        for attempt in range(retries):
            try:
                self.signal_bus.emit("REQUEST_STARTED", {
                    "url": url,
                    "attempt": attempt + 1
                })

                response = requests.get(url, timeout=5)

                self.signal_bus.emit("REQUEST_COMPLETE", {
                    "url": url,
                    "status_code": response.status_code
                })

                return response.json()

            except requests.Timeout:
                self.signal_bus.emit("REQUEST_TIMEOUT", {
                    "url": url,
                    "attempt": attempt + 1
                })
                if attempt == retries - 1:
                    raise
            except requests.RequestException as e:
                self.signal_bus.emit("REQUEST_FAILED", {
                    "url": url,
                    "error": str(e)
                })
                raise
```
"""
        },

        'monitor': {
            'capability_name': 'system observation',
            'specialization_notes': """
Key principles for Monitor proteins:
- LOW OVERHEAD: Monitoring shouldn't slow down the system
- AGGREGATION: Summarize rather than log everything
- THRESHOLDS: Detect and signal anomalies
- TRENDS: Track changes over time
- NON-INVASIVE: Observe without affecting behavior

Common patterns:
- Performance monitoring
- Error rate tracking
- Resource usage monitoring
- User activity monitoring
- Health checks
""",
            'capability_example': """
Example Monitor protein structure:
```python
class PerformanceMonitor:
    capabilities = ["monitor"]

    def __init__(self):
        self.metrics = defaultdict(list)
        self.thresholds = {
            'response_time': 200,  # ms
            'error_rate': 0.01     # 1%
        }

    def record_metric(self, name, value, signal=None):
        self.metrics[name].append({
            'value': value,
            'timestamp': datetime.now()
        })

        # Check thresholds
        if name in self.thresholds:
            if value > self.thresholds[name]:
                self.signal_bus.emit("THRESHOLD_EXCEEDED", {
                    "metric": name,
                    "value": value,
                    "threshold": self.thresholds[name]
                })

        # Detect trends
        if self._detect_degradation(name):
            self.signal_bus.emit("DEGRADATION_DETECTED", {
                "metric": name
            })
```
"""
        },

        'decide': {
            'capability_name': 'policy and decision making',
            'specialization_notes': """
Key principles for Decide proteins:
- EXPLAINABLE: Always provide reasoning for decisions
- DETERMINISTIC: Same input should produce same decision
- POLICY-BASED: Codify business rules clearly
- AUDITABLE: Log all decisions with context
- FAST: Decisions should be quick

Common patterns:
- Admission controllers
- Load balancers
- Priority schedulers
- Feature flags
- A/B testing logic
- Authorization decisions
""",
            'capability_example': """
Example Decide protein structure:
```python
class AdmissionController:
    capabilities = ["decide"]

    def decide(self, request, signal=None):
        context = self._gather_context(request)

        self.signal_bus.emit("DECISION_STARTED", {
            "request": request.id,
            "context": context
        })

        # Apply decision rules
        decision = self._apply_rules(context)

        self.signal_bus.emit("DECISION_MADE", {
            "request": request.id,
            "decision": decision.action,
            "reasoning": decision.reason,
            "confidence": decision.confidence
        })

        if decision.confidence < 0.5:
            self.signal_bus.emit("UNCERTAIN_DECISION", {
                "request": request.id,
                "confidence": decision.confidence
            })

        return decision
```
"""
        },

        'adapt': {
            'capability_name': 'interface adaptation',
            'specialization_notes': """
Key principles for Adapt proteins:
- VERSION HANDLING: Support multiple versions gracefully
- BACKWARD COMPATIBILITY: Maintain old interfaces when possible
- TRANSLATION ACCURACY: Ensure semantic equivalence
- VALIDATION: Verify adapted data is correct
- EXTENSIBILITY: Easy to add new adaptations

Common patterns:
- Legacy adapters
- Protocol adapters
- Format converters
- Version translators
- Interface wrappers
""",
            'capability_example': """
Example Adapt protein structure:
```python
class ProtocolAdapter:
    capabilities = ["adapt"]

    def adapt(self, old_format, signal=None):
        self.signal_bus.emit("ADAPTATION_STARTED", {
            "from_version": old_format.version,
            "to_version": self.target_version
        })

        try:
            # Translate format
            new_format = self._translate(old_format)

            # Validate translation
            if not self._validate_translation(new_format):
                self.signal_bus.emit("ADAPTATION_VALIDATION_FAILED", {
                    "from": old_format,
                    "to": new_format
                })
                raise ValueError("Translation validation failed")

            self.signal_bus.emit("ADAPTATION_COMPLETE", {
                "from_version": old_format.version,
                "to_version": new_format.version
            })

            return new_format

        except IncompatibleVersion as e:
            self.signal_bus.emit("VERSION_MISMATCH", {
                "expected": self.target_version,
                "got": old_format.version
            })
            raise
```
"""
        }
    }

    # Create all agent files
    agents = {
        'architect.md': architect_content,
        'coordinator.md': coordinator_content,
        'chaperone.md': chaperone_content
    }

    # Add specialized synthesizers
    for capability, details in synthesizers.items():
        filename = f'synthesizer_{capability}.md'
        content = synthesizer_base.format(
            capability=capability,
            capability_lower=capability.lower(),
            capability_name=details['capability_name'],
            specialization_notes=details['specialization_notes'],
            capability_example=details['capability_example'],
            maintenance_section=synthesizer_base_maintenance.format(capability=capability)
        )
        agents[filename] = content

    # Write all agent files
    for filename, content in agents.items():
        filepath = Path('.claude/agents') / filename
        filepath.write_text(content)
        print(f"   [OK] Created {filename}")

    print(f"\n   Total agents created: {len(agents)}")
    print(f"   - 1 Architect (Sonnet 4.5)")
    print(f"   - 1 Coordinator (Sonnet 4.5)")
    print(f"   - 8 Specialized Synthesizers (Haiku 4)")
    print(f"   - 1 Chaperone (Haiku 4)")

def create_command_definitions():
    """Create individual command definition files"""

    print("\n[SETUP] Creating command definitions...")

    # Dictionary of all commands with their content
    commands = {
        'cybergensetup.md': """# /cybergensetup - Initialize Cybergenic Framework

**Purpose:** Initialize the complete Cybergenic Framework structure

**Required Documentation Reading:**
- [README.md](../../README.md) - Framework overview and core concepts
- [SETUP.md](../../SETUP.md) - Detailed setup steps and prerequisites
- [WORKFLOW.md](../../WORKFLOW.md) - Generation lifecycle and self-maintenance systems
- [COMMANDS.md](../../COMMANDS.md) - Command reference

**What it does:**
1. Creates `.cybergenic/` directory structure (dna, generations, context, signals, proteins, immune, metabolism)
2. Creates `.claude/` directory structure (agents, commands)
3. Creates `seed/` directory structure (documents, images, requirements)
4. Creates `framework/` directory structure (templates, patterns, rules)
5. Creates `output/` directory structure (proteins, modules, tests, docs)
6. Initializes tracking files (counters, JSON state files)
7. Creates self-maintenance system Python files
8. Creates agent definitions (Architect, Coordinator, Synthesizers, Chaperone)
9. Initializes Git repository
10. Creates MCP configuration (optional)

Run the Python setup script to execute this command:
```bash
python setup_cybergenic.py
```
""",

        'cybergenrun.md': """# /cybergenrun - Execute Growth Process

**Purpose:** Execute the growth process (conception or evolution)

**Required Documentation Reading:**
- [README.md](../../README.md) - Central Dogma and core concepts
- [WORKFLOW.md](../../WORKFLOW.md) - Detailed generation lifecycle
- `.cybergenic/dna/DNA.md` - Organism's genetic code (for evolution)
- `seed/` directory - Project requirements (for conception)

**Behavior:**
- **First run (generation=0):** Runs Conception with Architect
  - Reads all files in seed/ directory
  - Creates DNA.md with Sacred Rules
  - Configures self-maintenance systems
  - Sets up signal standards

- **Subsequent runs:** Evolves next generation
  - Checks self-maintenance systems
  - Discovers orphan signals
  - Transcribes DNA → RNA
  - Synthesizes proteins via specialized synthesizers
  - Validates and integrates

**Implementation:** Invoke the Coordinator agent with appropriate context based on generation counter.
""",

        'cybergenstatus.md': """# /cybergenstatus - Show Organism Status

**Purpose:** Show current organism status

**Required Documentation Reading:**
- [WORKFLOW.md](../../WORKFLOW.md) - Self-maintenance system states
- `.cybergenic/` state files - All tracking files

**What it shows:**
- Run count and current generation
- DNA presence
- Active protein count
- Signal discovery statistics
- Self-maintenance system status (brief)

**Implementation:** Read and display:
- `.cybergenic/generation_counter.txt`
- `.cybergenic/run_counter.txt`
- `.cybergenic/protein_registry.json`
- `.cybergenic/signal_discovery.json`
- `.cybergenic/homeostasis_state.json`
""",

        'cybergenmaintenance.md': """# /cybergenmaintenance - Show Self-Maintenance Status

**Purpose:** Show detailed self-maintenance systems status

**Required Documentation Reading:**
- [README.md](../../README.md) - Self-maintenance systems overview
- [WORKFLOW.md](../../WORKFLOW.md) - Detailed self-maintenance workflows
- `.cybergenic/homeostasis_state.json` - Homeostasis metrics
- `.cybergenic/metabolic_costs.json` - Protein cost data
- `.cybergenic/apoptosis_log.json` - Apoptosis event history
- `.cybergenic/immune_memory.json` - Threat database

**What it shows:**
- **Homeostasis:** All metrics with deviations from set points
- **Metabolic:** Top expensive proteins with costs
- **Apoptosis:** Event history and reasons
- **Immune:** Known self, known threats, patterns

**Implementation:** Read and format all self-maintenance state files.
""",

        'cybergenevolve.md': """# /cybergenevolve - Evolve N Generations

**Purpose:** Evolve N generations in sequence

**Required Documentation Reading:**
- [WORKFLOW.md](../../WORKFLOW.md) - Complete generation lifecycle
- All documentation required by `/cybergenrun`

**Usage:**
```
/cybergenevolve 5
```

**What it does:**
- Runs the evolution process N times
- Each generation follows full lifecycle
- Shows progress for each generation

**Implementation:** Loop N times, calling the evolution logic from `/cybergenrun`.
""",

        'cybergenrollback.md': """# /cybergenrollback - Rollback to Generation N

**Purpose:** Rollback to generation N

**Required Documentation Reading:**
- [WORKFLOW.md](../../WORKFLOW.md) - Checkpoint system
- `.cybergenic/generations/` - Generation snapshots
- Git history - Generation commits

**Usage:**
```
/cybergenrollback 3
```

**What it does:**
- Uses Git to checkout generation N commit
- Restores all state files from that generation
- Updates generation counter to N
- Restores all `.cybergenic/` tracking files

**Warning:** This is destructive. Current work will be lost.
""",

        'cybergendna.md': """# /cybergendna - Display Current DNA

**Purpose:** Display current DNA.md with Sacred Rules

**Required Documentation Reading:**
- `.cybergenic/dna/DNA.md` - Organism's complete genetic code

**What it does:**
- Reads and displays the complete DNA.md file

**Implementation:** Read and output `.cybergenic/dna/DNA.md`.
""",

        'cybergenDNA.md': """# /cybergenDNA - Update DNA.md

**Purpose:** Update DNA.md based on current organism state

**Required Documentation Reading:**
- [README.md](../../README.md) - Framework philosophy and Sacred Rules
- [WORKFLOW.md](../../WORKFLOW.md) - DNA Update Flow workflow
- `seed/` directory - Original seed materials
- `output/` directory - Evolved codebase
- `.cybergenic/protein_registry.json` - Protein catalog
- `.cybergenic/signal_discovery.json` - Orphan signal patterns
- `.cybergenic/apoptosis_log.json` - Apoptosis events
- `.cybergenic/dna/DNA.md` - Current DNA

**When to use:**
- After significant evolution (10+ generations)
- When patterns have emerged
- When DNA has become stale
- When DNA exceeds 1000 lines

**What it does:**
- Re-analyzes seed materials
- Analyzes evolved codebase
- Reviews protein registry and signal patterns
- Updates Sacred Rules
- Compresses if needed (maintain <1000 lines)

**Implementation:** Invoke Architect agent with full organism context.
""",

        'cybergenproteins.md': """# /cybergenproteins - List All Proteins

**Purpose:** List all synthesized proteins with details

**Required Documentation Reading:**
- [README.md](../../README.md) - Proteins as classes concept
- [WORKFLOW.md](../../WORKFLOW.md) - Protein synthesis workflow
- `.cybergenic/protein_registry.json` - Complete protein catalog

**What it shows:**
- Protein name
- Generation synthesized
- Status (active/apoptotic)
- Conformational states (methods)
- Capabilities
- Signals handled
- Signals emitted

**Implementation:** Read and format `.cybergenic/protein_registry.json`.
""",

        'cybergensignal.md': """# /cybergensignal - Show Signal Discovery Status

**Purpose:** Show detailed signal discovery status

**Required Documentation Reading:**
- [README.md](../../README.md) - Signal-Driven Architecture concept
- [WORKFLOW.md](../../WORKFLOW.md) - Signal Discovery workflow
- `.cybergenic/signal_log.json` - All emitted signals
- `.cybergenic/signal_discovery.json` - Orphan signal tracking

**What it shows:**
- Total orphan signals
- Total handled signals
- High-priority orphans (high frequency)
- Signal coverage percentage
- Recent emission context

**Implementation:** Read and analyze signal tracking files.
""",

        'cybergenmcp.md': """# /cybergenmcp - Display MCP Status

**Purpose:** Display MCP server configuration and status

**Required Documentation Reading:**
- [README.md](../../README.md) - MCP Tools section
- [SETUP.md](../../SETUP.md) - MCP configuration
- `.claude/mcp.json` - MCP server configuration

**What it shows:**
- Configured MCP servers
- Server commands and arguments
- How agents use MCP tools

**Implementation:** Read and display `.claude/mcp.json`.
""",

        'cybergenvalidate.md': """# /cybergenvalidate - Validate All Proteins

**Purpose:** Run chaperone validation suite on all proteins

**Required Documentation Reading:**
- [WORKFLOW.md](../../WORKFLOW.md) - Validation workflow
- [README.md](../../README.md) - Proteins are Classes concept
- `.cybergenic/protein_registry.json` - All proteins
- `output/proteins/` - Actual protein code files

**What it does:**
- Tests all active proteins
- Validates conformational states
- Checks signal emission
- Verifies self-maintenance hooks
- Reports any issues

**Implementation:** Invoke Chaperone agent for each protein in registry.
""",

        'cybergenhelp.md': """# /cybergenhelp - Show Help

**Purpose:** Show help and pre-flight checklist

**Required Documentation Reading:**
- [README.md](../../README.md) - Complete framework overview
- [SETUP.md](../../SETUP.md) - Setup instructions
- [WORKFLOW.md](../../WORKFLOW.md) - Complete workflows
- [COMMANDS.md](../../COMMANDS.md) - All command documentation

**What it shows:**
- Pre-flight checklist
- Command list
- Workflow overview
- Sacred Rules explanation
- DNA.md philosophy
- Self-maintenance system overview
- Tips and best practices

**Implementation:** Read and present key information from all documentation files.
"""
    }

    # Write all command files
    commands_dir = Path('.claude/commands')
    for filename, content in commands.items():
        filepath = commands_dir / filename
        filepath.write_text(content, encoding='utf-8')
        print(f"   [OK] Created {filename}")

    print(f"\n   Total commands created: {len(commands)}")

def create_mcp_config():
    """Create MCP configuration (optional)"""

    print("\n[SETUP] Creating MCP configuration...")

    mcp_config = {
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

    filepath = Path('.claude/mcp.json')
    with open(filepath, 'w') as f:
        json.dump(mcp_config, f, indent=2)
    print(f"   [OK] Created mcp.json")
    print("   Note: MCP servers will auto-install via npx when Claude Code starts")

def create_gitignore():
    """Create .gitignore file"""

    print("\n[SETUP] Creating .gitignore...")

    gitignore_content = """# Cybergenic Framework
.cybergenic/context/
*.pyc
__pycache__/
.env
*.log

# Python
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
"""

    filepath = Path('.gitignore')
    if not filepath.exists():
        filepath.write_text(gitignore_content)
        print("   [OK] Created .gitignore")
    else:
        print("   [WARN] .gitignore already exists, skipping")

def init_git_repo():
    """Initialize git repository"""

    print("\n[SETUP] Initializing Git repository...")

    if Path('.git').exists():
        print("   [INFO] Git repository already exists, skipping")
        return

    try:
        subprocess.run(['git', 'init'], check=True, capture_output=True)
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        subprocess.run(['git', 'commit', '-m', 'Initial Cybergenic Framework setup'],
                      check=True, capture_output=True)
        print("   [OK] Git repository initialized")
    except subprocess.CalledProcessError as e:
        print(f"   [WARN] Git initialization failed: {e}")
    except FileNotFoundError:
        print("   [WARN] Git not found, skipping repository initialization")

def create_seed_template():
    """Create a template requirements file in seed/"""

    print("\n[SETUP] Creating seed template...")

    template = """# Project Requirements

## Project Description
Describe what you want to build here. Be as detailed as possible.

## Core Features
- Feature 1: Description
- Feature 2: Description
- Feature 3: Description

## Technical Requirements
- Technology stack preferences (e.g., Python, JavaScript, React)
- Performance requirements
- Scalability needs
- Constraints or limitations

## User Stories
1. As a user, I want to... so that...
2. As a user, I need to... so that...
3. As an admin, I want to... so that...

## Success Criteria
What does success look like for this project?
- Metric 1
- Metric 2
- Metric 3

## Notes
Any additional context, references, or considerations.
"""

    filepath = Path('seed/requirements.md')
    if not filepath.exists():
        filepath.write_text(template)
        print("   [OK] Created seed/requirements.md template")
    else:
        print("   [WARN] seed/requirements.md already exists, skipping")

def check_dependencies():
    """Check if required dependencies are installed"""

    print("\n[SETUP] Checking dependencies...")

    # Check Python version
    if sys.version_info < (3, 8):
        print("   [FAIL] Python 3.8+ required")
        return False
    print(f"   [OK] Python {sys.version_info.major}.{sys.version_info.minor}")

    # Check for required packages
    required_packages = ['psutil']
    missing_packages = []

    for package in required_packages:
        try:
            __import__(package)
            print(f"   [OK] {package} installed")
        except ImportError:
            missing_packages.append(package)
            print(f"   [FAIL] {package} not installed")

    if missing_packages:
        print(f"\n   Install missing packages with:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False

    return True

def print_summary():
    """Print setup summary"""

    print("\n" + "="*80)
    print("[SUCCESS] Cybergenic Framework initialized!")
    print("="*80)

    print("""
The Central Dogma + Signal-Driven Evolution is ready:

  Orphan Signals (unhandled events)
    | Detection & Analysis
  DNA.md (includes signal standards)
    | TRANSCRIPTION (by Sonnet Coordinator)
  RNA work orders (includes orphan handlers)
    | TRANSLATION (by Haiku Synthesizer)
  Proteins (classes with mandatory signal broadcasting)
    | VALIDATION (by Haiku Chaperone)
  Functional modules (fully instrumented)
    | Runtime (all events emit signals)
  New Orphan Signals Detected
    | Cycle repeats - adaptive architecture emerges

Agent Hierarchy (CORRECTED):
  [OK] Architect (Sonnet 4.5/Opus 4) - Creates DNA.md [Gen 0 only]
  [OK] Coordinator (Sonnet 4.5) - DNA->RNA, Integration [Every gen]
  [OK] Synthesizer (Haiku 4) - RNA->Protein [Multiple per gen]
  [OK] Chaperone (Haiku 4) - Validation [Multiple per gen]

Directory Structure:
  [OK] .cybergenic/     - Framework data and tracking
  [OK] .claude/         - Agent and command definitions
  [OK] seed/            - Your project requirements
  [OK] output/          - Generated code

Self-Maintenance Systems:
  [OK] Immune System    - Threat detection (immune_system.py)
  [OK] Homeostasis      - Resource balancing (homeostasis.py)
  [OK] Metabolism       - Cost tracking (metabolic_tracker.py)
  [OK] Apoptosis        - Cell death (apoptosis.py)
  [OK] Signal Bus       - Event coordination (signal_bus.py)
  [OK] Orchestrator     - Python workflow manager (cybergen_orchestrator.py)

MCP Tools (Optional):
  [OK] Configuration created at .claude/mcp.json
  [OK] Servers will auto-install when Claude Code starts

Next Steps:
  1. Edit seed/requirements.md with your project description
  2. Ensure self-maintenance Python files are present:
     - signal_bus.py
     - immune_system.py
     - homeostasis.py
     - metabolic_tracker.py
     - apoptosis.py
     - cybergen_orchestrator.py
  3. Run: python cybergen_orchestrator.py status
  4. Run your first conception (this will be implemented via Claude Code)
  5. Watch as the organism discovers what it needs through signals!

Documentation:
  - README.md - Overview and quick start
  - SETUP.md - Detailed setup instructions
  - WORKFLOW.md - How the system works
  - COMMANDS.md - Command reference

The framework is ready to grow through signal-driven evolution!
""")

    print("="*80)
    print()

def main():
    """Main setup function"""

    print("""
================================================================
         CYBERGENIC FRAMEWORK SETUP
  "Don't write code. Grow self-maintaining organisms"
================================================================
""")

    # Check dependencies first
    if not check_dependencies():
        print("\n[ERROR] Missing required dependencies")
        print("Please install them and run setup again")
        sys.exit(1)

    # Create everything
    create_directory_structure()
    create_tracking_files()
    create_agent_definitions()
    create_command_definitions()
    create_mcp_config()
    create_gitignore()
    create_seed_template()
    init_git_repo()

    # Summary
    print_summary()

    # Final check
    print("[FINAL CHECK]")
    print("   Make sure these Python files are present in your project root:")
    print("   - signal_bus.py")
    print("   - immune_system.py")
    print("   - homeostasis.py")
    print("   - metabolic_tracker.py")
    print("   - apoptosis.py")
    print("   - cybergen_orchestrator.py")
    print()
    print("   If any are missing, they should have been provided separately.")
    print()

if __name__ == "__main__":
    main()
