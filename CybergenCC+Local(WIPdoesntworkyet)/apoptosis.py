"""
Apoptosis System for Cybergenic Organisms
Proteins self-destruct when damaged or obsolete
"""

import json
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class ApoptosisSystem:
    """Manages programmed cell death for proteins"""

    def __init__(self, signal_bus, protein_registry):
        self.signal_bus = signal_bus
        self.protein_registry = protein_registry
        self.log_file = Path('.cybergenic/apoptosis_log.json')

        # Default thresholds (can be overridden in DNA.md)
        self.thresholds = {
            'max_error_count': 10,
            'max_unused_days': 7,
            'min_success_rate': 0.5
        }

        # Apoptosis log
        self.log = self._load_log()

    def _load_log(self) -> List[Dict]:
        """Load apoptosis log from file"""
        if self.log_file.exists():
            try:
                with open(self.log_file) as f:
                    return json.load(f).get('events', [])
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def _save_log(self):
        """Save apoptosis log to file"""
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        data = {
            'events': self.log,
            'last_updated': datetime.now().isoformat()
        }
        try:
            with open(self.log_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"[APOPTOSIS] Failed to save log: {e}")

    def check_protein_health(self, protein_name: str, protein_data: Dict) -> bool:
        """
        Check if protein should undergo apoptosis.
        Returns True if protein should die.
        """
        reasons = []

        # Check error count
        error_count = protein_data.get('error_count', 0)
        if error_count > self.thresholds['max_error_count']:
            reasons.append(f"excessive_errors_{error_count}")

        # Check last use
        last_execution = protein_data.get('last_execution')
        if last_execution:
            try:
                last_exec_time = datetime.fromisoformat(last_execution)
                days_unused = (datetime.now() - last_exec_time).days
                if days_unused > self.thresholds['max_unused_days']:
                    reasons.append(f"unused_{days_unused}_days")
            except (ValueError, TypeError):
                pass

        # Check success rate
        total_executions = protein_data.get('total_executions', 0)
        successful_executions = protein_data.get('successful_executions', 0)
        if total_executions > 10:  # Need enough data
            success_rate = successful_executions / total_executions
            if success_rate < self.thresholds['min_success_rate']:
                reasons.append(f"low_success_rate_{success_rate:.2f}")

        # Check self-reported health
        if protein_data.get('self_check_failed', False):
            reasons.append("self_check_failed")

        if reasons:
            self.initiate_apoptosis(protein_name, reasons, protein_data)
            return True

        return False

    def initiate_apoptosis(self, protein_name: str, reasons: List[str], protein_data: Dict):
        """Execute programmed cell death for a protein"""

        # Log apoptosis event
        event = {
            'protein_name': protein_name,
            'reasons': reasons,
            'timestamp': datetime.now().isoformat(),
            'capabilities': protein_data.get('capabilities', []),
            'generation': protein_data.get('generation', 'unknown'),
            'error_count': protein_data.get('error_count', 0),
            'total_executions': protein_data.get('total_executions', 0),
            'successful_executions': protein_data.get('successful_executions', 0)
        }

        self.log.append(event)
        self._save_log()

        # Emit signals
        self.signal_bus.emit("APOPTOSIS_INITIATED", {
            "protein": protein_name,
            "reasons": reasons,
            "error_count": protein_data.get('error_count', 0)
        })

        # Mark protein as apoptotic
        self.protein_registry.update_protein_status(protein_name, 'apoptotic')

        # Request replacement
        self.signal_bus.emit("PROTEIN_REPLACEMENT_NEEDED", {
            "protein": protein_name,
            "capabilities": protein_data.get('capabilities', []),
            "responds_to": protein_data.get('responds_to', []),
            "priority": "high" if "excessive_errors" in str(reasons) else "medium"
        })

        # Note: Actual removal would happen in the next generation
        # For now, just mark as apoptotic

    def scan_all_proteins(self) -> List[str]:
        """Scan all proteins and initiate apoptosis for unhealthy ones"""
        proteins_to_check = self.protein_registry.list_proteins()

        dying_proteins = []
        for protein_name in proteins_to_check:
            protein_data = self.protein_registry.get_protein(protein_name)

            # Skip already apoptotic proteins
            if protein_data.get('status') == 'apoptotic':
                continue

            if self.check_protein_health(protein_name, protein_data):
                dying_proteins.append(protein_name)

        if dying_proteins:
            self.signal_bus.emit("APOPTOSIS_SCAN_COMPLETE", {
                "proteins_scanned": len(proteins_to_check),
                "proteins_dying": len(dying_proteins),
                "dying_list": dying_proteins
            })

        return dying_proteins

    def get_statistics(self) -> Dict:
        """Get apoptosis statistics"""
        total_events = len(self.log)

        # Count by reason
        reason_counts = {}
        for event in self.log:
            for reason in event['reasons']:
                # Extract base reason (remove numbers)
                base_reason = ''.join([c for c in reason if not c.isdigit() and c != '_'])
                reason_counts[base_reason] = reason_counts.get(base_reason, 0) + 1

        return {
            'total_apoptosis_events': total_events,
            'reason_breakdown': reason_counts,
            'last_event': self.log[-1] if self.log else None
        }

    def get_recent_events(self, n: int = 10) -> List[Dict]:
        """Get the N most recent apoptosis events"""
        return self.log[-n:] if len(self.log) >= n else self.log

    def set_threshold(self, threshold_name: str, value: float):
        """Update an apoptosis threshold"""
        if threshold_name in self.thresholds:
            self.thresholds[threshold_name] = value
