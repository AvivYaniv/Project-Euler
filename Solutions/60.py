
import math
import itertools

FRIENDS_NUMBER      =   5

def IsPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

class NumberConcator:
    def __init__(self, validy_method):
        self.d = dict()
        self.validy_method = validy_method

    @staticmethod
    def _CutNumber(n):
        cut_number = []
        n_as_string = str(n)
        n_length = len(n_as_string)
        for i in xrange(1, n_length, 1):
            if '0' == n_as_string[i]:
                continue
            cut_number.append((int(n_as_string[0:i]), int(n_as_string[i:n_length])))
        return cut_number

    def _IsKeyExist(self, a):
        entry = self.d.get(a)
        return entry is not None

    def _AddEntry(self, a, b):
        self.AddKey(a)
        self.d[a].update([b])

    def _IsEntry(self, a, b):
        if not self._IsKeyExist(a):
            return False
        return b in self.d[a]

    def _AddEntries(self, a, b):
        self._AddEntry(a, b)
        self._AddEntry(b, a)

    def _ConnectEntries(self, a, b):
        a_fiends = self.d[a]
        b_fiends = self.d[b]
        self._AddEntries(a, b)
        in_a_not_in_b = list(a_fiends - b_fiends)
        in_b_not_in_a = list(b_fiends - a_fiends)
        for anb in in_a_not_in_b:
            if self._IsMutualValidity(anb, b):
                self._AddEntries(anb, b)
        for bna in in_b_not_in_a:            
            if self._IsMutualValidity(bna, a):
                self._AddEntries(bna, a)

    def AddKey(self, n):
        if not self._IsKeyExist(n):
            self.d[n] = set()
        
    def Add(self, n):
        added_nodes = []
        if self.validy_method(n):
            for (cut_start, cut_end) in NumberConcator._CutNumber(n):
                cuts = [cut_start, cut_end]
                if self._ValidateNumbers(cuts) and \
                   self._IsConcationValid(cut_end, cut_start):                
                    self._ConnectEntries(cut_start, cut_end)
                    added_nodes.extend(cuts)
            self.AddKey(n)
        return added_nodes

    def _ValidateNumbers(self, numbers):
        for n in numbers:
            if not self.validy_method(n):
                return False
        return True

    def _IsConcationValid(self, a, b):
        return self.validy_method(int(str(a) + str(b)))

    def _IsMutualValidity(self, a, b):
        return self._IsConcationValid(a, b) and \
               self._IsConcationValid(b, a)

    def _IsValidGroup(self, group):
        for (a, b) in itertools.permutations(group, 2):
            if not self._IsEntry(a, b):
                if not self._IsMutualValidity(a, b):
                    return False
        return True

    def GetMutualGroup(self, start_node, friends_number):
        friends = list(self.d[start_node])

        # If not enough friends to 
        if len(friends) + 1 < friends_number:
            return []
        
        # Setting mutual group to be start node and it's friends
        # later, removing friends that don't have enough friends in common
        mutual_group = [start_node] + friends[::]

        # Gong over start node friends
        for friend in friends:
            friend_friends = list(self.d.get(friend))
			
            # If friend has no friends - removing it from mutual group
            # as he has not mutual friends at all
            if not friend_friends:
                mutual_group.remove(friend)
            # Else, friend has friends - checking which are mutual
            else:
                # Start node and current friend are mutual
                mutual_friends = [friend, start_node]

                # Going over the mutual group,
                # checking which are friends of currenf friend as well
                for other_friend in mutual_group:
                    if friend != other_friend and other_friend != start_node:                        
                        if other_friend in friend_friends:
                            mutual_friends.extend([other_friend])

                # If friend has'nt enoug friends for
                # being in the mutual group removing him
                if len(mutual_friends) <  friends_number:
                    mutual_group.remove(friend)

        # If mutual group has the exact number of friends
        if len(mutual_group) == friends_number:
            # Validating group members
            if self._IsValidGroup(mutual_group):
                return mutual_group

        # Mutual groups not found
        return []
 
def GetMutualGroup(validation_method, friends_number, start_number, increment):
    n = start_number
    concator = NumberConcator(validation_method)
    while True:                     
        for added_node in concator.Add(n):                
            group = concator.GetMutualGroup(added_node, friends_number)
            if group:                     
                return group            
        n += increment

# Main
def main():
           
    # 26033
    print sum(GetMutualGroup(IsPrime, FRIENDS_NUMBER, 3, 2))
    
if __name__ == "__main__":
    main()
