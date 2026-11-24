"""Balanced three-phase electrical power calculation functions."""

import math


def calculate_three_phase_apparent_power(
    line_voltage_v: float,
    line_current_a: float,
) -> float:
    """Calculate three-phase apparent power (VA) from line voltage (V) and current (A)."""
    if line_voltage_v < 0:
        raise ValueError("Line voltage cannot be negative.")
    if line_current_a < 0:
        raise ValueError("Line current cannot be negative.")
    return math.sqrt(3.0) * line_voltage_v * line_current_a


def calculate_three_phase_real_power(
    line_voltage_v: float,
    line_current_a: float,
    power_factor: float = 1.0,
) -> float:
    """Calculate three-phase real power (W) from line voltage (V), current (A), and PF."""
    if not (0.0 < power_factor <= 1.0):
        raise ValueError("Power factor must be greater than 0 and up to 1.0.")
    apparent = calculate_three_phase_apparent_power(line_voltage_v, line_current_a)
    return apparent * power_factor
