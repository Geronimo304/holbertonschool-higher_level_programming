#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Load a JSON file and return the corresponding Python dictionary."""
    with open(filename, 'r') as f:
        return json.load(f)
