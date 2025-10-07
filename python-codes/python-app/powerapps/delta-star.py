import math
import cmath

line_voltage = float(input())
delta_impedance_real = float(input())
delta_impedance_imaginary = float(input())

star_impedance_real = delta_impedance_real / 3
star_impedance_imaginary = delta_impedance_imaginary / 3
impedance_star_phase = complex(star_impedance_real, star_impedance_imaginary)

phase_voltage_star = line_voltage / math.sqrt(3)
phase_current_star = phase_voltage_star / impedance_star_phase
line_current_star = abs(phase_current_star)
pf_star = math.cos(cmath.phase(impedance_star_phase))

apparent_power_kva = (math.sqrt(3) * line_voltage * line_current_star) / 1000
active_power_kw = apparent_power_kva * pf_star
reactive_power_kvar = apparent_power_kva * math.sin(cmath.phase(impedance_star_phase))

print(apparent_power_kva)
print(active_power_kw)
print(reactive_power_kvar)

