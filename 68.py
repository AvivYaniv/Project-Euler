
import itertools

def GetPremutation(array):
    for p in itertools.permutations(array, len(array)):
        yield p

def IsEqualSums(arrays):
    array_sum = sum(arrays[0])
    for ai in xrange(1, len(arrays), 1):
        if sum(arrays[ai]) != array_sum:
            return False
    return True

def Magic5gonMaximalSolution():
    N = 5
    max_solution = 0
    maximal_number = 2*N    
    numbers = [n for n in xrange(1, maximal_number + 1, 1)]    
    
    for p in GetPremutation(numbers):
        inner_shape = [p[ii] for ii in [1, 2, 4, 6, 8]]
        # Maximal number should be in outer nodes, to maximize the string        
        if maximal_number in inner_shape:            
            continue

        outer_nodes = [p[oi] for oi in [3, 5, 7, 9]]
        # Outer nodes shuld be larger than 0-node,
        # so solution would be uniqely described        
        if any([o < p[0] for o in outer_nodes]):
            continue                
        
        branch_1 = [p[i] for i in [0, 1, 2]]
        branch_2 = [p[i] for i in [3, 2, 4]]
        branch_3 = [p[i] for i in [5, 4, 6]]
        branch_4 = [p[i] for i in [7, 6, 8]]
        branch_5 = [p[i] for i in [9, 8, 1]]        
        branches = [branch_1, branch_2, branch_3, branch_4, branch_5]

        # All branches should have equal sum, to be called "Magic-n-gon"
        if not IsEqualSums(branches):
            continue
        
        solution = int("".join(["".join(str(n) for n in b) for b in branches]))
        if max_solution < solution:
            max_solution = solution
            
    return max_solution

# Main
def main():

    # 6531031914842725
    print Magic5gonMaximalSolution()
    
if __name__ == "__main__":
    main()
