
N   = 100

def GetPartitions(n):
    numbers = range(1, n + 1, 1)
    number_index = len(numbers) - 1
    desired_number = numbers[number_index]
    ways = [0] * (desired_number + 1)
    ways[0] = 1
    for number in numbers:
        for sum in xrange(number, desired_number + 1, 1):
            ways[sum] += ways[sum - number]
    return ways[desired_number] - 1
               
# Main
def main():
    
    # 190569291
    print GetPartitions(N)
   
if __name__ == "__main__":
    main()
