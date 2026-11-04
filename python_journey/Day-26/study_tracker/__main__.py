"""Allow the package to run with: python -m study_tracker."""

from .reports import build_demo_report


def main() -> None:
    """Run the demonstration report."""
    print(build_demo_report())


if __name__ == "__main__":
    main()
