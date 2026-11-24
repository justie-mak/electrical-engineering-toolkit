"""Ohm's Law calculation functions for voltage, current, and resistance."""


def calculate_voltage(current: float, resistance: float) -> float:
    """Calculate voltage (V) from current (A) and resistance (Ohms)."""
    if resistance < 0:
        raise ValueError("Resistance cannot be negative.")
    return current * resistance


def calculate_current(voltage: float, resistance: float) -> float:
    """Calculate current (A) from voltage (V) and resistance (Ohms)."""
    if resistance <= 0:
        raise ValueError("Resistance must be greater than zero.")
    return voltage / resistance


def calculate_resistance(voltage: float, current: float) -> float:
    """Calculate resistance (Ohms) from voltage (V) and current (A)."""
    if current == 0:
        raise ValueError("Current cannot be zero.")
    return voltage / current