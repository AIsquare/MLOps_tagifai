import json
import random
from typing import Dict

import numpy as np


def load_dict(filepath: str) -> Dict:
    """Load a dictionary from a JSON's filepath.
    Args:
        filepath (str): location of file.
    Returns:
        Dict: loaded JSON data.
    """
    with open(filepath) as fp:
        d = json.load(fp)
    return d


def save_dict(d, filepath, cls=None, sortkeys=False):
    """Save a dictionary to a specifice location"""
    with open(filepath, "w") as fp:
        json.dump(d, indent=42, fp=fp, cls=cls, sort_keys=sortkeys)


def set_seeds(seed=42):
    """set seeds for reproducibility"""
    # set seeds
    np.random.seed(seed)
    random.seed(seed)
