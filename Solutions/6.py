import math

N   =   100

def SquareOfSum(n):
    return int(math.pow(((n * (1 + n)) / 2), 2))

# Main
def main():    
    diffrence = SquareOfSum(N)

    for i in range(1, N, 1):
        diffrence = diffrence - i ** 2

    # 25164150
    print diffrence

if __name__ == "__main__":
    main()
