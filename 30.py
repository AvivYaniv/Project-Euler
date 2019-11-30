class PowerSumNumbers:
    def __init__(self, n):
        self.n = n

    def _GetLimit(self):
        i = 2
        q = 10**i
        while (i * 9**self.n > q):
            q *= 10
            i += 1
        return q   

    def Get(self):
        power_sum_numbers = []
        for i in xrange(10, self._GetLimit(), 1):
            i_as_string = str(i)
            sum_digits_powers = 0
            for di in xrange(len(i_as_string)):
                d = int(i_as_string[di])
                sum_digits_powers += d ** self.n 
                if sum_digits_powers > i:
                    break
            if  sum_digits_powers == i:
                power_sum_numbers.append(i)
        return power_sum_numbers

# Main
def main():
   
    # 443839
    print sum(PowerSumNumbers(5).Get())
    
if __name__ == "__main__":
    main()

    
