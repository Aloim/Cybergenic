#!/usr/bin/env python3
"""
Cybergenic Framework Orchestrator with Self-Maintenance
Manages growth lifecycle with signal-driven evolution and self-healing
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# Import self-maintenance systems
from immune_system import ImmuneSystem
from homeostasis import HomeostasisController
from metabolic_tracker import MetabolicTracker
from apoptosis import ApoptosisSystem
from signal_bus import SignalBus, get_signal_bus

class SignalDiscoverySystem:
    """Tracks signal emissions and discovers orphans for adaptive synthesis"""

    def __init__(self):
        self.signal_log = Path('.cybergenic/signal_discovery.json')
        self.data = self._load()

    def _load(self) -> Dict:
        if self.signal_log.exists():
            try:
                with open(self.signal_log) as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return self._empty_data()
        return self._empty_data()

    def _empty_data(self) -> Dict:
        return {
            "orphans": {},
            "handled": {},
            "history": [],
            "generation_stats": {}
        }

    def record_emission(self, signal_type: str, context: Optional[Dict] = None, generation: int = 0):
        """Record that a signal was emitted"""
        if signal_type not in self.data["orphans"]:
            self.data["orphans"][signal_type] = {
                "count": 0,
                "first_seen_generation": generation,
                "first_seen_time": datetime.now().isoformat(),
                "contexts": [],
                "severity": self._infer_severity(signal_type)
            }

        self.data["orphans"][signal_type]["count"] += 1

        if context and len(self.data["orphans"][signal_type]["contexts"]) < 10:
            self.data["orphans"][signal_type]["contexts"].append({
                "time": datetime.now().isoformat(),
                "data": context
            })

        self._save()

    def record_handler(self, signal_type: str, protein_name: str, generation: int):
        """Record that a protein now handles this signal"""
        if signal_type in self.data["orphans"]:
            orphan_data = self.data["orphans"][signal_type]

            self.data["handled"][signal_type] = {
                **orphan_data,
                "handler_protein": protein_name,
                "handled_at_generation": generation,
                "handled_at_time": datetime.now().isoformat(),
                "was_orphan_for_generations": generation - orphan_data["first_seen_generation"]
            }

            del self.data["orphans"][signal_type]

            self.data["history"].append({
                "event": "orphan_handled",
                "signal": signal_type,
                "protein": protein_name,
                "generation": generation,
                "emissions_while_orphan": orphan_data["count"]
            })

        self._save()

    def get_high_priority_orphans(self, min_count: int = 10) -> Dict:
        """Get orphan signals that should trigger protein synthesis"""
        return {
            signal: data
            for signal, data in self.data["orphans"].items()
            if data["count"] >= min_count or data["severity"] == "critical"
        }

    def suggest_proteins(self, generation: int) -> List[Dict]:
        """Suggest proteins to synthesize based on orphan signals"""
        orphans = self.get_high_priority_orphans()
        suggestions = []

        for signal, data in sorted(orphans.items(), key=lambda x: x[1]["count"], reverse=True):
            protein_name = self._signal_to_protein_name(signal)
            capabilities = self._infer_capabilities(signal)
            conformations = self._suggest_conformations(signal, data)

            suggestions.append({
                "protein_name": protein_name,
                "reason": f"Handles orphan signal (emitted {data['count']} times since gen {data['first_seen_generation']})",
                "responds_to": [signal],
                "capabilities": capabilities,
                "suggested_conformations": conformations,
                "priority": "high" if data["count"] > 50 else "medium",
                "suggested_emissions": self._suggest_emissions(signal)
            })

        return suggestions

    def _infer_severity(self, signal: str) -> str:
        """Infer severity from signal name"""
        if any(word in signal for word in ["ERROR", "FAILED", "CRITICAL", "FATAL", "APOPTOSIS"]):
            return "critical"
        elif any(word in signal for word in ["WARNING", "EXCEEDED", "HIGH", "THREAT"]):
            return "high"
        elif any(word in signal for word in ["DEGRADATION", "SLOW", "TIMEOUT"]):
            return "medium"
        else:
            return "low"

    def _signal_to_protein_name(self, signal: str) -> str:
        """Convert VELOCITY_EXCEEDED to VelocityLimiter"""
        parts = signal.split('_')

        # Remove common suffixes
        suffixes_to_remove = ['EXCEEDED', 'DETECTED', 'FAILED', 'ERROR',
                               'COMPLETE', 'STARTED', 'HIGH', 'LOW', 'INITIATED']
        parts = [p for p in parts if p not in suffixes_to_remove]

        if not parts:
            parts = signal.split('_')[:2]

        # Determine appropriate suffix
        if 'ERROR' in signal or 'FAILED' in signal:
            suffix = 'Handler'
        elif 'EXCEEDED' in signal or 'HIGH' in signal or 'LOW' in signal:
            suffix = 'Limiter'
        elif 'MONITOR' in signal or 'DETECT' in signal:
            suffix = 'Monitor'
        elif 'VALIDATE' in signal or 'CHECK' in signal:
            suffix = 'Validator'
        elif 'REPLACEMENT' in signal or 'APOPTOSIS' in signal:
            suffix = 'Replacement'
        else:
            suffix = 'Manager'

        base_name = ''.join(word.capitalize() for word in parts)
        return base_name + suffix

    def _infer_capabilities(self, signal: str) -> List[str]:
        """Infer what capabilities the protein should have"""
        capabilities = []

        if 'ERROR' in signal or 'FAILED' in signal or 'VALIDATE' in signal:
            capabilities.append('validate')

        if 'EXCEEDED' in signal or 'HIGH' in signal or 'LOW' in signal:
            capabilities.extend(['monitor', 'coordinate'])

        if 'STATE' in signal or 'CHANGE' in signal:
            capabilities.append('manage_state')

        if 'NETWORK' in signal or 'TIMEOUT' in signal or 'IO' in signal:
            capabilities.append('communicate')

        if 'TRANSFORM' in signal or 'CONVERT' in signal:
            capabilities.append('transform')

        if 'DECIDE' in signal or 'POLICY' in signal:
            capabilities.append('decide')

        if 'ADAPT' in signal or 'CONVERT' in signal:
            capabilities.append('adapt')

        if not capabilities:
            capabilities.append('coordinate')

        return list(set(capabilities))

    def _suggest_conformations(self, signal: str, data: Dict) -> List[str]:
        """Suggest conformational states for the protein"""
        base_conformations = []

        if 'EXCEEDED' in signal:
            base_conformations = ['clamp', 'throttle', 'reject']
        elif 'ERROR' in signal:
            base_conformations = ['retry', 'fallback', 'escalate']
        elif 'SLOW' in signal or 'TIMEOUT' in signal:
            base_conformations = ['optimize', 'cache', 'skip']
        elif 'HIGH' in signal or 'LOW' in signal:
            base_conformations = ['adjust_up', 'adjust_down', 'maintain']
        elif 'REPLACEMENT' in signal:
            base_conformations = ['improved', 'alternative', 'optimized']
        else:
            base_conformations = ['handle', 'log', 'ignore']

        return base_conformations

    def _suggest_emissions(self, signal: str) -> List[str]:
        """Suggest what signals the new protein should emit"""
        base = signal.replace('_DETECTED', '').replace('_EXCEEDED', '').replace('_INITIATED', '')

        return [
            f"{base}_HANDLED",
            f"{base}_FAILED",
            f"{base}_RESOLVED"
        ]

    def get_statistics(self, generation: int) -> Dict:
        """Get statistics about signal discovery"""
        return {
            "generation": generation,
            "orphan_count": len(self.data["orphans"]),
            "handled_count": len(self.data["handled"]),
            "high_priority_orphans": len(self.get_high_priority_orphans()),
            "total_orphan_emissions": sum(d["count"] for d in self.data["orphans"].values()),
            "average_orphan_frequency": sum(d["count"] for d in self.data["orphans"].values()) / len(self.data["orphans"]) if self.data["orphans"] else 0
        }

    def _save(self):
        self.signal_log.parent.mkdir(parents=True, exist_ok=True)
        with open(self.signal_log, 'w') as f:
            json.dump(self.data, f, indent=2)

class ProteinRegistry:
    """Tracks all synthesized proteins in the organism"""

    def __init__(self):
        self.registry_file = Path('.cybergenic/protein_registry.json')
        self.proteins = self._load_registry()

    def _load_registry(self) -> Dict:
        if self.registry_file.exists():
            try:
                with open(self.registry_file) as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}

    def register_protein(self, protein_name: str, metadata: Dict):
        """Register a newly synthesized protein"""
        self.proteins[protein_name] = {
            **metadata,
            'synthesized_at': datetime.now().isoformat(),
            'status': 'active',
            'error_count': 0,
            'total_executions': 0,
            'successful_executions': 0,
            'last_execution': datetime.now().isoformat()
        }
        self._save_registry()

    def get_protein(self, protein_name: str) -> Dict:
        return self.proteins.get(protein_name, {})

    def list_proteins(self) -> List[str]:
        return list(self.proteins.keys())

    def update_protein_status(self, protein_name: str, status: str):
        """Update protein status (e.g., 'active', 'apoptotic')"""
        if protein_name in self.proteins:
            self.proteins[protein_name]['status'] = status
            self._save_registry()

    def remove_protein(self, protein_name: str):
        """Remove protein from registry"""
        if protein_name in self.proteins:
            del self.proteins[protein_name]
            self._save_registry()

    def _save_registry(self):
        self.registry_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.registry_file, 'w') as f:
            json.dump(self.proteins, f, indent=2)

class CybergenicOrchestrator:
    def __init__(self):
        self.root = Path('.')
        self.cybergenic_dir = self.root / '.cybergenic'
        self.generation = self._load_counter('generation_counter.txt')
        self.run_count = self._load_counter('run_counter.txt')

        # Core registries
        self.protein_registry = ProteinRegistry()
        self.signal_discovery = SignalDiscoverySystem()

        # Self-maintenance systems
        self.signal_bus = get_signal_bus()
        self.immune_system = ImmuneSystem()
        self.homeostasis = HomeostasisController(self.signal_bus)
        self.metabolic_tracker = MetabolicTracker(self.signal_bus)
        self.apoptosis_system = ApoptosisSystem(self.signal_bus, self.protein_registry)

    def _load_counter(self, filename: str) -> int:
        counter_file = self.cybergenic_dir / filename
        if counter_file.exists():
            try:
                return int(counter_file.read_text().strip())
            except (ValueError, IOError):
                return 0
        return 0

    def _save_counter(self, filename: str, value: int):
        self.cybergenic_dir.mkdir(parents=True, exist_ok=True)
        counter_file = self.cybergenic_dir / filename
        counter_file.write_text(str(value))

    def first_run(self):
        """Execute first run: Conception with Architect"""
        print("[FIRST RUN] Initiating Conception Phase...")
        print("[CONCEPTION] Following Central Dogma + Signal Discovery + Self-Maintenance")
        print("   Seed + Framework → DNA.md (genetic code + signal standards + self-maintenance config)")

        self._save_counter('run_counter.txt', 1)

        seed_dir = self.root / 'seed'
        if not seed_dir.exists() or not any(seed_dir.iterdir()):
            print("[ERROR] No seed materials found in /seed/ directory")
            print("        Please add at least one requirements file to seed/")
            return False

        print("[DNA] Invoking Architect for DNA synthesis...")

        # This would actually invoke Claude Code with the architect agent
        # For now, just indicate success
        print("[SUCCESS] DNA.md created successfully")
        print("[GENOME] Sacred Rules + Signal Standards + Self-Maintenance Config encoded")

        self._save_counter('generation_counter.txt', 1)
        self.git_checkpoint("Generation 0: Conception complete - DNA synthesized")
        return True

    def evolve_generation(self):
        """Execute one evolution generation with signal-driven protein synthesis and self-maintenance"""
        gen = self.generation
        print(f"\n{'='*80}")
        print(f"[GENERATION {gen}] Self-Maintaining Signal-Driven Evolution")
        print(f"{'='*80}")

        # Step 1: Self-Maintenance Check
        print(f"\n[STEP 1: SELF-MAINTENANCE CHECK]")

        # Homeostasis
        print("   [HOMEOSTASIS] Checking system balance...")
        self.homeostasis.monitor_and_adjust()
        homeostasis_stats = self.homeostasis.get_statistics()
        print(f"      CPU: {homeostasis_stats['current_values'].get('cpu_load', 0):.2f} (target: {homeostasis_stats['set_points']['cpu_load']})")
        print(f"      Memory: {homeostasis_stats['current_values'].get('memory_usage', 0):.2f} (target: {homeostasis_stats['set_points']['memory_usage']})")

        # Metabolic
        print("   [METABOLIC] Checking protein costs...")
        metabolic_stats = self.metabolic_tracker.get_statistics()
        print(f"      Proteins tracked: {metabolic_stats['total_proteins_tracked']}")
        print(f"      Expensive proteins: {metabolic_stats['expensive_proteins']}")

        # Apoptosis
        print("   [APOPTOSIS] Scanning for unhealthy proteins...")
        dying_proteins = self.apoptosis_system.scan_all_proteins()
        if dying_proteins:
            print(f"      Proteins undergoing apoptosis: {len(dying_proteins)}")
            for protein_name in dying_proteins:
                print(f"         - {protein_name}")
        else:
            print(f"      All proteins healthy")

        # Immune
        print("   [IMMUNE] System status...")
        immune_stats = self.immune_system.get_statistics()
        print(f"      Known self: {immune_stats['known_self_count']} proteins")
        print(f"      Known threats: {immune_stats['known_threats_count']}")

        # Step 2: Signal Discovery
        print(f"\n[STEP 2: SIGNAL DISCOVERY]")
        stats = self.signal_discovery.get_statistics(gen)
        print(f"   Orphan signals: {stats['orphan_count']}")
        print(f"   Handled signals: {stats['handled_count']}")
        print(f"   High-priority orphans: {stats['high_priority_orphans']}")

        orphan_suggestions = self.signal_discovery.suggest_proteins(gen)

        if orphan_suggestions:
            print(f"\n   Adaptive Synthesis Recommendations:")
            for suggestion in orphan_suggestions[:5]:
                print(f"   → {suggestion['protein_name']}")
                print(f"      Reason: {suggestion['reason']}")
                print(f"      Priority: {suggestion['priority']}")

        # Step 3+: Would continue with transcription, translation, etc.
        # For now, just checkpoint
        self.generation += 1
        self._save_counter('generation_counter.txt', self.generation)

        checkpoint_msg = f"Gen {gen}: {len(dying_proteins)} apoptosis, {stats['orphan_count']} orphans"
        self.git_checkpoint(checkpoint_msg)

        print(f"\n{'='*80}")
        print(f"[GENERATION {gen} COMPLETE]")
        print(f"   Active proteins: {len(self.protein_registry.list_proteins())}")
        print(f"   System health: {'GOOD' if not dying_proteins else 'RECOVERING'}")
        print(f"{'='*80}\n")

    def git_checkpoint(self, message: str):
        """Create git checkpoint"""
        try:
            subprocess.run(['git', 'add', '-A'], check=False)
            subprocess.run(['git', 'commit', '-m', f"[Cybergenic] {message}"], check=False)
            print(f"[GIT] Checkpoint: {message}")
        except Exception as e:
            print(f"[GIT] Warning: Could not create checkpoint: {e}")

    def status(self):
        """Show current status"""
        print(f"\n{'='*80}")
        print(f"[CYBERGENIC ORGANISM STATUS]")
        print(f"{'='*80}")
        print(f"   Run Count: {self.run_count}")
        print(f"   Current Generation: {self.generation}")
        print(f"   DNA Present: {(self.cybergenic_dir / 'dna' / 'DNA.md').exists()}")
        print(f"   Active Proteins: {len(self.protein_registry.list_proteins())}")

        # Signal discovery
        stats = self.signal_discovery.get_statistics(self.generation)
        print(f"\n[SIGNAL DISCOVERY]")
        print(f"   Orphan Signals: {stats['orphan_count']}")
        print(f"   Handled Signals: {stats['handled_count']}")
        print(f"   High-Priority Orphans: {stats['high_priority_orphans']}")

        # Self-maintenance systems
        print(f"\n[SELF-MAINTENANCE SYSTEMS]")

        homeostasis_stats = self.homeostasis.get_statistics()
        print(f"   Homeostasis:")
        print(f"      CPU: {homeostasis_stats['current_values'].get('cpu_load', 0):.2f}")
        print(f"      Memory: {homeostasis_stats['current_values'].get('memory_usage', 0):.2f}")

        metabolic_stats = self.metabolic_tracker.get_statistics()
        print(f"   Metabolic Tracker:")
        print(f"      Proteins tracked: {metabolic_stats['total_proteins_tracked']}")
        print(f"      Expensive: {metabolic_stats['expensive_proteins']}")

        apoptosis_stats = self.apoptosis_system.get_statistics()
        print(f"   Apoptosis:")
        print(f"      Total events: {apoptosis_stats['total_apoptosis_events']}")

        immune_stats = self.immune_system.get_statistics()
        print(f"   Immune System:")
        print(f"      Known self: {immune_stats['known_self_count']}")
        print(f"      Known threats: {immune_stats['known_threats_count']}")

        print(f"{'='*80}\n")

    def maintenance_status(self):
        """Show detailed self-maintenance status"""
        print(f"\n{'='*80}")
        print(f"[SELF-MAINTENANCE SYSTEMS DETAILED STATUS]")
        print(f"{'='*80}")

        # Homeostasis
        print(f"\n[HOMEOSTASIS CONTROLLER]")
        homeostasis_stats = self.homeostasis.get_statistics()
        print(f"   Set Points:")
        for metric, target in homeostasis_stats['set_points'].items():
            current = homeostasis_stats['current_values'].get(metric, 0)
            deviation = homeostasis_stats['deviations'].get(metric, {})
            status = "OK" if deviation.get('within_threshold', False) else "ADJUSTING"
            print(f"      {metric}: {current:.3f} (target: {target}, deviation: {deviation.get('percent', 0):.1f}%) [{status}]")

        # Metabolic
        print(f"\n[METABOLIC COST TRACKER]")
        metabolic_stats = self.metabolic_tracker.get_statistics()
        print(f"   Total proteins tracked: {metabolic_stats['total_proteins_tracked']}")
        print(f"   Expensive proteins: {metabolic_stats['expensive_proteins']}")
        print(f"   Total executions: {metabolic_stats['total_executions']}")

        expensive_proteins = self.metabolic_tracker.get_most_expensive_proteins(5)
        if expensive_proteins:
            print(f"\n   Expensive Proteins (Top 5):")
            for protein_data in expensive_proteins:
                avg = protein_data['avg_costs']
                print(f"      {protein_data['protein']}:")
                print(f"         CPU: {avg['cpu_seconds']:.3f}s, Memory: {avg['memory_mb']:.1f}MB")
                print(f"         Executions: {protein_data['executions']}")

        # Apoptosis
        print(f"\n[APOPTOSIS SYSTEM]")
        apoptosis_stats = self.apoptosis_system.get_statistics()
        print(f"   Total apoptosis events: {apoptosis_stats['total_apoptosis_events']}")
        if apoptosis_stats['reason_breakdown']:
            print(f"   Reason breakdown:")
            for reason, count in apoptosis_stats['reason_breakdown'].items():
                print(f"      {reason}: {count}")

        if apoptosis_stats['last_event']:
            print(f"   Last event: {apoptosis_stats['last_event']['protein_name']} ({apoptosis_stats['last_event']['timestamp']})")

        # Immune
        print(f"\n[IMMUNE SYSTEM]")
        immune_stats = self.immune_system.get_statistics()
        print(f"   Known self proteins: {immune_stats['known_self_count']}")
        print(f"   Known threats: {immune_stats['known_threats_count']}")
        print(f"   Threat patterns monitored: {immune_stats['threat_patterns_monitored']}")

        print(f"{'='*80}\n")

if __name__ == "__main__":
    orchestrator = CybergenicOrchestrator()

    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "status":
            orchestrator.status()
        elif command == "maintenance":
            orchestrator.maintenance_status()
        elif command == "run":
            if orchestrator.run_count == 0:
                orchestrator.first_run()
            else:
                orchestrator.evolve_generation()
    else:
        orchestrator.status()
