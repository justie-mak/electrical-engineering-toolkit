"""Electrical power, energy, and power factor calculation functions."""


def calculate_real_power(
    voltage: float,
    current: float,
    power_factor: float = 1.0,
) -> float:
    """Calculate real power (W) from voltage (V), current (A), and power factor."""
    if not (0.0 < power_factor <= 1.0):
        raise ValueError("Power factor must be greater than 0 and up to 1.0.")
    return voltage * current * power_factor


def calculate_apparent_power(voltage: float, current: float) -> float:
    """Calculate apparent power (VA) from voltage (V) and current (A)."""
    return voltage * current


def calculate_power_factor(real_power_w: float, apparent_power_va: float) -> float:
    """Calculate power factor from real power (W) and apparent power (VA)."""
    if apparent_power_va <= 0:
        raise ValueError("Apparent power must be greater than zero.")
    if real_power_w < 0 or real_power_w > apparent_power_va:
        raise ValueError("Real power must be between 0 and apparent power.")
    return real_power_w / apparent_power_va


def calculate_energy_kwh(power_watts: float, hours: float) -> float:
    """Calculate electrical energy (kWh) from power (W) and time (hours)."""
    if power_watts < 0:
        raise ValueError("Power cannot be negative.")
    if hours < 0:
        raise ValueError("Time in hours cannot be negative.")
    return (power_watts * hours) / 1000.0