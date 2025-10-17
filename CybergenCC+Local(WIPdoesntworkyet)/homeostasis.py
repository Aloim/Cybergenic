"""
Homeostasis System for Cybergenic Organisms
Maintains optimal operating conditions through negative feedback loops
"""

import json
import psutil
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

class HomeostasisController:
    """Maintains organism balance through negative feedback loops"""

    def __init__(self, signal_bus):
        self.signal_bus = signal_bus
        self.state_file = Path('.cybergenic/homeostasis_state.json')

        # Set points (targets) - these can be configured in DNA.md
        self.set_points = {
            "cpu_load": 0.7,           # Target 70% CPU
            "memory_usage": 0.8,       # Target 80% memory
            "error_rate": 0.01,        # Target 1% errors
            "api_cost_per_hour": 1.0,  # Target $1/hour
            "response_time_ms": 200    # Target 200ms
        }

        # Deviation thresholds (when to act) - 10% by default
        self.deviation_threshold = 0.1

        # Current values
        self.current_values = {}

        # History for trend analysis
        self.history = []
        self.max_history = 1000

        # Load previous state
        self._load_state()

    def _load_state(self):
        """Load homeostasis state from file"""
        if self.state_file.exists():
            try:
                with open(self.state_file) as f:
                    data = json.load(f)
                    self.current_values = data.get('current_values', {})
                    self.history = data.get('history', [])[-self.max_history:]
            except (json.JSONDecodeError, IOError):
                pass

    def _save_state(self):
        """Save homeostasis state to file"""
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        data = {
            'current_values': self.current_values,
            'set_points': self.set_points,
            'history': self.history[-self.max_history:],
            'last_updated': datetime.now().isoformat()
        }
        try:
            with open(self.state_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"[HOMEOSTASIS] Failed to save state: {e}")

    def measure(self, metric: str) -> float:
        """Measure current value of a metric"""
        try:
            if metric == "cpu_load":
                return psutil.cpu_percent(interval=0.1) / 100.0
            elif metric == "memory_usage":
                return psutil.virtual_memory().percent / 100.0
            elif metric == "error_rate":
                # Would track from actual errors
                return self.current_values.get("error_rate", 0.0)
            elif metric == "api_cost_per_hour":
                # Would track from actual API usage
                return self.current_values.get("api_cost_per_hour", 0.0)
            elif metric == "response_time_ms":
                # Would track from actual response times
                return self.current_values.get("response_time_ms", 0.0)
        except Exception as e:
            print(f"[HOMEOSTASIS] Error measuring {metric}: {e}")
            return 0.0

        return 0.0

    def update_metric(self, metric: str, value: float):
        """Manually update a metric value (for non-system metrics)"""
        self.current_values[metric] = value

    def monitor_and_adjust(self):
        """Main homeostasis loop - continuous monitoring"""
        adjustments_made = []

        for metric, target in self.set_points.items():
            current = self.measure(metric)
            self.current_values[metric] = current

            # Calculate deviation
            deviation = current - target
            deviation_percent = (deviation / target * 100) if target != 0 else 0

            # Apply feedback if deviation exceeds threshold
            if abs(deviation) > self.deviation_threshold * target:
                adjustment = self.apply_feedback(metric, deviation, current, target)
                if adjustment:
                    adjustments_made.append(adjustment)

            # Record history
            self.history.append({
                'metric': metric,
                'value': current,
                'target': target,
                'deviation': deviation,
                'deviation_percent': deviation_percent,
                'timestamp': datetime.now().isoformat()
            })

        # Keep history bounded
        if len(self.history) > self.max_history:
            self.history = self.history[-self.max_history:]

        # Save state periodically
        if len(self.history) % 10 == 0:
            self._save_state()

        return adjustments_made

    def apply_feedback(self, metric: str, deviation: float, current: float, target: float) -> Optional[Dict]:
        """Apply negative feedback to restore balance"""

        adjustment = {
            'metric': metric,
            'deviation': deviation,
            'action': None
        }

        if metric == "cpu_load":
            if deviation > 0:  # Too high
                self.signal_bus.emit("HIGH_LOAD", {
                    "cpu": current,
                    "target": target,
                    "deviation": deviation,
                    "action": "switch_to_efficient_conformations"
                })
                adjustment['action'] = "emitted_HIGH_LOAD"
            else:  # Too low
                self.signal_bus.emit("LOW_LOAD", {
                    "cpu": current,
                    "target": target,
                    "action": "can_use_detailed_conformations"
                })
                adjustment['action'] = "emitted_LOW_LOAD"

        elif metric == "memory_usage":
            if deviation > 0:
                self.signal_bus.emit("HIGH_MEMORY", {
                    "memory": current,
                    "target": target,
                    "action": "garbage_collect_and_optimize"
                })
                adjustment['action'] = "emitted_HIGH_MEMORY"
            else:
                self.signal_bus.emit("LOW_MEMORY", {
                    "memory": current,
                    "action": "can_allocate_freely"
                })
                adjustment['action'] = "emitted_LOW_MEMORY"

        elif metric == "error_rate":
            if deviation > 0:
                self.signal_bus.emit("ERROR_SPIKE", {
                    "rate": current,
                    "target": target,
                    "action": "enable_circuit_breakers"
                })
                adjustment['action'] = "emitted_ERROR_SPIKE"
            else:
                self.signal_bus.emit("STABLE_OPERATION", {
                    "rate": current,
                    "action": "can_take_more_risks"
                })
                adjustment['action'] = "emitted_STABLE_OPERATION"

        elif metric == "api_cost_per_hour":
            if deviation > 0:
                self.signal_bus.emit("COST_EXCEEDED", {
                    "rate": current,
                    "target": target,
                    "action": "use_cheaper_models"
                })
                adjustment['action'] = "emitted_COST_EXCEEDED"
            else:
                self.signal_bus.emit("BUDGET_AVAILABLE", {
                    "rate": current,
                    "action": "can_use_expensive_models"
                })
                adjustment['action'] = "emitted_BUDGET_AVAILABLE"

        elif metric == "response_time_ms":
            if deviation > 0:
                self.signal_bus.emit("SLOW_RESPONSE", {
                    "time": current,
                    "target": target,
                    "action": "optimize_or_cache"
                })
                adjustment['action'] = "emitted_SLOW_RESPONSE"

        return adjustment if adjustment['action'] else None

    def get_statistics(self) -> Dict:
        """Get homeostasis statistics"""
        stats = {
            'current_values': self.current_values,
            'set_points': self.set_points,
            'deviations': {}
        }

        for metric, target in self.set_points.items():
            current = self.current_values.get(metric, 0)
            deviation = current - target
            stats['deviations'][metric] = {
                'absolute': deviation,
                'percent': (deviation / target * 100) if target != 0 else 0,
                'within_threshold': abs(deviation) <= self.deviation_threshold * target
            }

        return stats

    def set_target(self, metric: str, target: float):
        """Update a set point target"""
        if metric in self.set_points:
            self.set_points[metric] = target
            self._save_state()

    def get_trend(self, metric: str, window: int = 10) -> str:
        """Get trend for a metric (increasing, decreasing, stable)"""
        recent = [h for h in self.history[-window:] if h['metric'] == metric]

        if len(recent) < 2:
            return "insufficient_data"

        values = [h['value'] for h in recent]
        avg_first_half = sum(values[:len(values)//2]) / (len(values)//2)
        avg_second_half = sum(values[len(values)//2:]) / (len(values) - len(values)//2)

        change = avg_second_half - avg_first_half

        if abs(change) < 0.05:
            return "stable"
        elif change > 0:
            return "increasing"
        else:
            return "decreasing"
