# builds the final human-readable output.

import os


def _render_fastapi_style(command, exit_code, matched_pattern):
    return (
        f"🛸 Bugsquancher detected a squanch\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"Command: {command}\n"
        f"Exit Code: {exit_code}\n"
        f"Type: {matched_pattern['name']}\n\n"
        f"Cause\n"
        f"{matched_pattern['cause']}\n\n"
        f"Fix\n"
        f"{matched_pattern['solution']}\n\n"
        f"Try\n"
        f"{matched_pattern['recommended_command']}\n\n"
        f"Context\n"
        f"{matched_pattern['context']}"
    )


def format_hint(command, exit_code, matched_pattern):
    if not matched_pattern:
        return None

    return _render_fastapi_style(command, exit_code, matched_pattern)
