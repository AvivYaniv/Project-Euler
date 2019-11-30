DIGITS              = "123456789"

import itertools

def GetPandigitalProducts(word):
    x = ""
    products = set()
    length = len(word)
    for p in itertools.permutations(word, ):
        x = "".join(p)
        multiplicandSmallerThanProduct = True
        for ai in xrange(1, length):
            if not multiplicandSmallerThanProduct:
                break            
            a = x[:ai]
            for bl in xrange(1, length - ai):                
                b = x[ai:(ai+bl)]                
                c = x[(ai+bl):]
                if len(a) > len(c):
                    multiplicandSmallerThanProduct = False
                    break
                if int(a) * int(b) == int(c):
                    products.update([int(c)])                
    return products

# Main
def main():

    # 45228
    print sum(GetPandigitalProducts(DIGITS))
    
if __name__ == "__main__":
    main()


