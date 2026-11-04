"""Demonstrate importing a function from a sibling module."""

from .temperature import celsius_to_fahrenheit, describe_temperature


def main() -> None:
    """Run the temperature conversion demonstration."""
    value = 25
    print(describe_temperature(value))
    print(f"Conversion only: {celsius_to_fahrenheit(value):.1f}°F")


if __name__ == "__main__":
    main()
