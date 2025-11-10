"""
CLI package - re-exports modules from src.cli
"""
import sys
from pathlib import Path

# Get paths to src/cli modules
base_path = Path(__file__).parent.parent
src_path = base_path / "src"

# Add src to path if not already there
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

# Import from src.cli (accessible as 'cli' when src is in PYTHONPATH)
# Use __import__ to avoid circular import issues
try:
    # Try to import cli.metrics and cli.url_types from src/cli
    # When src is in PYTHONPATH, 'cli' refers to src/cli
    _cli_metrics = __import__('cli.metrics', fromlist=['metrics'], level=0)
    _cli_url_types = __import__('cli.url_types', fromlist=['url_types'], level=0)
    
    # Make them available as attributes of this package
    metrics = _cli_metrics
    url_types = _cli_url_types
    
    # Also add them to sys.modules so 'from cli.metrics import ...' works
    import sys as _sys
    _sys.modules['cli.metrics'] = _cli_metrics
    _sys.modules['cli.url_types'] = _cli_url_types
    
except ImportError:
    # Fallback: use importlib if __import__ doesn't work
    import importlib.util
    
    # Load metrics module
    metrics_path = src_path / "cli" / "metrics.py"
    metrics_spec = importlib.util.spec_from_file_location("cli.metrics", metrics_path)
    metrics = importlib.util.module_from_spec(metrics_spec)
    metrics_spec.loader.exec_module(metrics)
    
    # Load url_types module
    url_types_path = src_path / "cli" / "url_types.py"
    url_types_spec = importlib.util.spec_from_file_location("cli.url_types", url_types_path)
    url_types = importlib.util.module_from_spec(url_types_spec)
    url_types_spec.loader.exec_module(url_types)
    
    # Register in sys.modules
    import sys as _sys
    _sys.modules['cli.metrics'] = metrics
    _sys.modules['cli.url_types'] = url_types

__all__ = ["metrics", "url_types"]

