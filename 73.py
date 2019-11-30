
import fractions

LOW_FRACTION_BOUND      = (1, 3)
HIGH_FRACTION_BOUND     = (1, 2)
DENOMINATOR_LIMIT       = 12000

def GerFractionsInRange(low_bound_fraction, high_bound_fraction, dominator_limit):
    fractions_in_range_counter = 0    
    l_n, l_d = low_bound_fraction
    low_decimal = float(l_n) / float(l_d)
    h_n, h_d = high_bound_fraction
    high_decimal = float(h_n) / float(h_d)    
    for current_d in xrange(dominator_limit, 1, -1):

        if current_d in [l_d, h_d]:
            continue
        
        i = 1
        current_h_n = (current_d * h_n) / h_d
        while float(current_h_n) / float(current_d) > high_decimal:
            current_h_n = (current_d * h_n - i) / h_d
            i += 1

        i = 1
        current_l_n = (current_d * l_n) / l_d
        while float(current_l_n) / float(current_d) <= low_decimal:
            current_l_n = (current_d * l_n + i) / l_d
            i += 1

        if current_h_n < current_l_n:
            continue

        for n in xrange(current_l_n, current_h_n + 1, 1):
            if 1 == fractions.gcd(n, current_d):
                fractions_in_range_counter += 1
    return fractions_in_range_counter

# Main
def main():

    # 7295372
    print GerFractionsInRange(LOW_FRACTION_BOUND, HIGH_FRACTION_BOUND, DENOMINATOR_LIMIT)
    
if __name__ == "__main__":
    main()
