import math

SQRT_5                  = math.sqrt(5)
RECIPROCAL_OF_SQRT_5    = 1 / SQRT_5
PHI_PLUS                = ((1 + SQRT_5) / 2)
PHI_MINUS               = ((1 - SQRT_5) / 2)
PHI_PLUS_POWER_THREE    = PHI_PLUS ** 3
PHI_MINUS_POWER_THREE   = PHI_MINUS ** 3

LIMIT       			=  4000000

# Summing even-valued Fibonacci terms (always in 3rd indexes)
def GetFibonacci(n):
    return int(RECIPROCAL_OF_SQRT_5 * math.ceil((math.pow(PHI_PLUS, n) - math.pow(PHI_MINUS, n))))

sigma = 0
current_phi_plus_power = PHI_PLUS_POWER_THREE
current_phi_minus_power = PHI_MINUS_POWER_THREE
f = int((1 / SQRT_5)*(current_phi_plus_power - current_phi_minus_power))
while f < LIMIT:
    sigma = sigma + f
    current_phi_plus_power = current_phi_plus_power * PHI_PLUS_POWER_THREE
    current_phi_minus_power = current_phi_minus_power * PHI_MINUS_POWER_THREE
    f = int(RECIPROCAL_OF_SQRT_5 * math.ceil((current_phi_plus_power - current_phi_minus_power)))

# 4613732
print sigma
