
import math

def IsInteger(f):
    return int(f) == f

def GetTriangleNumber(n):
    return (n * (n + 1)) / 2

def GetSquareNumber(n):
    return n**2

def GetPentagonalNumber(n):
    return (n * (3*n - 1)) / 2

def GetHexagonalNumber(n):
    return n * (2*n -1)

def GetHeptagonalNumber(n):
    return (n * (5*n - 3)) / 2

def GetOctagonalNumber(n):
    return n * (3*n - 2)

def CutGrop(group, common_digits):
    beginings = []
    ends = []
    result_invalid = ([], [])
    for m in group:
        m_as_string = str(m)
        m_length = len(m_as_string)        
        if m_length != 2 * common_digits:
            return result_invalid
        if '0' == m_as_string[common_digits-1] or \
           '0' == m_as_string[common_digits]:
            return result_invalid
        beginings.append(m_as_string[0:common_digits])
        ends.append(m_as_string[common_digits:m_length])
    return (beginings, ends)

def IsCyclicGroup(group, common_digits):
    beginings, ends = CutGrop(group, common_digits)
    return sorted(beginings) == sorted(ends)

def IsCommonStartEnd(x_a, b_x, common_digits):
    group = [x_a, b_x]
    beginings, ends = CutGrop(group, common_digits)
    return beginings and ends and beginings[0] == ends[1]

def IsCommonEndStart(a_x, x_b, common_digits):
    group = [a_x, x_b]
    beginings, ends = CutGrop(group, common_digits)    
    return beginings and ends and beginings[1] == ends[0]

def GetNumbers(generator, length):
    numbers = []
    i = 1
    n = generator(i)
    n_length = len(str(n))
    while n_length < length + 1:
        if n_length == length:
            numbers.append(n)
        n = generator(i)
        n_length = len(str(n))        
        i += 1
    return numbers   

import itertools

def GetPremutation(array):
    for p in itertools.permutations(array, len(array)):
        yield p

def GetCyclicFourDigitsTriangleSquarePentagonalHexagonalHeptagonalOctagonalNumbers():
    length = 4
    shapes = []
    common_digits = length / 2
    shape_generators = \
           [GetTriangleNumber, \
            GetSquareNumber, \
            GetPentagonalNumber, \
            GetHexagonalNumber, \
            GetHeptagonalNumber, \
            GetOctagonalNumber]
    number_of_shapes = len(shape_generators)

    for shape_generator in shape_generators:
        shapes.append(GetNumbers(shape_generator, length))

    indexes = [i for i in xrange(number_of_shapes)]

    for premutation in GetPremutation(indexes):
        cycles = []
        shapes_added_counter = 0        
        for i in premutation:
            cycle_with_current_shape = []
            
            if 0 == shapes_added_counter:
                for s in shapes[0]:
                    cycle_with_current_shape.append([s])
            else:            
                for c in cycles:
                    for cs in shapes[i]:
                        if IsCommonEndStart(c[-1], cs, common_digits) and \
                           (True if number_of_shapes - 1 != shapes_added_counter \
                                else IsCommonStartEnd(c[0], cs, common_digits)):
                            cycle_with_current_shape.append(c[::] + [cs])

            shapes_added_counter += 1
            cycles = cycle_with_current_shape
            if not cycles:
                break
        for g in cycles:
            if len(g) == number_of_shapes:
                return g    
    return []

# Main
def main():
    
    # 28684
    print sum(GetCyclicFourDigitsTriangleSquarePentagonalHexagonalHeptagonalOctagonalNumbers())
    
if __name__ == "__main__":
    main()

import math
