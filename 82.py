
MATRIX_NAME = 'matrix.txt'

DELIMITER = ','

def ReadMatrixFile(name):
    lists = []
    with open(name) as f:
        lines = f.readlines()
    for line in lines:        
        l = []
        for c in line.strip().split(DELIMITER):
            l.append(int(c))
        lists.append(l)
    return lists

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix        

    @staticmethod
    def Copy(matrix):
        copy = []
        for r in matrix:
            copy.append(r[::])
        return copy

    @staticmethod
    def GetEmpty(rows, columns):
        empty = []
        for r in xrange(rows):
            empty.append([0] * columns)
        return empty

    def GetSize(self):
        return len(self.matrix), len(self.matrix[0])

    def GetMatrixMinimalThreeWaysPathSum(self):
        rows, columns = self.GetSize()
        minimal_sums = Matrix.GetEmpty(rows, columns)

        # First column requires no movment, copying it as sums
        for r in xrange(rows):
            minimal_sums[r][0] = self.matrix[r][0]

        # Solving for each column, right-to-left, with Dynamic Programming
        for c in xrange(1, columns, 1):
            # Going over the rows bottom-to-top
            # Finding minimal sum from left & down
            for r in xrange(rows - 1, -1, -1):
                left_sum = minimal_sums[r][c - 1]
                directions = [left_sum]
                if r != rows - 1:                    
                    down_sum = minimal_sums[r + 1][c]
                    directions.append(down_sum)                
                minimal_sums[r][c] = \
                    self.matrix[r][c] + \
                        min(directions)

            # Going over the rows top-to-bottom
            # Finding minimal sum from up compared to (left & down)
            for r in xrange(rows):
                up_sum = minimal_sums[r - 1][c]
                current_plus_up_sum = self.matrix[r][c] + up_sum
                if current_plus_up_sum < minimal_sums[r][c]:
                    minimal_sums[r][c] = current_plus_up_sum

        return min(minimal_sums[x][rows - 1] for x in xrange(rows))

# Main
def main():
    
    matrix = Matrix(ReadMatrixFile(MATRIX_NAME))
    
    # 260324
    print matrix.GetMatrixMinimalThreeWaysPathSum()
    
if __name__ == "__main__":
    main()
