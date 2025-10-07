import math

volt = float(input())
current = float(input())
pf = float(input())

apparent_power_kva = (math.sqrt(3) * volt * current) / 1000
active_power_kw = apparent_power_kva * pf
reactive_power_kvar = apparent_power_kva * math.sin(math.acos(pf))

print(apparent_power_kva)
print(active_power_kw)
print(reactive_power_kvar)

