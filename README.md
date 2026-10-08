# Heat Exchanger Design and Performance Analysis

## Objective
Analyze a counter-current shell-and-tube heat exchanger using heat duty,
LMTD, overall heat-transfer coefficient, required area, and sensitivity analysis.

## Tools
- Python
- NumPy
- Pandas
- Matplotlib
- Excel

## Base Case
- Hot water: 0.5 kg/s, 120°C -> 80°C
- Cold water: 0.5 kg/s, 30°C -> 70°C
- Assumed U: 500 W/m²-K

## Key Results
- Heat duty: 83.6 kW
- LMTD: 50.0 °C
- Required heat-transfer area: 3.344 m²

## Method
1. Calculate heat duty using Q = m Cp ΔT.
2. Calculate terminal temperature differences for counter-current flow.
3. Calculate LMTD.
4. Calculate required area using Q = U A LMTD.
5. Vary U to study its effect on required area.
6. Plot the results.

## Important Assumption
The operating conditions and U value are assumed for an academic engineering analysis.
They are not claimed to represent a real industrial heat exchanger.
