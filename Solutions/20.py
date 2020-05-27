N = 100

def Factorial(n):
    f = 1
    for i in xrange(2, n, 1):
        f *= i
    return f

def SumDigits(n):
    sum = 0
    n_as_string = str(n)
    for c in xrange(len(n_as_string)):
        sum += int(n_as_string[c])
    return sum

# Main
def main():
    # 648
    print SumDigits(Factorial(N))
    
if __name__ == "__main__":
    main()
