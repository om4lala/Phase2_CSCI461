"""
CLI package - re-exports metrics from src.cli.metrics
"""
import sys
import importlib.util
from pathlib import Path

# Get the path to src/cli/metrics.py
src_metrics_path = Path(__file__).parent.parent / "src" / "cli" / "metrics.py"

# Load the metrics module directly
spec = importlib.util.spec_from_file_location("cli.metrics", src_metrics_path)
metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metrics)

__all__ = ["metrics"]

