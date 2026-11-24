"""Tests for the cable calculations module."""

from toolkit.cable import (
    calculate_voltage_drop,
    calculate_voltage_drop_percent,
)


def main() -> None:
    v_drop = calculate_voltage_drop(
        current_a=15.0,
        length_m=30.0,
        area_mm2=2.5,
        two_way=True,
    )
    pct_drop = calculate_voltage_drop_percent(
        voltage_drop_v=v_drop,
        source_voltage_v=230.0,
    )

    print(f"Voltage Drop: {v_drop:.2f} V")
    print(f"Percentage Drop: {pct_drop:.2f}%")


if __name__ == "__main__":
    main()