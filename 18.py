FILE_NAME = 'triangle.txt'

DELIMITER = ' '

def ReadListsFile(name):
    lists = []
    with open(name) as f:
        lines = f.readlines()
    for line in lines:        
        l = []
        for c in line.strip().split(DELIMITER):
            l.append(int(c))
        lists.append(l)
    return lists

class TraingleLists:
    def __init__(self, lists):
        self.lists = lists

    @staticmethod
    def _GetNeighborsIndexes(i):
        return [i, i + 1]

    @staticmethod
    def _GetNeighbors(lists, i, length):
        neighbors = []
        next_list = lists[length + 1]        
        for ni in TraingleLists._GetNeighborsIndexes(i):
            neighbors.append(next_list[ni])
        return neighbors

    def Copy(self):
        copy = []
        for l in self.lists:
            copy.append(l[::])
        return copy
           
    def GetMaximalSum(self):
        lists = self.lists
        lists_number = len(self.lists)
        sums_lists = self.Copy()
        for l in xrange(lists_number - 2, -1, -1):     
            for i in xrange(l + 1):
                sums_lists[l][i] += max(TraingleLists._GetNeighbors(sums_lists, i, l))
   
        return sums_lists[0][0]

# Main
def main():
    lists = ReadListsFile(FILE_NAME)
    triangle = TraingleLists(lists)
    
    # 1074
    print triangle.GetMaximalSum()
    
if __name__ == "__main__":
    main()
