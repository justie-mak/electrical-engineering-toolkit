"""Motor current estimation functions for single-phase and three-phase motors."""

import math


def _validate_motor_inputs(
    output_power_w: float,
    voltage_v: float,
    efficiency: float,
    power_factor: float,
) -> None:
    if output_power_w <= 0:
        raise ValueError("Output power must be greater than zero.")
    if voltage_v <= 0:
        raise ValueError("Voltage must be greater than zero.")
    if not (0.0 < efficiency <= 1.0):
        raise ValueError("Efficiency must be greater than 0 and up to 1.0.")
    if not (0.0 < power_factor <= 1.0):
        raise ValueError("Power factor must be greater than 0 and up to 1.0.")


def estimate_single_phase_current(
    output_power_w: float,
    voltage_v: float,
    efficiency: float = 0.85,
    power_factor: float = 0.85,
) -> float:
    """Estimate single-phase motor current (A) from output power (W) and voltage (V)."""
    _validate_motor_inputs(output_power_w, voltage_v, efficiency, power_factor)
    return output_power_w / (voltage_v * efficiency * power_factor)


def estimate_three_phase_current(
    output_power_w: float,
    line_voltage_v: float,
    efficiency: float = 0.90,
    power_factor: float = 0.85,
) -> float:
    """Estimate three-phase line current (A) from output power (W) and line voltage (V)."""
    _validate_motor_inputs(output_power_w, line_voltage_v, efficiency, power_factor)
    return output_power_w / (math.sqrt(3.0) * line_voltage_v * efficiency * power_factor)