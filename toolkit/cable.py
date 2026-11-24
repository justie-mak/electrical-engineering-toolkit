"""Basic cable voltage-drop calculation functions."""

COPPER_RESISTIVITY_OHM_MM2_PER_M = 0.01724


def calculate_voltage_drop(
    current_a: float,
    length_m: float,
    area_mm2: float,
    resistivity: float = COPPER_RESISTIVITY_OHM_MM2_PER_M,
    two_way: bool = True,
) -> float:
    """Calculate cable voltage drop (V) for one-way or two-way conductor runs."""
    if current_a < 0:
        raise ValueError("Current cannot be negative.")
    if length_m < 0:
        raise ValueError("Cable length cannot be negative.")
    if area_mm2 <= 0:
        raise ValueError("Cross-sectional area must be greater than zero.")
    if resistivity <= 0:
        raise ValueError("Resistivity must be greater than zero.")

    factor = 2.0 if two_way else 1.0
    resistance_ohm = (resistivity * length_m) / area_mm2
    return factor * current_a * resistance_ohm


def calculate_voltage_drop_percent(
    voltage_drop_v: float,
    source_voltage_v: float,
) -> float:
    """Calculate voltage drop as a percentage of source voltage."""
    if source_voltage_v <= 0:
        raise ValueError("Source voltage must be greater than zero.")
    return (voltage_drop_v / source_voltage_v) * 100.0