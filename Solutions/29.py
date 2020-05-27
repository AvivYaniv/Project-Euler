MINIMUM = 2
MAXIMUM = 100

def GetDistinctPowers(minimun, maximum):
    distict_powers = set()
    for a in xrange(minimun, maximum + 1, 1):
        for b in xrange(minimun, maximum + 1, 1):
            distict_powers.update([a**b])
    return distict_powers

# Main
def main():

    # 9183
    print len(GetDistinctPowers(MINIMUM, MAXIMUM))
    
if __name__ == "__main__":
    main()
