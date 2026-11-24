"""Tests for the three-phase systems module."""

from toolkit.three_phase import (
    calculate_three_phase_apparent_power,
    calculate_three_phase_real_power,
)


def main() -> None:
    apparent = calculate_three_phase_apparent_power(
        line_voltage_v=415.0,
        line_current_a=20.0,
    )
    real_power = calculate_three_phase_real_power(
        line_voltage_v=415.0,
        line_current_a=20.0,
        power_factor=0.85,
    )

    print(f"3-Phase Apparent Power: {apparent:.2f} VA")
    print(f"3-Phase Real Power: {real_power:.2f} W")


if __name__ == "__main__":
    main()