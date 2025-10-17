"""
SignalBus for organism-wide coordination and signal discovery
Enables promiscuous signal emission and orphan tracking
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Callable, Any, Dict, List, Optional

class SignalBus:
    """
    Coordinates proteins through environmental signals.
    Tracks all emissions for orphan signal discovery.
    """

    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}
        self.signal_log_file = Path('.cybergenic/signal_log.json')
        self.signal_log = self._load_log()
        self.active_signals = {}
        self.emission_count = {}

    def _load_log(self) -> List[Dict]:
        """Load signal log from file"""
        if self.signal_log_file.exists():
            try:
                with open(self.signal_log_file) as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def emit(self, signal_type: str, data: Any = None):
        """
        Broadcast signal to all subscribers.
        ALWAYS call this - even if no handlers exist yet.
        This is how orphan signals are discovered.
        """
        entry = {
            "type": signal_type,
            "data": data,
            "timestamp": datetime.now().isoformat(),
            "has_handlers": signal_type in self.subscribers and len(self.subscribers[signal_type]) > 0
        }

        self.signal_log.append(entry)
        self.active_signals[signal_type] = data

        # Track emission count
        self.emission_count[signal_type] = self.emission_count.get(signal_type, 0) + 1

        # Save to file periodically (every 10 emissions)
        if len(self.signal_log) % 10 == 0:
            self._save_log()

        # Notify subscribers if any exist
        handler_count = len(self.subscribers.get(signal_type, []))
        if handler_count > 0:
            for callback in self.subscribers[signal_type]:
                try:
                    callback(data)
                except Exception as e:
                    print(f"[SIGNAL ERROR] Handler failed for {signal_type}: {e}")
        else:
            # This is an orphan signal - tracked automatically
            pass

    def subscribe(self, signal_type: str, callback: Callable):
        """
        Subscribe a protein to environmental signals.

        Example:
            signal_bus.subscribe("HIGH_LOAD", protein.switch_to_fast_mode)
        """
        if signal_type not in self.subscribers:
            self.subscribers[signal_type] = []
        self.subscribers[signal_type].append(callback)
        print(f"[SIGNAL BUS] {signal_type} → handler registered")

    def unsubscribe(self, signal_type: str, callback: Callable):
        """Remove a subscription"""
        if signal_type in self.subscribers:
            try:
                self.subscribers[signal_type].remove(callback)
            except ValueError:
                pass

    def get_active_signal(self, signal_type: str) -> Any:
        """Get the most recent data for a signal type"""
        return self.active_signals.get(signal_type)

    def clear_signal(self, signal_type: str):
        """Clear an active signal (return to baseline)"""
        if signal_type in self.active_signals:
            del self.active_signals[signal_type]
            self.emit(f"{signal_type}_CLEARED", {})

    def get_orphan_signals(self) -> Dict[str, int]:
        """Get signals with no handlers and their emission counts"""
        orphans = {}
        for signal_type, count in self.emission_count.items():
            if signal_type not in self.subscribers or len(self.subscribers[signal_type]) == 0:
                orphans[signal_type] = count
        return orphans

    def get_statistics(self) -> Dict:
        """Get signal bus statistics"""
        total_emissions = sum(self.emission_count.values())
        handled_signals = len([s for s in self.emission_count.keys() if s in self.subscribers and self.subscribers[s]])
        orphan_signals = len(self.get_orphan_signals())

        return {
            "total_emissions": total_emissions,
            "unique_signals": len(self.emission_count),
            "handled_signals": handled_signals,
            "orphan_signals": orphan_signals,
            "coverage_percent": (handled_signals / len(self.emission_count) * 100) if self.emission_count else 0
        }

    def _save_log(self):
        """Save signal log to file"""
        # Keep only last 10000 entries to prevent file bloat
        if len(self.signal_log) > 10000:
            self.signal_log = self.signal_log[-10000:]

        try:
            with open(self.signal_log_file, 'w') as f:
                json.dump(self.signal_log, f, indent=2)
        except Exception as e:
            print(f"[SIGNAL BUS] Failed to save log: {e}")

# Global signal bus instance
_signal_bus = None

def get_signal_bus() -> SignalBus:
    """Get or create the global signal bus"""
    global _signal_bus
    if _signal_bus is None:
        _signal_bus = SignalBus()
    return _signal_bus
