"""
Metabolic Cost Tracker for Cybergenic Organisms
Tracks resource consumption (ATP = tokens, CPU, memory)
"""

import json
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
from collections import defaultdict

class MetabolicTracker:
    """Track the energy cost of all operations"""

    def __init__(self, signal_bus):
        self.signal_bus = signal_bus
        self.costs_file = Path('.cybergenic/metabolic_costs.json')

        # Cost tracking per protein
        self.protein_costs = defaultdict(list)

        # Thresholds for expensive warnings
        self.thresholds = {
            'cpu_seconds': 0.1,      # 100ms
            'memory_mb': 100,        # 100 MB
            'api_tokens': 10000,     # 10k tokens
            'cost_usd': 0.01         # 1 cent
        }

        # Load existing data
        self._load_costs()

    def _load_costs(self):
        """Load metabolic costs from file"""
        if self.costs_file.exists():
            try:
                with open(self.costs_file) as f:
                    data = json.load(f)
                    for protein_name, costs in data.get('proteins', {}).items():
                        self.protein_costs[protein_name] = costs
            except (json.JSONDecodeError, IOError):
                pass

    def _save_costs(self):
        """Save metabolic costs to file"""
        self.costs_file.parent.mkdir(parents=True, exist_ok=True)
        data = {
            'proteins': dict(self.protein_costs),
            'last_updated': datetime.now().isoformat()
        }
        try:
            with open(self.costs_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"[METABOLIC] Failed to save costs: {e}")

    def record_execution(self, protein_name: str, cpu_seconds: float,
                        memory_mb: float, api_tokens: int = 0, cost_usd: float = 0.0):
        """Record the cost of a protein execution"""

        cost_entry = {
            'cpu_seconds': cpu_seconds,
            'memory_mb': memory_mb,
            'api_tokens': api_tokens,
            'cost_usd': cost_usd,
            'timestamp': datetime.now().isoformat()
        }

        self.protein_costs[protein_name].append(cost_entry)

        # Keep only last 100 executions per protein
        if len(self.protein_costs[protein_name]) > 100:
            self.protein_costs[protein_name] = self.protein_costs[protein_name][-100:]

        # Check if protein is too expensive
        if self._is_too_expensive(protein_name):
            avg_costs = self._get_average_costs(protein_name)

            self.signal_bus.emit("PROTEIN_TOO_EXPENSIVE", {
                "protein": protein_name,
                "avg_cpu": avg_costs['cpu_seconds'],
                "avg_memory": avg_costs['memory_mb'],
                "avg_cost": avg_costs['cost_usd'],
                "executions": len(self.protein_costs[protein_name]),
                "suggestions": self._get_optimization_suggestions(avg_costs)
            })

        # Periodic save
        if sum(len(costs) for costs in self.protein_costs.values()) % 50 == 0:
            self._save_costs()

    def _is_too_expensive(self, protein_name: str) -> bool:
        """Check if protein exceeds cost thresholds"""
        if len(self.protein_costs[protein_name]) < 10:
            return False  # Need more data

        avg = self._get_average_costs(protein_name)

        return (avg['cpu_seconds'] > self.thresholds['cpu_seconds'] or
                avg['memory_mb'] > self.thresholds['memory_mb'] or
                avg['api_tokens'] > self.thresholds['api_tokens'] or
                avg['cost_usd'] > self.thresholds['cost_usd'])

    def _get_average_costs(self, protein_name: str) -> Dict:
        """Calculate average costs for a protein"""
        costs = self.protein_costs[protein_name]

        if not costs:
            return {
                'cpu_seconds': 0,
                'memory_mb': 0,
                'api_tokens': 0,
                'cost_usd': 0
            }

        return {
            'cpu_seconds': sum(c['cpu_seconds'] for c in costs) / len(costs),
            'memory_mb': sum(c['memory_mb'] for c in costs) / len(costs),
            'api_tokens': sum(c['api_tokens'] for c in costs) / len(costs),
            'cost_usd': sum(c['cost_usd'] for c in costs) / len(costs)
        }

    def _get_optimization_suggestions(self, avg_costs: Dict) -> List[str]:
        """Suggest optimizations based on cost profile"""
        suggestions = []

        if avg_costs['cpu_seconds'] > self.thresholds['cpu_seconds']:
            suggestions.append("Add caching conformation")
            suggestions.append("Optimize algorithm complexity")
            suggestions.append("Consider parallel processing")

        if avg_costs['memory_mb'] > self.thresholds['memory_mb']:
            suggestions.append("Use streaming instead of loading all data")
            suggestions.append("Implement memory-efficient data structures")
            suggestions.append("Add memory pooling")

        if avg_costs['api_tokens'] > self.thresholds['api_tokens']:
            suggestions.append("Use cheaper model for this task")
            suggestions.append("Batch multiple operations")
            suggestions.append("Add result caching")
            suggestions.append("Reduce prompt size")

        if avg_costs['cost_usd'] > self.thresholds['cost_usd']:
            suggestions.append("Switch to more economical model")
            suggestions.append("Implement request throttling")

        return suggestions

    def get_protein_stats(self, protein_name: str) -> Optional[Dict]:
        """Get cost statistics for a specific protein"""
        if protein_name not in self.protein_costs:
            return None

        costs = self.protein_costs[protein_name]
        avg = self._get_average_costs(protein_name)

        return {
            'executions': len(costs),
            'average_costs': avg,
            'total_costs': {
                'cpu_seconds': sum(c['cpu_seconds'] for c in costs),
                'memory_mb': sum(c['memory_mb'] for c in costs),
                'api_tokens': sum(c['api_tokens'] for c in costs),
                'cost_usd': sum(c['cost_usd'] for c in costs)
            },
            'is_expensive': self._is_too_expensive(protein_name),
            'suggestions': self._get_optimization_suggestions(avg) if self._is_too_expensive(protein_name) else []
        }

    def get_statistics(self) -> Dict:
        """Get overall metabolic statistics"""
        total_proteins = len(self.protein_costs)
        expensive_proteins = sum(1 for p in self.protein_costs.keys()
                                if self._is_too_expensive(p))

        total_executions = sum(len(costs) for costs in self.protein_costs.values())

        return {
            'total_proteins_tracked': total_proteins,
            'expensive_proteins': expensive_proteins,
            'total_executions': total_executions
        }

    def get_most_expensive_proteins(self, n: int = 10) -> List[Dict]:
        """Get the N most expensive proteins"""
        protein_avgs = []

        for protein_name in self.protein_costs.keys():
            avg = self._get_average_costs(protein_name)
            # Composite cost score
            score = (avg['cpu_seconds'] * 10 +
                    avg['memory_mb'] / 100 +
                    avg['cost_usd'] * 100)

            protein_avgs.append({
                'protein': protein_name,
                'score': score,
                'avg_costs': avg,
                'executions': len(self.protein_costs[protein_name])
            })

        # Sort by score descending
        protein_avgs.sort(key=lambda x: x['score'], reverse=True)

        return protein_avgs[:n]

    def set_threshold(self, metric: str, value: float):
        """Update a threshold value"""
        if metric in self.thresholds:
            self.thresholds[metric] = value
            self._save_costs()
