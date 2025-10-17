"""
Immune System for Cybergenic Organisms
Detects and eliminates threats through self/non-self recognition
"""

import json
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class ImmuneSystem:
    """Distinguishes self from non-self and eliminates threats"""

    def __init__(self):
        self.memory_file = Path('.cybergenic/immune_memory.json')
        self.known_self: set = set()  # (protein_name, signature) tuples
        self.known_threats = self._load_threats()

        # Threat patterns to detect
        self.threat_patterns = [
            # Code injection
            (r'eval\s*\(', "code_injection"),
            (r'exec\s*\(', "code_injection"),
            (r'__import__\s*\(', "suspicious_import"),
            (r'compile\s*\(', "dynamic_compilation"),

            # System commands
            (r'os\.system\s*\(', "system_command"),
            (r'subprocess\.call\s*\(', "system_command"),
            (r'subprocess\.run\s*\(', "system_command"),
            (r'subprocess\.Popen\s*\(', "system_command"),

            # Infinite loops
            (r'while\s+True\s*:', "infinite_loop_risk"),

            # SQL injection
            (r'DROP\s+TABLE', "sql_injection"),
            (r'DELETE\s+FROM.*WHERE.*=.*\+', "sql_injection_risk"),
            (r'INSERT\s+INTO.*VALUES.*\+', "sql_injection_risk"),

            # Path traversal
            (r'\.\./|\.\.\\', "path_traversal"),

            # Resource exhaustion
            (r'fork\s*\(', "resource_exhaustion"),
            (r'os\.fork\s*\(', "resource_exhaustion"),

            # Network attacks
            (r'socket\.socket\s*\(.*socket\.RAW', "raw_socket"),

            # File system risks
            (r'os\.remove\s*\(.*[\*\?]', "wildcard_deletion"),
            (r'shutil\.rmtree\s*\(', "recursive_deletion_risk"),
        ]

    def _load_threats(self) -> List[Dict]:
        """Load known threats from immune memory"""
        if self.memory_file.exists():
            try:
                with open(self.memory_file) as f:
                    data = json.load(f)
                    return data.get('threats', [])
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def _save_threats(self):
        """Save threats to immune memory"""
        self.memory_file.parent.mkdir(parents=True, exist_ok=True)
        data = {
            'threats': self.known_threats,
            'last_updated': datetime.now().isoformat(),
            'known_self_count': len(self.known_self)
        }
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"[IMMUNE] Failed to save memory: {e}")

    def compute_signature(self, code: str) -> str:
        """Compute cryptographic signature of protein code"""
        return hashlib.sha256(code.encode()).hexdigest()[:16]

    def register_self(self, protein_name: str, code: str):
        """Register a protein as trusted self"""
        signature = self.compute_signature(code)
        self.known_self.add((protein_name, signature))

    def is_recognized_self(self, protein_name: str, code: str) -> bool:
        """Check if protein is recognized as self"""
        signature = self.compute_signature(code)
        return (protein_name, signature) in self.known_self

    def check_protein(self, protein_name: str, code: str) -> Tuple[bool, Optional[List[str]]]:
        """
        Validate protein for threats.
        Returns (is_safe, threat_list)
        """
        # Check if recognized self
        if self.is_recognized_self(protein_name, code):
            return (True, None)

        # Scan for threat patterns
        threats_found = []

        for pattern, threat_type in self.threat_patterns:
            if re.search(pattern, code, re.IGNORECASE):
                threats_found.append(threat_type)

        # Special check for infinite loops
        if self._has_uncontrolled_infinite_loop(code):
            threats_found.append("infinite_loop_confirmed")

        # Check against known threats
        for known_threat in self.known_threats:
            if self._matches_threat_pattern(code, known_threat['pattern']):
                threats_found.append(f"known_threat_{known_threat['id']}")

        if threats_found:
            # Learn this threat
            self._learn_threat(protein_name, code, threats_found)
            return (False, threats_found)

        # Looks safe - register as self
        self.register_self(protein_name, code)
        return (True, None)

    def _has_uncontrolled_infinite_loop(self, code: str) -> bool:
        """Check for while True without break"""
        # Find all "while True:" blocks
        while_true_pattern = r'while\s+True\s*:'
        matches = list(re.finditer(while_true_pattern, code))

        if not matches:
            return False

        for match in matches:
            # Get the next 10 lines after "while True:"
            start_pos = match.end()
            next_lines = code[start_pos:start_pos + 500]  # Check next 500 chars

            # Check if there's a break statement
            if 'break' not in next_lines and 'return' not in next_lines:
                return True

        return False

    def _matches_threat_pattern(self, code: str, pattern: str) -> bool:
        """Check if code matches a known threat pattern"""
        # Use fuzzy matching - check if significant portion matches
        pattern_length = len(pattern)
        code_length = len(code)

        # If pattern is longer, can't match
        if pattern_length > code_length:
            return False

        # Simple substring match for now
        # Could be enhanced with more sophisticated matching
        return pattern in code

    def _learn_threat(self, protein_name: str, code: str, threats: List[str]):
        """Add new threat to immune memory"""
        threat_entry = {
            'id': len(self.known_threats),
            'protein_name': protein_name,
            'pattern': code[:500],  # Store snippet (first 500 chars)
            'signature': self.compute_signature(code),
            'threats': threats,
            'first_seen': datetime.now().isoformat(),
            'encounter_count': 1
        }

        self.known_threats.append(threat_entry)
        self._save_threats()

    def get_statistics(self) -> Dict:
        """Get immune system statistics"""
        return {
            'known_self_count': len(self.known_self),
            'known_threats_count': len(self.known_threats),
            'threat_patterns_monitored': len(self.threat_patterns)
        }

    def export_self_signatures(self) -> List[Tuple[str, str]]:
        """Export all known self signatures for backup"""
        return list(self.known_self)

    def import_self_signatures(self, signatures: List[Tuple[str, str]]):
        """Import known self signatures from backup"""
        self.known_self.update(signatures)
