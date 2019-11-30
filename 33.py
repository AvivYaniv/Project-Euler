from fractions import Fraction as f

class Fraction:
    def __init__(self, n, d):
        self.f = f(n, d)

    def ToDecimal(self):
        return float(self.f.numerator) / float(self.f.denominator)

    def FromDecimal(self, decimal):
        self.f = f(decimal).limit_denominator()

    def IsEqual(self, fraction):
        return (self.ToDecimal() == fraction.ToDecimal())

    def IsLessThan(self, fraction):
        return (self.ToDecimal() < fraction.ToDecimal())

    def __str__(self):
        return self.f.__str__()

    def __repr__(self):
        return self.__str__()

def GetDigitCancellingFractions():
    digit_cancelling_fractions = []
    one = Fraction(1, 1)
    for a in xrange(1, 10, 1):
        for b in xrange(1, 10, 1):
            if a == b:
                continue
            for c in xrange(1, 10, 1):
                digit_cancelled_fraction = Fraction(a, c)
                """
                ab
                --
                bc
                """
                fraction1 = Fraction(10*a + b, 10*b + c)
                if fraction1.IsLessThan(one):
                    if fraction1.IsEqual(digit_cancelled_fraction):
                        digit_cancelling_fractions.extend([fraction1])
                """
                ba
                --
                cb
                """
                fraction2 = Fraction(10*b + a, 10*c + b)
                if fraction2.IsLessThan(one):
                    if fraction2.IsEqual(digit_cancelled_fraction):
                        digit_cancelling_fractions.extend([fraction2])
    return digit_cancelling_fractions

# Main
def main():

    multipication = 1
    for fraction in GetDigitCancellingFractions():
        multipication *= fraction.ToDecimal()
        
    # 100
    multipication_fraction = Fraction(1, 1)
    multipication_fraction.FromDecimal(multipication)
    print multipication_fraction.f.denominator
    
if __name__ == "__main__":
    main()
