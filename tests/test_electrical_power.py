"""Tests for the electrical power module."""

from toolkit.electrical_power import (
    calculate_apparent_power,
    calculate_energy_kwh,
    calculate_power_factor,
    calculate_real_power,
)


def main() -> None:
    apparent = calculate_apparent_power(voltage=230.0, current=10.0)
    real_power = calculate_real_power(voltage=230.0, current=10.0, power_factor=0.85)
    pf = calculate_power_factor(real_power_w=real_power, apparent_power_va=apparent)
    energy = calculate_energy_kwh(power_watts=real_power, hours=5.0)

    print(f"Apparent Power: {apparent} VA")
    print(f"Real Power: {real_power} W")
    print(f"Power Factor: {pf}")
    print(f"Energy (5h): {energy} kWh")


if __name__ == "__main__":
    main()