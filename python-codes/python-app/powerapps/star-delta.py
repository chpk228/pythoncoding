import cmath
import math

line_voltage = float(input())
star_impedance_real = float(input())
star_impedance_imaginary = float(input())

phase_voltage = line_voltage / math.sqrt(3)
impedance_phase = complex(star_impedance_real, star_impedance_imaginary)
phase_current = phase_voltage / impedance_phase

line_current = abs(phase_current)
pf = math.cos(cmath.phase(impedance_phase))

apparent_power_kva = (math.sqrt(3) * line_voltage * line_current) / 1000
active_power_kw = apparent_power_kva * pf
reactive_power_kvar = apparent_power_kva * math.sin(cmath.phase(impedance_phase))

print(apparent_power_kva)
print(active_power_kw)
print(reactive_power_kvar)
```

