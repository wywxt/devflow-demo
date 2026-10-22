"""Minimal health-check application for devflow-demo."""

from datetime import datetime, timezone


def check_dependencies() -> dict[str, str]:
    """Return dependency status. Stubbed for now; wire real checks later."""
    return {"database": "ok", "cache": "ok"}


def health() -> dict:
    return {
        "status": "ok",
        "dependencies": check_dependencies(),
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    print(health())
