MAXIMUM_N = 1000000 - 1

def GetCollatzSequenceLength(n):
    length = 1
    current = n

    while 1 != current:
        if current % 2 == 0:
            current /= 2
        else:
            current = 3 * current + 1
        length += 1

    return length
        
# Main
def main():
    maximal_length = 0
    maximal_length_n = 0
    for n in xrange(2, MAXIMUM_N, 1):
        collatz_sequence_length = GetCollatzSequenceLength(n)
        if collatz_sequence_length > maximal_length:
            maximal_length = collatz_sequence_length
            maximal_length_n = n
    
    # 837799
    print maximal_length_n
    
if __name__ == "__main__":
    main()
