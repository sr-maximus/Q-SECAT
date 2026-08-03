#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from qsecat.catalog import check_traceability

print(json.dumps({"valid": True, "counts": check_traceability(ROOT)}, indent=2))
