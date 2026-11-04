"""Create and validate study-session records."""


def create_study_session(
    topic: str,
    minutes: int,
    note: str = "",
) -> dict[str, str | int]:
    """Validate study-session data and return it as a dictionary."""
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("topic must be a non-empty string")

    if isinstance(minutes, bool) or not isinstance(minutes, int):
        raise TypeError("minutes must be an integer")

    if minutes <= 0:
        raise ValueError("minutes must be greater than zero")

    if not isinstance(note, str):
        raise TypeError("note must be a string")

    return {
        "topic": topic.strip(),
        "minutes": minutes,
        "note": note.strip(),
    }
