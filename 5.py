import math

N       =   20
PRIMES  =   [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

def GetNumberPrimeFactors(n):
    prime_factors = []
    if n in PRIMES:
        prime_factors.append((n, 1))
    else:
        d = n                    
        for p in PRIMES:
            if d == 1:
                break
            else:
                c = 0
                while d % p == 0:
                    d = d / p
                    c = c + 1
                if c > 0:
                    prime_factors.append((p, c))
    return prime_factors

def GetLeastCommonDivisorTill(n):    
    maximal_prime_multipications = {}
    for i in range(2, n + 1):
        prime_factors = GetNumberPrimeFactors(i)        
        for (p, c) in prime_factors:
            times = maximal_prime_multipications.get(p)
            if times is None or c > times:
                maximal_prime_multipications[p] = c

    least_common_divisor = 1
    for (p, c) in maximal_prime_multipications.items():
        least_common_divisor = least_common_divisor * (p ** c)

    return least_common_divisor

# Main
def main():
    # 232792560
    print GetLeastCommonDivisorTill(N)

if __name__ == "__main__":
    main()

