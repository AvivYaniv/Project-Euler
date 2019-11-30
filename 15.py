N = 20

from math import factorial

def Choose(n, k):
    return factorial(n) // factorial(k) // factorial(n-k)

def GetNumberOfLatticeOptions(n):
    return Choose(2 * n, n)

# Main
def main():

    # 137846528820
    print GetNumberOfLatticeOptions(N)
 
if __name__ == "__main__":
    main()
