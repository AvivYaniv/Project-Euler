
import math

DIGITS                  = 4
NUMER_OF_MEMBERS        = 3
DIFFRENCE               = 3330

def IsPrime(n):
    for i in xrange(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def IsPremutation(a, b):
    a = str(a)
    b = str(b)
    if len(a) != len(b):
        return False
    for ca in a:
        if ca not in b:
            return False
    return True            

def GetPrimePremutations(digits, number_of_members, diffrence):
    minimum = int('1' * digits)
    maximum = int('9' * digits)
    members = []
    for n in xrange(minimum, maximum, 1):
        if IsPrime(n):
            c = 1
            member = n
            prime_members = [member]
            while c < number_of_members and member < maximum:
                member += diffrence
                if IsPrime(member) and IsPremutation(n, member):
                    prime_members.append(member)
                    c += 1
            if c != number_of_members:
                prime_members = []
            else:
                members.append(prime_members)
    return members

# Main
def main():
    
    # 296962999629    
    print "".join([str(n) for n in GetPrimePremutations(DIGITS, NUMER_OF_MEMBERS, DIFFRENCE)[1]])
    
if __name__ == "__main__":
    main()
