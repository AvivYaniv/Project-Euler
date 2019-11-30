
import networkx

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
    def GetSize(matrix):
        return len(matrix), len(matrix[0])

    @staticmethod
    def GetNieghborIndexes(matrix, r, c, directions):
        nieghbors = []
        rows, columns = Matrix.GetSize(matrix)
        for i, j in directions:
            nieghbor = (current_r, current_c) = (r + i, c + j)
            if 0 <= current_r < rows and \
               0 <= current_c < columns:
                nieghbors.append(nieghbor)
        return nieghbors

    def GetAt(self, p):
        r, c = p
        return self.matrix[r][c]

    def GetMatrixMinimalFourWaysPathSum(self, source, target):
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        graph = networkx.DiGraph()
        rows, columns = Matrix.GetSize(self.matrix)
        for r in xrange(rows):
            for c in xrange(columns):
                current = (r, c)
                for neighbor in Matrix.GetNieghborIndexes(self.matrix, r, c, directions):
                    graph.add_edge(current, neighbor, weight = self.GetAt(neighbor))  
        return self.GetAt(source) + networkx.dijkstra_path_length(graph, source, target)

# Main
def main():
    
    matrix = Matrix(ReadMatrixFile(MATRIX_NAME))
    
    # 425185
    top_left = (0,0)
    rows, colums = Matrix.GetSize(matrix.matrix)
    bottom_right = (rows-1,colums-1)
    print matrix.GetMatrixMinimalFourWaysPathSum(top_left, bottom_right)
    
if __name__ == "__main__":
    main()
