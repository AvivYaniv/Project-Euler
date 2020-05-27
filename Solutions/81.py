
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
    def GetNieghbors(matrix, r, c, directions):
        nieghbors = []
        for i, j in directions:        
            nieghbors.append(matrix[r + i][c + j])
        return nieghbors

    def GetMatrixMinimalTwoWaysPathSum(self):
        directions = [(-1, 0), (0, -1)]
        copy_matrix = Matrix.Copy(self.matrix)
        for r in xrange(len(copy_matrix)):
            for c in xrange(len(copy_matrix[0])):
                current_directions = []
                if r > 0 and c > 0:
                    current_directions = directions
                elif r > 0:
                    current_directions.append(directions[0])
                elif c > 0:
                    current_directions.append(directions[1])
                else:
                    continue
                copy_matrix[r][c] += \
                    min(Matrix.GetNieghbors(copy_matrix, r, c, current_directions))
        return copy_matrix[-1][-1]

# Main
def main():
    
    matrix = Matrix(ReadMatrixFile(MATRIX_NAME))
    
    # 427337
    print matrix.GetMatrixMinimalTwoWaysPathSum()
    
if __name__ == "__main__":
    main()
