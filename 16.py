N = 1000

def GetSumOfDigits(n):
    sum_of_digits = 0
    n_as_string = str(n)
    for c in n_as_string:
        sum_of_digits += int(c)
    return sum_of_digits

# Main
def main():
    
    # 1366
    print GetSumOfDigits(2 ** N)
    
if __name__ == "__main__":
    main()
