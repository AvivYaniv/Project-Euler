MATRIX = \
[[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8], \
 [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0], \
 [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65], \
 [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91], \
 [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80], \
 [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50], \
 [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70], \
 [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21], \
 [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72], \
 [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95], \
 [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92], \
 [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57], \
 [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58], \
 [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40], \
 [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66], \
 [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69], \
 [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36], \
 [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16], \
 [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54], \
 [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

N = 20
SEQUENCE_LENGTH = 4

class Matrix:
    def __init__(self, ROWS, COLS, matrix):
        self.ROWS = ROWS
        self.COLS = COLS        
        self.matrix = matrix
        if ROWS == COLS:
            self.N = ROWS

    def GetHorizontalSegments(self):
        segments = []
        for ri in range(self.ROWS):
            row = self.matrix[ri]
            segments.append(row[::])
        return segments

    def GetVerticalSegments(self):
        segments = []
        for ci in range(self.COLS):
            col = []
            for ri in range(self.ROWS):
                cell = self.matrix[ri][ci]
                col.append(cell)
            segments.append(col)
        return segments

    def GetMainDiagonalParallelSegments(self):
        segments = []
        
        diagonal = []
        for i in range(self.N):
            diagonal.append(self.matrix[i][i])
        segments.append(diagonal)
        
        for d in  range(1, self.N):
            diagonal_up = []
            diagonal_down = []
            for i in range(self.N):
                if i + d >= self.N:
                    continue
                diagonal_up.append(self.matrix[i + d][i])
                diagonal_down.append(self.matrix[i][i + d])
            segments.append(diagonal_up)
            segments.append(diagonal_down)
        return segments

    def GetMinorDiagonalParallelSegments(self):
        segments = []
        
        diagonal = []
        for i in range(self.N):
            diagonal.append(self.matrix[i][(self.N - 1) - i])
        segments.append(diagonal)
        
        for d in  range(1, self.N):
            diagonal_up = []
            diagonal_down = []
            for i in range(self.N):
                if i + d >= self.N:
                    continue
                diagonal_up.append(self.matrix[i][(self.N - 1) - i - d])
                diagonal_down.append(self.matrix[i + d][(self.N - 1) - i])
            segments.append(diagonal_up)
            segments.append(diagonal_down)
        return segments

    def GetDigonalSegments(self):
        segments = []
        segments.extend(self.GetMainDiagonalParallelSegments())
        segments.extend(self.GetMinorDiagonalParallelSegments())
        return segments

def GetMultipicationOfArray(array):
    multipication = 1
    for v in array:
        multipication *= v
    return multipication

def GetMaximalMultipication(segments, length):
    parts = []

    for s in segments:
        part = []
        for v in s:
            if v != 0:
                part.append(v)
            else:
                if len(part) > 0:
                    parts.append(part)
                    part = []
        if len(part) > 0:
            parts.append(part)

    max_multipication_value = 0
    max_multipication_sequence = []

    current_multipication_value = 0
    for p in parts:
        if len(p) >= length:
            for i in range(len(p) - length + 1):
                current_multipication_sequence = (p[i:])[:length]                
                current_multipication_value = GetMultipicationOfArray(current_multipication_sequence)
                if current_multipication_value > max_multipication_value:
                    max_multipication_value = current_multipication_value
                    max_multipication_sequence = current_multipication_sequence
    return max_multipication_value
    
# Main
def main():
    matrix = Matrix(N, N, MATRIX)

    horizontal_segments = matrix.GetHorizontalSegments()    
    vertical_segments = matrix.GetVerticalSegments()        
    diagonal_segments = matrix.GetDigonalSegments()

    horizontal_maximal_multipication = GetMaximalMultipication(horizontal_segments, SEQUENCE_LENGTH)
    vertical_maximal_multipication = GetMaximalMultipication(vertical_segments, SEQUENCE_LENGTH)
    diagonal_maximal_multipication = GetMaximalMultipication(diagonal_segments, SEQUENCE_LENGTH)

    maximal_multipication = max( \
        max(horizontal_maximal_multipication, \
            vertical_maximal_multipication), \
        diagonal_maximal_multipication)
    
    # 70600674
    print maximal_multipication
    
if __name__ == "__main__":
    main()
