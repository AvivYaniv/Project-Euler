
def IsValidArray(array, valid_values):    
    for v in array:
        if v not in valid_values:
            return False
    return True

def SetDigitsCounter(number, digits_counter):    
    for d in str(number):
        digits_counter[int(d)] += 1
            
def IsPandigitalMultipication(number):
    n = 2    
    digits_counter = [0] * 10
    pandigital_multipication = str(number)
    SetDigitsCounter(number, digits_counter)
    while IsValidArray(digits_counter, [0, 1]):
        if 0 == digits_counter[0] and \
           9 == sum(digits_counter[1:]) and \
           n > 1:
            return (True, int(pandigital_multipication))        
        multipication = n * number
        multipication_as_tring = str(multipication)
        pandigital_multipication += multipication_as_tring
        SetDigitsCounter(multipication_as_tring, digits_counter)
        n += 1
    return (False, 0)

def GetMaximalPandigitalMultipication():
    maximal_pandigital_multipication = 0
    for number in xrange(1, 99999, 1):
        (is_pandigital_multipication, pandigital_multipication)  = \
            IsPandigitalMultipication(number)
        if is_pandigital_multipication and \
           maximal_pandigital_multipication < pandigital_multipication:            
            maximal_pandigital_multipication = pandigital_multipication
    return maximal_pandigital_multipication

# Main
def main():
    
    # 932718654
    print GetMaximalPandigitalMultipication()
    
if __name__ == "__main__":
    main()
