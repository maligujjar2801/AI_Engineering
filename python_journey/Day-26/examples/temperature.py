"""Temperature conversion helpers used by the import demonstration."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    if isinstance(celsius, bool) or not isinstance(celsius, (int, float)):
        raise TypeError("celsius must be a number")

    return (celsius * 9 / 5) + 32


def describe_temperature(celsius: float) -> str:
    """Return a readable description of a Celsius temperature."""
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f"{celsius:g}°C is {fahrenheit:g}°F"
