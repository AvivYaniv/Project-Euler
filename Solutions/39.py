PERIMITER_LIMIT = 1000

import math

def SetPowers(array):
    for i in xrange(len(array)):
        array[i] = i*i

def GetRightAngleTrianglesByPerimeter(perimeter_limit):
    powers = [0] * (perimeter_limit + 1)
    SetPowers(powers)
    perimeter_solutions = [[] for i in range(perimeter_limit + 1)]
    for p in xrange(3, perimeter_limit, 1):
        for c in xrange(1, p, 1):
            for a in xrange(1, c, 1):
                b = p - (a + c)
                if a + b <= c:
                    continue                
                if powers[a] + powers[b] == powers[c]:
                    perimeter_solutions[p].append((a, b, c))
    return perimeter_solutions

# Main
def main():

    max_solutions = 0
    max_solutions_index = 0
    perimeter_solutions = GetRightAngleTrianglesByPerimeter(PERIMITER_LIMIT)
    for solution_index in xrange(len(perimeter_solutions)):
        number_of_solutions = len(perimeter_solutions[solution_index])
        if max_solutions < number_of_solutions:
            max_solutions = number_of_solutions
            max_solutions_index = solution_index
    
    # 840
    print max_solutions_index
    
if __name__ == "__main__":
    main()
