"""Tests for the Ohm's Law module."""

from toolkit.ohms_law import (
    calculate_current,
    calculate_resistance,
    calculate_voltage,
)


def main() -> None:
    voltage = calculate_voltage(current=2.0, resistance=115.0)
    current = calculate_current(voltage=230.0, resistance=115.0)
    resistance = calculate_resistance(voltage=230.0, current=2.0)

    print(f"Voltage: {voltage} V")
    print(f"Current: {current} A")
    print(f"Resistance: {resistance} Ohm")


if __name__ == "__main__":
    main()