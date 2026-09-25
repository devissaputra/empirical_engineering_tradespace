#!/usr/bin/env python3
from research.model import load_summary, load_sensitivity_summary, validate_bundle
import json

print(json.dumps(load_summary(), indent=2, ensure_ascii=False))
print(json.dumps(load_sensitivity_summary(), indent=2, ensure_ascii=False))
print("bundle_validation:", "PASS" if validate_bundle() else "FAIL")
