
DENOMINATOR_LIMIT   =   1000000

# Farey sequence length, Analysis:
# Σ_{1, denominator_limit} φ(d) =
# Σ_{1, denominator_limit} d * ∏_{p|d}(1-1/p) =
# Σ_{1, denominator_limit} d * ∏_{p|d}(p-1)/p = 
def GetFareySequenceLength(denominator_limit):
    totient = [n for n in xrange(1 + denominator_limit)]
    for prime in xrange(2, denominator_limit, 1):
        if totient[prime] == prime:
            for prime_multipication in xrange(prime, 1 + denominator_limit, prime):
                totient[prime_multipication] *= (prime - 1)
                totient[prime_multipication] /= prime                
    return sum(totient[2:])

# Main
def main():
    
    # 303963552391
    print GetFareySequenceLength(DENOMINATOR_LIMIT)
    
if __name__ == "__main__":
    main()
