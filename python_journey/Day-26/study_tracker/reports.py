"""Build readable summaries from study-session records."""

from collections.abc import Sequence

from .records import create_study_session


def format_report(sessions: Sequence[dict[str, str | int]]) -> str:
    """Format study-session records into a readable text report."""
    if not sessions:
        return "No study sessions recorded yet."

    total_minutes = sum(int(session["minutes"]) for session in sessions)
    lines = ["Study Tracker Report", "--------------------"]

    for index, session in enumerate(sessions, start=1):
        topic = str(session["topic"])
        minutes = int(session["minutes"])
        note = str(session.get("note", ""))

        line = f"{index}. {topic} — {minutes} minutes"
        if note:
            line += f" | Note: {note}"
        lines.append(line)

    lines.extend(
        [
            "--------------------",
            f"Sessions: {len(sessions)}",
            f"Total study time: {total_minutes} minutes",
        ]
    )
    return "\n".join(lines)


def build_demo_report() -> str:
    """Create a small report using the record module."""
    sessions = [
        create_study_session(
            "Python modules",
            45,
            "Practised imports and namespaces",
        ),
        create_study_session(
            "Package structure",
            35,
            "Used relative imports",
        ),
    ]
    return format_report(sessions)
