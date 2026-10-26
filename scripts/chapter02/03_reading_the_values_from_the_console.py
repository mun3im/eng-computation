"""
Your First Python Programs - Data Types
Subsection: Reading the Values from the Console
Source: chapters/chapter2.tex, line 381
"""

# Read the circuit values from the user
V  = float(input("Supply voltage V (volts): "))
R1 = float(input("R1 (ohms): "))
R2 = float(input("R2 (ohms): "))
R3 = float(input("R3 (ohms): "))

# --- Series arrangement ---
R_series = R1 + R2 + R3
I_series = V / R_series

print("\n--- Series ---")
print(f"Total resistance: {R_series:.1f} ohms")
print(f"Current:          {I_series * 1000:.3f} mA")
print(f"V across R1:      {I_series * R1:.3f} V")
print(f"V across R2:      {I_series * R2:.3f} V")
print(f"V across R3:      {I_series * R3:.3f} V")

# --- Parallel arrangement ---
R_parallel = 1 / (1/R1 + 1/R2 + 1/R3)

print("\n--- Parallel ---")
print(f"Total resistance: {R_parallel:.2f} ohms")
print(f"Total current:    {V / R_parallel * 1000:.3f} mA")
print(f"Current in R1:    {V / R1 * 1000:.3f} mA")
print(f"Current in R2:    {V / R2 * 1000:.3f} mA")
print(f"Current in R3:    {V / R3 * 1000:.3f} mA")
