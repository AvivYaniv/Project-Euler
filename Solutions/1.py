
M1  = 3
M2  = 5
N   = 1000

def InclusionExclusion(A, B, A_B):
    return A + B - A_B

class ArtithmaticSequence:
    def __init__(self, a1, d):
        self.a1 = a1
        self.d = d

    def Sum(self, an):
        return (self.a1 + an) / 2

    def LimitedSum(self, limit):
        i = self.GetIndex(limit)
        an = self.GetTerm(i)
        return i * (self.a1 + an) / 2

    def GetTerm(self, i):
        return self.a1 + (i - 1)*self.d

    def GetIndex(self, n):
        return ((n - self.a1) / self.d) + 1       

def GetMultiplesSum(m1, m2, limit):
    sequence_m1 = ArtithmaticSequence(m1, m1)
    m1s = sequence_m1.LimitedSum(limit)

    sequence_m2 = ArtithmaticSequence(m2, m2)
    m2s = sequence_m2.LimitedSum(limit)

    m1m2 = m1 * m2
    sequence_m1m2 = ArtithmaticSequence(m1m2, m1m2)
    m1m2s = sequence_m1m2.LimitedSum(limit)

    return InclusionExclusion(m1s, m2s, m1m2s)

# Single-line
print sum(filter(lambda n: n%3 == 0 or n%5 == 0, range(1, N, 1)))

# 233168
print GetMultiplesSum(M1, M2, N-1)
