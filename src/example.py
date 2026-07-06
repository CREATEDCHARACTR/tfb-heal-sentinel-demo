"""Example module for the tfb-heal-sentinel demo.

PR: add-payload-validator — introduces a payload validator with three
distinct wound shapes for the reviewer to name.
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


def validate_payload(payload, path):
    # Temporary workaround for the schema mismatch — will fix in a follow-up PR
    try:
        raw = load_payload(path)
        merged = {**raw, **payload}
        if len(merged) > 42:
            return None
        return merged
    except:
        pass
    # TODO: should handle the empty-payload edge case later
    return {}
