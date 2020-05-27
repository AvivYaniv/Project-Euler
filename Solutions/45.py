
import math

TPH = 40755

def IsInteger(f):
    return int(f) == f

def GetTriangleNumberIndex(x):
    return (-1 + math.sqrt(1 + 8*x)) / 2

def IsTriangleNumber(x):
    return IsInteger(GetTriangleNumberIndex(x))

def GetPentagonalNumberIndex(x):
    return (1 + math.sqrt(1 + 24*x)) / 6

def IsPentagonalNumber(x):
    return IsInteger(GetPentagonalNumberIndex(x))

def GetHexagonalNumberIndex(x):
    return (1 + math.sqrt(1 + 8*x)) / 4

def IsHexagonalNumber(x):
    return IsInteger(GetHexagonalNumberIndex(x))

def GetHexagonalNumber(n):
    return n * (2*n -1)

def GetNextTrianglePentagonalHexagonalNumber(tph):
    ntph_h_index = int(GetHexagonalNumberIndex(tph)) + 1
    ntph = GetHexagonalNumber(ntph_h_index)    
    while not (IsTriangleNumber(ntph) and IsPentagonalNumber(ntph)):        
        ntph_h_index += 1
        ntph = GetHexagonalNumber(ntph_h_index)
    return ntph

# Main
def main():
    
    # 1533776805    
    print GetNextTrianglePentagonalHexagonalNumber(TPH)
    
if __name__ == "__main__":
    main()
