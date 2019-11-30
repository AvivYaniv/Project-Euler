N = 1001

class Helix:
    def __init__(self, N):
        self.N = N

    def _InitMatrix(self):
        matrix = []
        for i in xrange(self.N):
            matrix.append([0] * self.N)
        return matrix

    def _GetSteps(self):
        steps = []
        for s in xrange(1, self.N, 1):
            steps.append(s)
            steps.append(s)
        steps.append(self.N)
        return steps
    
    def GetMatrix(self):
        helix_matrix = self._InitMatrix()

        n = 1
        steps = self._GetSteps()
        x, y = ((self.N - 1) / 2,) * 2     

        si = 0
        while n <= self.N**2:
            for i in range(steps[si]):
                helix_matrix[x][y] = n
                if si % 4 == 0:
                    y += 1
                elif si % 4 == 1:
                    x += 1
                elif si % 4 == 2:                
                    y -= 1
                elif si % 4 == 3:
                    x -= 1
                n += 1
            si += 1 
            
        return helix_matrix

def GetDiagonalsSum(matrix):    
    n = len(matrix)
    sum = 0
    for i in xrange(n):
        sum += matrix[i][i]
        if (i, i) != (i, n - i - 1):
            sum += matrix[i][n - i - 1]
    return sum

# Main
def main():
	
    # 669171001
    print GetDiagonalsSum(Helix(N).GetMatrix())
    
if __name__ == "__main__":
    main()
