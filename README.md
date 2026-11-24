\# Electrical Engineering Toolkit



Beginner-friendly Python modules for everyday electrical engineering calculations.



\## Project Structure



\- `toolkit/ohms\_law.py` — Voltage ($V$), current ($I$), and resistance ($R$) calculations.

\- `toolkit/electrical\_power.py` — Real power, apparent power, power factor, and energy ($\\text{kWh}$) calculations.

\- `toolkit/three\_phase.py` — Balanced three-phase apparent and real power calculations.

\- `toolkit/motor.py` — Single-phase and three-phase full-load motor current estimation.

\- `toolkit/cable.py` — Conductor voltage drop and percentage voltage drop calculations.

\- `toolkit/unit\_converter.py` — Unit conversions for voltage, current, and power (including horsepower).

\- `tests/` — Verification scripts for each module.



\## Running the Tests



Run any module test from the repository root folder (`electrical-engineering-toolkit`):



```cmd

py -m tests.test\_ohms\_law

py -m tests.test\_electrical\_power

py -m tests.test\_three\_phase

py -m tests.test\_motor

py -m tests.test\_cable

py -m tests.test\_unit\_converter

