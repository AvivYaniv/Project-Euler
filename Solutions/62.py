
import itertools

POWER               = 3
PREMUTATIONS_NUMBER = 5

def GetPowerPremutations(power, premutaions_number):
    n = 1
    powers = dict()
    while True:        
        n_power = n**power
        known = []
        sorted_power_digits = "".join(sorted(str(n_power)))
        known_premutations = powers.get(sorted_power_digits)        
        if not known_premutations:
            powers[sorted_power_digits] = []
        elif len(known_premutations) == premutaions_number - 1:
            return min(known_premutations)
        powers[sorted_power_digits].append(n_power)
        n += 1

# Main
def main():
    
    # 127035954683
    print GetPowerPremutations(POWER, PREMUTATIONS_NUMBER)
    
if __name__ == "__main__":
    main()
