#!/usr/bin/env python3
"""
Chris — Unlock the fullest potential of your device
Cross-platform iOS customization tool
"""

import sys
import os

# Ensure src is in path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.gui.main_window import launch

if __name__ == "__main__":
    launch()
