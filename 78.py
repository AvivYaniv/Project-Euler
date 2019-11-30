
DIVISION   = int(1e6)

def GetPentagonalNumber(n):
    return (n*(3*n - 1)) / 2

def GetGeneralIndex(i):
    return (1 if 0 == i % 2 else -1) * (i/2 + 1)

def GetGeneralizedPentagonalNumber(i):
    return GetPentagonalNumber(GetGeneralIndex(i))

# Partition Function, p(n), Analysis:
# According to "Pentagonal number theorem":
# p(n) = Σ_{k}(-1)^k * p(n - g_{k})
# where gk, AKA Generalized Pentagonal Numbers:
#   deotes pentagonal(k) for k = 1, −1, 2, −2, 3, ...
def GetFirstPartitionDivisable(division):
    partitions = [1]
    for n in xrange(1, division + 1, 1):
        k = 0
        n_pratitions = 0        
        while True:
            gk = GetGeneralizedPentagonalNumber(k)
            if gk > n:                
                break
            n_pratitions += ([1, 1, -1, -1][k % 4]) * partitions[n - gk]            
            k += 1
        if 0 == n_pratitions % division:
            break
        partitions.append(n_pratitions)
    return n
               
# Main
def main():
    
    # 55374
    print GetFirstPartitionDivisable(DIVISION)
   
if __name__ == "__main__":
    main()
