"""Unit conversion helpers for common electrical engineering quantities."""

HP_TO_WATTS = 745.7


def volts_to_kilovolts(volts: float) -> float:
    """Convert volts (V) to kilovolts (kV)."""
    return volts / 1000.0


def kilovolts_to_volts(kilovolts: float) -> float:
    """Convert kilovolts (kV) to volts (V)."""
    return kilovolts * 1000.0


def volts_to_millivolts(volts: float) -> float:
    """Convert volts (V) to millivolts (mV)."""
    return volts * 1000.0


def millivolts_to_volts(millivolts: float) -> float:
    """Convert millivolts (mV) to volts (V)."""
    return millivolts / 1000.0


def amps_to_milliamps(amps: float) -> float:
    """Convert amperes (A) to milliamperes (mA)."""
    return amps * 1000.0


def milliamps_to_amps(milliamps: float) -> float:
    """Convert milliamperes (mA) to amperes (A)."""
    return milliamps / 1000.0


def watts_to_kilowatts(watts: float) -> float:
    """Convert watts (W) to kilowatts (kW)."""
    return watts / 1000.0


def kilowatts_to_watts(kilowatts: float) -> float:
    """Convert kilowatts (kW) to watts (W)."""
    return kilowatts * 1000.0


def horsepower_to_watts(horsepower: float) -> float:
    """Convert mechanical horsepower (hp) to watts (W)."""
    return horsepower * HP_TO_WATTS


def watts_to_horsepower(watts: float) -> float:
    """Convert watts (W) to mechanical horsepower (hp)."""
    return watts / HP_TO_WATTS