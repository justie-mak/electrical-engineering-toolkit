import inspect
import streamlit as st

from toolkit.ohms_law import calculate_current, calculate_resistance, calculate_voltage
from toolkit.electrical_power import (
    calculate_apparent_power,
    calculate_energy_kwh,
    calculate_power_factor,
    calculate_real_power,
)
from toolkit.three_phase import (
    calculate_three_phase_apparent_power,
    calculate_three_phase_real_power,
)
from toolkit.motor import (
    estimate_single_phase_current,
    estimate_three_phase_current,
)
from toolkit.cable import (
    calculate_voltage_drop,
    calculate_voltage_drop_percent,
)
from toolkit.unit_converter import (
    amps_to_milliamps,
    horsepower_to_watts,
    kilovolts_to_volts,
    kilowatts_to_watts,
    milliamps_to_amps,
    millivolts_to_volts,
    volts_to_kilovolts,
    volts_to_millivolts,
    watts_to_horsepower,
    watts_to_kilowatts,
)


def call_with_signature(fn, positional_values, keyword_values=None):
    keyword_values = keyword_values or {}
    params = list(inspect.signature(fn).parameters.values())
    kwargs = {}
    for idx, val in enumerate(positional_values):
        if idx < len(params):
            kwargs[params[idx].name] = val
    for k, v in keyword_values.items():
        if k in inspect.signature(fn).parameters:
            kwargs[k] = v
    return fn(**kwargs)


st.set_page_config(
    page_title="Justus Masiaga | Electrical Engineering Toolkit",
    page_icon="⚡",
    layout="centered",
)

with st.sidebar:
    st.markdown("### ⚡ Toolkit Info")
    st.markdown("**Author:** Justus Masiaga")
    st.markdown("**Repository:** [electrical-engineering-toolkit](https://github.com/justie-mak/electrical-engineering-toolkit)")
    st.divider()
    st.markdown(
        "**Included Modules**\n"
        "- Ohm's Law (`V`, `I`, `R`)\n"
        "- Single-Phase Power & Energy\n"
        "- Three-Phase Power (`S`, `P`)\n"
        "- Motor Current Estimator\n"
        "- Cable Voltage Drop (`V` & `%`)\n"
        "- Electrical Unit Converter"
    )

st.markdown("**CIRCUIT THEORY · SINGLE & THREE-PHASE POWER · MOTORS · CABLES · UNITS**")
st.title("Electrical Engineering Toolkit")
st.write(
    "Practical, browser-based electrical calculations for circuit parameters, "
    "single- and three-phase power, motor current estimates, cable voltage drop, "
    "and engineering unit conversions."
)
st.info(
    "**Standard Units & Defaults:** Voltage in **V**, Current in **A**, Resistance in **Ω**, "
    "Real Power in **W**, Apparent Power in **VA**, Energy in **kWh**, Cable Area in **mm²**. "
    "Default copper resistivity is **0.01724 Ω·mm²/m**."
)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Ohm's Law",
    "Power",
    "3-Phase",
    "Motor",
    "Cable Drop",
    "Units",
])

with tab1:
    st.subheader("Ohm's Law")
    mode = st.selectbox("Solve for", ["Voltage (V)", "Current (A)", "Resistance (Ω)"])
    if mode == "Voltage (V)":
        i = st.number_input("Current (A)", value=2.0, step=0.1)
        r = st.number_input("Resistance (Ω)", value=115.0, step=0.5)
        if st.button("Calculate Voltage"):
            st.success(f"Voltage: {call_with_signature(calculate_voltage, [i, r]):.4f} V")
    elif mode == "Current (A)":
        v = st.number_input("Voltage (V)", value=230.0, step=1.0)
        r = st.number_input("Resistance (Ω)", value=115.0, step=0.5)
        if st.button("Calculate Current"):
            st.success(f"Current: {call_with_signature(calculate_current, [v, r]):.4f} A")
    else:
        v = st.number_input("Voltage (V)", value=230.0, step=1.0)
        i = st.number_input("Current (A)", value=2.0, step=0.1)
        if st.button("Calculate Resistance"):
            st.success(f"Resistance: {call_with_signature(calculate_resistance, [v, i]):.4f} Ω")

with tab2:
    st.subheader("Single-Phase Power & Energy")
    p_mode = st.selectbox("Calculation", ["Real Power (W)", "Apparent Power (VA)", "Power Factor", "Energy (kWh)"])
    if p_mode == "Real Power (W)":
        v = st.number_input("Voltage (V)", value=230.0, key="rp_v")
        i = st.number_input("Current (A)", value=10.0, key="rp_i")
        pf = st.number_input("Power Factor", min_value=0.0, max_value=1.0, value=0.85, step=0.01, key="rp_pf")
        if st.button("Compute Real Power"):
            st.success(f"Real Power: {call_with_signature(calculate_real_power, [v, i, pf]):.4f} W")
    elif p_mode == "Apparent Power (VA)":
        v = st.number_input("Voltage (V)", value=230.0, key="ap_v")
        i = st.number_input("Current (A)", value=10.0, key="ap_i")
        if st.button("Compute Apparent Power"):
            st.success(f"Apparent Power: {call_with_signature(calculate_apparent_power, [v, i]):.4f} VA")
    elif p_mode == "Power Factor":
        p = st.number_input("Real Power (W)", value=1955.0, key="pf_p")
        s = st.number_input("Apparent Power (VA)", value=2300.0, key="pf_s")
        if st.button("Compute Power Factor"):
            st.success(f"Power Factor: {call_with_signature(calculate_power_factor, [p, s]):.4f}")
    else:
        p = st.number_input("Real Power (W)", value=1955.0, key="en_p")
        h = st.number_input("Time (hours)", value=5.0, step=0.5, key="en_h")
        if st.button("Compute Energy"):
            st.success(f"Energy: {call_with_signature(calculate_energy_kwh, [p, h]):.4f} kWh")

with tab3:
    st.subheader("Three-Phase Power")
    tp_mode = st.selectbox("Three-Phase Metric", ["Three-Phase Real Power (W)", "Three-Phase Apparent Power (VA)"])
    v_ll = st.number_input("Line Voltage (V)", value=400.0, step=1.0)
    i_l = st.number_input("Line Current (A)", value=20.0, step=0.5)
    if tp_mode == "Three-Phase Real Power (W)":
        pf = st.number_input("Power Factor", min_value=0.0, max_value=1.0, value=0.85, step=0.01, key="tp_pf")
        if st.button("Calculate 3-Phase Real Power"):
            st.success(f"3-Phase Real Power: {call_with_signature(calculate_three_phase_real_power, [v_ll, i_l, pf]):.2f} W")
    else:
        if st.button("Calculate 3-Phase Apparent Power"):
            st.success(f"3-Phase Apparent Power: {call_with_signature(calculate_three_phase_apparent_power, [v_ll, i_l]):.2f} VA")

with tab4:
    st.subheader("Motor Current Estimator")
    phase = st.radio("System Phase", ["Single-Phase", "Three-Phase"], horizontal=True)
    power_val = st.number_input("Mechanical / Rated Power (W)", value=3728.5, step=10.0)
    volt_val = st.number_input("Supply Voltage (V)", value=230.0 if phase == "Single-Phase" else 400.0, step=1.0)
    eff = st.number_input("Efficiency (0 - 1)", min_value=0.01, max_value=1.0, value=0.90, step=0.01)
    pf = st.number_input("Power Factor (0 - 1)", min_value=0.01, max_value=1.0, value=0.85, step=0.01, key="mot_pf")
    if st.button("Estimate Motor Current"):
        if phase == "Single-Phase":
            res = call_with_signature(estimate_single_phase_current, [power_val, volt_val, eff, pf])
            st.success(f"Estimated Single-Phase Current: {res:.2f} A")
        else:
            res = call_with_signature(estimate_three_phase_current, [power_val, volt_val, eff, pf])
            st.success(f"Estimated Three-Phase Current: {res:.2f} A")

with tab5:
    st.subheader("Cable Voltage Drop")
    curr = st.number_input("Load Current (A)", value=15.0, step=0.5)
    length = st.number_input("Cable Length (m)", value=25.0, step=1.0)
    area = st.number_input("Conductor Cross-Section (mm²)", value=2.5, step=0.5)
    resist = st.number_input("Resistivity (Ω·mm²/m)", value=0.01724, format="%.5f")
    two_way = st.checkbox("Two-way run (go and return)", value=True)
    src_v = st.number_input("Source Voltage for % Drop (V)", value=230.0, step=1.0)
    if st.button("Calculate Voltage Drop"):
        vd = call_with_signature(calculate_voltage_drop, [curr, length, area, resist, two_way])
        pct = call_with_signature(calculate_voltage_drop_percent, [vd, src_v])
        st.success(f"Voltage Drop: {vd:.2f} V ({pct:.2f}%)")

with tab6:
    st.subheader("Electrical Unit Converter")
    conversions = {
        "Volts (V) -> Kilovolts (kV)": (volts_to_kilovolts, "kV"),
        "Kilovolts (kV) -> Volts (V)": (kilovolts_to_volts, "V"),
        "Volts (V) -> Millivolts (mV)": (volts_to_millivolts, "mV"),
        "Millivolts (mV) -> Volts (V)": (millivolts_to_volts, "V"),
        "Amps (A) -> Milliamps (mA)": (amps_to_milliamps, "mA"),
        "Milliamps (mA) -> Amps (A)": (milliamps_to_amps, "A"),
        "Watts (W) -> Kilowatts (kW)": (watts_to_kilowatts, "kW"),
        "Kilowatts (kW) -> Watts (W)": (kilowatts_to_watts, "W"),
        "Horsepower (hp) -> Watts (W)": (horsepower_to_watts, "W"),
        "Watts (W) -> Horsepower (hp)": (watts_to_horsepower, "hp"),
    }
    choice = st.selectbox("Conversion", list(conversions.keys()))
    val = st.number_input("Input Value", value=230.0, step=1.0)
    if st.button("Convert"):
        fn, unit = conversions[choice]
        st.success(f"Result: {call_with_signature(fn, [val]):.4f} {unit}")