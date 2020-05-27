
import math

def IsPrime(n):
    if n == 1:
        return False
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def IsComposite(n):
    return not IsPrime(n)

class PowersDictionary:
    def __init__(self):
        self.d = dict()

    def GetPower(self, n):
        p = self.d.get(n)
        if p is None:
            self.d[n] = n**2
        return self.d[n]

def GetGoldbachRepresentation(c, powers):
    for n in xrange(c):        
        p = c - 2*powers.GetPower(n)
        if p <= 0:
            continue
        if IsPrime(p):
            return (p, n)
    return None           

def GetFirstCompositeWithoutGoldbachRepresentation():
    c = 9
    powers = PowersDictionary()
    goldbach_representation = GetGoldbachRepresentation(c, powers)
    while goldbach_representation is not None:
        c += 2
        while IsPrime(c):
            c += 2
        goldbach_representation = GetGoldbachRepresentation(c, powers)
    return c

# Main
def main():
    
    # 5777
    print GetFirstCompositeWithoutGoldbachRepresentation()
    
if __name__ == "__main__":
    main()
