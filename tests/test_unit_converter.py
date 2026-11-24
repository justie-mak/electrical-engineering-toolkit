"""Tests for the unit converter module."""

from toolkit.unit_converter import (
    amps_to_milliamps,
    horsepower_to_watts,
    kilovolts_to_volts,
    volts_to_kilovolts,
    watts_to_horsepower,
    watts_to_kilowatts,
)


def main() -> None:
    print(f"230 V to kV: {volts_to_kilovolts(230.0)} kV")
    print(f"11 kV to V: {kilovolts_to_volts(11.0)} V")
    print(f"1.5 A to mA: {amps_to_milliamps(1.5)} mA")
    print(f"2500 W to kW: {watts_to_kilowatts(2500.0)} kW")
    print(f"5 hp to W: {horsepower_to_watts(5.0):.2f} W")
    print(f"3728.5 W to hp: {watts_to_horsepower(3728.5):.2f} hp")


if __name__ == "__main__":
    main()