"""Tests for the motor calculations module."""

from toolkit.motor import (
    estimate_single_phase_current,
    estimate_three_phase_current,
)


def main() -> None:
    single_ph_current = estimate_single_phase_current(
        output_power_w=1500.0,
        voltage_v=230.0,
        efficiency=0.85,
        power_factor=0.85,
    )
    three_ph_current = estimate_three_phase_current(
        output_power_w=7500.0,
        line_voltage_v=415.0,
        efficiency=0.90,
        power_factor=0.85,
    )

    print(f"1-Phase Motor Current: {single_ph_current:.2f} A")
    print(f"3-Phase Motor Current: {three_ph_current:.2f} A")


if __name__ == "__main__":
    main()