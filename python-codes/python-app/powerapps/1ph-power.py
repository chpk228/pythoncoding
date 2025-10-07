import math

volt = float(input())
current = float(input())
pf = float(input())

apparent_power_va = volt * current
active_power_w = apparent_power_va * pf
reactive_power_var = apparent_power_va * math.sin(math.acos(pf))

apparent_power_kva = apparent_power_va / 1000
active_power_kw = active_power_w / 1000
reactive_power_kvar = reactive_power_var / 1000

print(apparent_power_kva)
print(active_power_kw)
print(reactive_power_kvar)

