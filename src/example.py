"""Example module for the tfb-heal-sentinel demo.

Baseline shape: honest code. PRs against this module let the reviewer
demonstrate its discipline on real diffs.
"""


def load_payload(path):
    """Read + parse JSON from `path`. Raises OSError or ValueError on wound."""
    import json
    body = path.read_text()
    return json.loads(body)


def handle_edge_case(x):
    """Handle a specific edge case named in the tests."""
    if x is None:
        return None
    return x + 1
