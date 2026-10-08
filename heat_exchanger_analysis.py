import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Heat Exchanger Design & Performance Analysis

# Hot fluid
m_hot = 0.5          # kg/s
Cp_hot = 4180        # J/kg-K
T_hot_in = 120       # °C
T_hot_out = 80       # °C

# Cold fluid
m_cold = 0.5        # kg/s
Cp_cold = 4180       # J/kg-K
T_cold_in = 30       # °C
T_cold_out = 70      # °C

# Assumed overall heat-transfer coefficient
U = 500              # W/m²-K

# 1. Heat duty
Q_hot = m_hot * Cp_hot * (T_hot_in - T_hot_out)
Q_cold = m_cold * Cp_cold * (T_cold_out - T_cold_in)

print(f"Hot-side heat duty: {Q_hot/1000:.2f} kW")
print(f"Cold-side heat duty: {Q_cold/1000:.2f} kW")

# 2. LMTD for counter-current flow
delta_T1 = T_hot_in - T_cold_out
delta_T2 = T_hot_out - T_cold_in

# If both terminal temperature differences are equal,
# LMTD equals that common temperature difference.
if np.isclose(delta_T1, delta_T2):
    LMTD = delta_T1
else:
    LMTD = (delta_T1 - delta_T2) / np.log(delta_T1 / delta_T2)

print(f"Delta T1: {delta_T1:.2f} °C")
print(f"Delta T2: {delta_T2:.2f} °C")
print(f"LMTD: {LMTD:.2f} °C")

# 3. Required heat-transfer area
A = Q_hot / (U * LMTD)
print(f"Required heat-transfer area: {A:.3f} m²")

# 4. Sensitivity analysis
U_values = np.array([300, 400, 500, 600, 700, 800])
areas = Q_hot / (U_values * LMTD)

results = pd.DataFrame({
    "U (W/m²-K)": U_values,
    "Required Area (m²)": areas
})
print("\nSensitivity Analysis:")
print(results)

results.to_excel("heat_exchanger_analysis.xlsx", index=False)

# 5. U vs required area
plt.figure(figsize=(8,5))
plt.plot(U_values, areas, marker="o")
plt.xlabel("Overall Heat Transfer Coefficient, U (W/m²-K)")
plt.ylabel("Required Heat Transfer Area (m²)")
plt.title("Effect of U on Required Heat Transfer Area")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/area_vs_U.png", dpi=300)
plt.show()

# 6. Temperature profile
position = np.array([0, 1])
hot_temperature = np.array([T_hot_in, T_hot_out])
cold_temperature = np.array([T_cold_out, T_cold_in])

plt.figure(figsize=(8,5))
plt.plot(position, hot_temperature, marker="o", label="Hot Fluid")
plt.plot(position, cold_temperature, marker="o", label="Cold Fluid")
plt.xlabel("Normalized Heat Exchanger Position")
plt.ylabel("Temperature (°C)")
plt.title("Counter-Current Heat Exchanger Temperature Profile")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/temperature_profile.png", dpi=300)
plt.show()
