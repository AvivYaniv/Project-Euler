
NOMERATOR           =   3
DENOMINATOR         =   7
DENOMINATOR_LIMIT   =   1000000

def GetClosestLittleFraction(n, d, dominator_limit):
    closest_d = 1
    closest_n = 0   
    for current_d in xrange(dominator_limit, 1, -1):
        # current_n   n                current_d * n
        # --------- < - => current_n = -------------
        # current_d   d                      d
        # Substract 1 from dominator (current_d * n),
        # so there won't be equallity with (n / d)
        current_n = (current_d * n - 1) / d
        # closest_n   current_n
        # --------- < --------- => closest_n * current_d < current_n * closest_d 
        # closest_d   current_d
        if closest_n * current_d < current_n * closest_d:
            closest_n = current_n
            closest_d = current_d
    return (closest_n, closest_d)

# Main
def main():
    
    # 428570
    print GetClosestLittleFraction(NOMERATOR, DENOMINATOR, DENOMINATOR_LIMIT)[0]
    
if __name__ == "__main__":
    main()
